import os
import xml.etree.ElementTree as ET
import pandas as pd
import re  # For regex operations

# Path to the folder containing extracted QTI folders
qti_folder = "Lab1"
data = []

# Namespace in the XML file (adjust based on your file)
namespace = {"qti": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2"}

# Function to remove HTML tags from text
def clean_text(text):
    if text:
        # Remove specific <font> tags but preserve their inner content
        clean_text = re.sub(r'<font[^>]*>', '', text, flags=re.DOTALL)
        clean_text = re.sub(r'</font>', '', clean_text, flags=re.DOTALL)
        # Remove any other HTML tags
        clean_text = re.sub(r'<.*?>', '', clean_text)
        # Replace problematic apostrophes with the correct one
        clean_text = clean_text.replace("‘", "'").replace("’", "'")
        return clean_text.strip()
    return text

# List of question types to remove
excluded_question_types = [
    "text_only_question", "essay_question", "true_false_question", 
    "multiple_answers_question", "numerical_question"
]

# Iterate through each folder
for folder in os.listdir(qti_folder):
    folder_path = os.path.join(qti_folder, folder)
    if os.path.isdir(folder_path):
        # Find the XML file in the folder
        for file in os.listdir(folder_path):
            if file.endswith(".xml"):
                xml_file = os.path.join(folder_path, file)
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # Process each question
                for item in root.findall(".//qti:item", namespace):
                    question = {}

                    # Column A
                    question_type = item.find(".//qti:fieldentry", namespace).text
                    if question_type in excluded_question_types:
                        continue  # Skip this question if the type is in the excluded list
                    if question_type == "multiple_choice_question":
                        question["Question Type"] = "MC"
                        

                    # Column B
                    question[""] = None 

                    # Column C
                    question["Points"] = item.find(".//qti:qtimetadatafield[qti:fieldlabel='points_possible']/qti:fieldentry", namespace).text or "0"
                    # question["Quiz Name"] = root.get("title", "Unknown Quiz")
                    # question["Question ID"] = item.get("ident", "Unknown ID")

                    # Column D
                    # Extract question text
                    question_text = item.find(".//qti:mattext", namespace)
                    question["Question"] = clean_text(question_text.text if question_text is not None else "No Question Text")


                    # Extract answers
                    answers = []
                    correct_answer_indices = []

                    # Find the correct answer identifiers from <varequal> in <respcondition>
                    correct_idents = [
                        var.text for var in item.findall(".//qti:respcondition/qti:conditionvar/qti:varequal", namespace)
                    ]

                    # Process correct answers first
                    for idx, response in enumerate(item.findall(".//qti:response_label", namespace), start=1):
                        answer_text = response.find(".//qti:mattext", namespace)
                        answer_ident = response.get("ident")
                        answer_text = answer_text.text if answer_text is not None else "No Answer Text"
                        
                        # Check if the answer is correct
                        if answer_ident in correct_idents:
                            correct_answer_indices.append(str(idx))  # Store the numeric index of the correct answer

                    # Save the correct answer(s) as numbers
                    question["Correct Answer"] = clean_text(" | ".join(correct_answer_indices))

                    # Process each <response_label> for answers
                    for idx, response in enumerate(item.findall(".//qti:response_label", namespace), start=1):
                        answer_text = response.find(".//qti:mattext", namespace)
                        answer_ident = response.get("ident")
                        answer_text = answer_text.text if answer_text is not None else "No Answer Text"
                        
                        # Add each answer as its own column, e.g., "Answer 1", "Answer 2"
                        question[f"Answer {idx}"] = clean_text(answer_text)

                    # Remove empty answer columns
                    question.pop("Answer 5", None)
                    question.pop("Answer 6", None)

                    # Add the question to the data list
                    data.append(question)





# Convert to a DataFrame and export to CSV
df = pd.DataFrame(data)
df.to_csv("questions_output.csv", index=False, header=False)
