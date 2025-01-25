# Canvas Quiz Automation: CSV to QTI Converter Guide

## Table of Contents

1. [CSV to Canvas (QTI 2.0) Converter](#csv-to-canvas-qti-20-converter)
2. [Instructions for Formatting CSV File](#instructions-for-formatting-csv-file)
3. [Adding Questions from a Question Bank](#adding-questions-from-a-question-bank)
4. [Creating Your Own Question Bank](#creating-your-own-question-bank)

## CSV to Canvas (QTI 2.0) Converter
[CSV to Canvas Converter](https://canconvert.k-state.edu/qti/)

## Instructions for Formatting CSV File
[How to Add Quiz Questions to Canvas by Converting CSV Files to QTI Zip Files](https://dl.sps.northwestern.edu/canvas/2021/06/add-quiz-questions-to-canvas-by-converting-csv-files-to-qti-zip-files/)

---

## Adding Questions from a Question Bank

1. **Create a new quiz on Canvas:**  
   - Navigate to *Quizzes* > *+ Quiz* and rename the quiz as desired.  
     ![image](https://github.com/user-attachments/assets/358c7c12-b985-423c-9c59-b307a778f49e)
     
2. **Add questions from the Question Bank:**  
   - Go to the *Questions* tab and click *Find Questions.*  
     ![image](https://github.com/user-attachments/assets/8fc0a6d3-3805-4e07-91d8-db8989e9f711)  
   - Find the desired Question Bank and click *Select All.* Scroll down and click *Add Questions.*  
     ![image](https://github.com/user-attachments/assets/052d64ff-4704-40dd-8e60-107f3389a0ae)

3. **Save the quiz:**  
   - Scroll down and click *Save* (be careful not to click *Save and Publish*).  

4. **Export the quiz in QTI format:**  
   - Go to *Settings* and click *Export Course Content* on the right-hand side.  
     ![image](https://github.com/user-attachments/assets/023d5d40-ec09-414c-b151-c9de38eac2ff)  
   - Under *Export Type,* select *Quiz.* Choose either *All Quizzes* or the specific quiz you created, then click *Create Export.*  
     ![image](https://github.com/user-attachments/assets/19c3e717-8622-4257-8ac6-45fcf9007e3f)

5. **Download the export:**  
   - Your export will appear at the top of the page. Refresh the page if necessary. Once it’s ready, download the zipped QTI folder.  
     ![image](https://github.com/user-attachments/assets/13f157d1-379a-41fe-a732-efd473a147fd)

6. **Prepare the QTI folder:**  
   - Move the downloaded folder to your workspace, unzip it, and place the `qti_to_csv.py` script in the same location. Update the script to point to the unzipped folder, then save the changes.

7. **Create a Python virtual environment:**  
   - On Linux:  
     ```bash
     python3 -m venv <venv_name>
     ```  
     (For Windows, the command might differ slightly.)

8. **Activate the virtual environment:**  
   - On Linux:  
     ```bash
     source <venv_name>/bin/activate
     ```

9. **Install Pandas:**  
   ```bash
   pip install pandas

10. **Run the Script:**  
   - Make sure the path to the folder is specified.  
     ![Specify Folder Path](https://github.com/user-attachments/assets/16945ccd-8490-4fcf-99fd-d4776f6f705c)  
   - Then run the script. This will export a CSV file.  
     ![Running Script](https://github.com/user-attachments/assets/ea42b080-3496-44eb-b882-7e97fae1eadb)  
   - The exported CSV file will be generated. Feel free to rename it:  
     ![Exported CSV File](https://github.com/user-attachments/assets/b7304484-8952-4521-978d-42f1dab4c9f4)  

11. **Import the CSV File into Google Drive and Open as Google Sheets.**  

12. **Add Extra Questions If Needed:**  
   - Make sure to follow Step 1 in the [Instructions for Formatting CSV File](https://dl.sps.northwestern.edu/canvas/2021/06/add-quiz-questions-to-canvas-by-converting-csv-files-to-qti-zip-files/).

13. **Export as a CSV File.**  

14. **Import into the [CSV to Canvas (QTI 2.0) Converter](https://canconvert.k-state.edu/qti/):**  
   - Perform the conversion. This will export a QTI zipped folder.  

15. **Import into Canvas:**  
   - Go into Canvas, and click **Import Course Content** on the right.  
     ![Import Course Content](https://github.com/user-attachments/assets/023d5d40-ec09-414c-b151-c9de38eac2ff)  

16. **Set the Content Type to QTI .zip File:**  
    - Browse for the zip folder and click **Import.**  
      ![Set Content Type](https://github.com/user-attachments/assets/b7bb8f82-9f25-4ebb-b139-4e149d530e1b)  

17. **Monitor the Import Progress:**  
    - Wait and check the progress of the import under *Current Jobs.*  
      - If it fails, check the CSV file you edited in Google Sheets and ensure there are no errors in any rows.
        (There may be HTML tags that are used, or images that are referenced. You must delete these rows, and manually import them into the Question Bank through Canvas later.)
      - If it is successful, it will say *Completed,* and you will see the imported Quiz under *Quizzes.*  


## Creating your own Question Bank
1. Open this website: [Instructions for Formatting CSV File](https://dl.sps.northwestern.edu/canvas/2021/06/add-quiz-questions-to-canvas-by-converting-csv-files-to-qti-zip-files/).
   - Go to Step 1 in the website, and download the CSV Template.
    
2. **Import the CSV File into Google Drive and Open as Google Sheets.**  
Create your questions in the proper format specified in the website in Step 1.

3. **Export as a CSV File.**
  
4. **Import into the [CSV to Canvas (QTI 2.0) Converter](https://canconvert.k-state.edu/qti/):**  
   - Perform the conversion. This will export a QTI zipped folder.  

5. **Import into Canvas:**  
   - Go into Canvas, and click **Import Course Content** on the right.  
     ![Import Course Content](https://github.com/user-attachments/assets/023d5d40-ec09-414c-b151-c9de38eac2ff)  

6. **Set the Content Type to QTI .zip File:**  
    - Browse for the zip folder and click **Import.**  
      ![Set Content Type](https://github.com/user-attachments/assets/b7bb8f82-9f25-4ebb-b139-4e149d530e1b)  

7. **Monitor the Import Progress:**  
    - Wait and check the progress of the import under *Current Jobs.*  
      - If it fails, check the CSV file you edited in Google Sheets and ensure there are no errors in any rows.
        (There may be HTML tags that are used, or images that are referenced. You must delete these rows, and manually import them into the Question Bank through Canvas later.)
      - If it is successful, it will say *Completed,* and you will see the imported Quiz under *Quizzes.*  



