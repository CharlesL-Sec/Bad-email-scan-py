# BAD Emial Scanner using
# Import Queue module
from queue import Queue
# Import threading modules
import threading

# Import time module for using stop watch
import time
# Net work sockets
import socket
# email protocols
import smtplib



# Setup Threading queue 
print_lock = threading.Lock()
# Assign queue funtion to q
q = Queue()
# A list of none valid email addresses in the file



# Job counter
count_valid = 0

# Failure queue
nonvalid_email = []

# Open my emails list file
f = open("emails.txt","r")

''' email_Queue  = Queue()
if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
    print("Valid")
    email_Queue.put(email)
else:
    print("Invalid")email_Queue  = Queue()
if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
    print("Valid")
    email_Queue.put(email)
else:
    print("Invalid") '''

# This function is where the actual task is done
# Function definition
def exampleJob(worker):
    print("Worker function")
    # This is a dummy task that could be a useful item
    print("Example Job function", threading.current_thread().name, worker)
    # this shows the threads in action for learning 
   
       

# This is where we put jobs into the queue
def threader():
    # Loops while there is something in the queue
    while True:
        # This "pops" a jon off the queue.
        # This could be the job board.
        worker = q.get()
        # Call the worker function with the job to be done
        exampleJob(worker)
        # When the work is done the thread is closed
        q.task_done()


# This is the factory manager dishing out the work.
# We'll have 10 workers


for x  in range(10):
    # Adds the threads 
    t = threading.Thread(target = threader) # The target = calls the theading modules
    # Sets the thread to run in the background 
    t.daemon = False
    # This starts the work day
    t.start()
    # Starts the stops workday
start = time.time()

# This is the number of tasks to perform
# open a file to process


# Read file line by line and check whether email is valid 
for line in f:
    item = line.strip()  # Strips newlines
    # only add valid emaild addresses
    if ('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', item):
        q.put(item) # put items in the queue
    else:
        # Not valid list
        print("/nNone valid/n", item)
        non_valid.append(item)
        print
    endif:
        
    # Adds the threads 
    t = threading.Thread(target = threader)
    # Sets the thread to run in the background 
    t.daemon = True
    # This starts the work day
    t.start()
    


q.join()

# Report
print(f"Entire job took", time.time() - start, "to check", count_valid, "email addressses")
print(nonvalid_email)
