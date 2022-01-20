# Bilateral-Solutions-Assessment
Here we are going to create Folders named Processing, Queue and Processed and after  that we are going to write a code that makes a text formated file every second in the Processing folder, picks up all the files from processing and moves all the files to the queue in every 5 seconds. It then picks files from the queue folder and updates a column in MySQL/mongoDB table as 0/1 and moves the file to the Processed folder Also, make sure that no files are moved from Processing to queue until the queue folder is empty.

