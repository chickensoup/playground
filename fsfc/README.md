This is a crawler to get the real estate information from Foshan City Government's official site.

Usage: python fsfc_projc.py [start-index] [end-index]

It will read the project code from project_code_list.txt file and then get the project and room information. start-index is the start index of the project in the txt file. Default is 0. end-index is the end index of the project in the txt file. Default is start-index+50.

The script will get all the project information for the project with project code in the file with index in range(start-index, end-index).
This means if you have start-index=0 and end-index=50, then project code index 0~49 will be processed.