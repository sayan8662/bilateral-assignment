'''   
Make Folders named Processing,queue and processed and Write a code that makes a file(txt) every second in the Processing folder, picks up all the files from processing and moves all the files to queue every 5 seconds. It then picks files from the queue folder and updates a column in MySQL/mongoDB table as 0/1 and moves the file to the Processed folder
Also, make sure that no files are moved from Processing to queue until the queue folder is empty.

'''



''' load all the required libraries '''

from time import sleep
from threading import *
import shutil
import os
import warnings
import pymysql
warnings.filterwarnings('ignore')


''' This class is used to create a folders automatically. And clear the database for the first time '''

class Folders:
    def __init__(self):
        self.Queue = "Queue"
        self.Processing = "Processing"
        self.Processed = "Processed"
        con=pymysql.connect(host='localhost',user='root',password='root',database='assignment')
        cur=con.cursor()
        cur.execute("delete from files")
        con.commit()
        con.close()

        if(os.path.exists(self.Queue)) and (os.path.exists(self.Processed)) and (os.path.exists(self.Processing)):
            shutil.rmtree(self.Queue)
            shutil.rmtree(self.Processing)
            shutil.rmtree(self.Processed)
            
            os.mkdir(self.Queue)
            os.mkdir(self.Processing)
            os.mkdir(self.Processed)
        else:
            os.mkdir(self.Queue)
            os.mkdir(self.Processing)
            os.mkdir(self.Processed)




''' Creating blank file every second in Processing folder '''

class Processing(Thread):
    def run(self):
        i = 1
        while(True):
            open("Processing/file_"+str(i)+".txt","w")
            i += 1
            sleep(1)



''' Now moving all the files in every 5 seconds from Processing folder to Queue folder. In every five seconds, 
processing folder creates the 5 files, then after creating the 5 files in 5 seconds, moved to the Queue folder. '''

class Queue(Thread):
    def run(self):
        src = 'Processing'
        dest = 'Queue'
        while(True):
            if len(os.listdir(src)) == 5: 
                for file in os.listdir(src):
                    file_name = os.path.join(src, file)
                    shutil.move(file_name, dest)
                    
        

''' Now moved all the files from Queue folder to Processed folder and update the status in the database for each file with processed '''

class Processed(Thread):
    def run(self):
        dest = 'Processed'
        src = 'Queue'
        while(True):
            sleep(2)
            if len(os.listdir(src)) != 0:
                for file in os.listdir(src):
                    con=pymysql.connect(host='localhost',user='root',password='root',database='assignment')
                    cur=con.cursor()
                    cur.execute('insert into files values(%s,%s)',(file,1))
                    con.commit()
                    con.close()
                    file_name = os.path.join(src, file)
                    shutil.move(file_name, dest)




''' Create object of Folder Class '''
f = Folders()

'''Creating objects of every thread'''
Processing_thread = Processing()
Queue_thread = Queue()
Processed_thread = Processed()


'''Start the Thread'''
Processing_thread.start()
Queue_thread.start()
Processed_thread.start()