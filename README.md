# XMLExtractor
This simple program can extract the xml file from your e-invoice. Without uploading your sensitive PDFs to any website!

## Execution of the Program
If Python is installed, run the run.py via
python run.py

To create the Executeable, install PyInstaller and run:
python -m PyInstaller -F --noconsole --icon icon.ico --name XMLExtractor.exe run.py 

## Functionality
The start-up window will list you all the pdf files in your directory. 
By default, this is the Downloads folder, but it can be changed by pressing the button "Change Folder".
If you added files recently while the XML Extractor was already open, you can refresh the view by pressing "Refresh Files".

You can Extract XML (and other embedded files) from your PDFs by selecting them in the list and clicking the button "Extract Embedded Files" on the bottom.

For each of the selected PDFs, a directory will be created with the same name as the pdf (without the file extension) which contains all the embedded files. 
You can choose to include the pdf aswell by checking the box "Move PDFs to Subfolder". In that case, it will move into the subfolder, otherwise it would remain in its original location.

If you want more feedback on what happened and which files were successfully extracted, you can check "Show Summary".
Now you will get a summary of the extracted files after clicking on "Extract Embedded Files".

