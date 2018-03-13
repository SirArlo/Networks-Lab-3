
#!/usr/bin/python


import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = threadID
    def run(self):
        print("Starting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        #print("%s: %s %d" % (threadName, time.ctime(time.time()),counter))
        print("%s: %s %d" % (threading.current_thread().getName(), time.ctime(time.time()),counter))
        print(threading.active_count())
        #print (threading.enumerate())
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 10)
thread2 = myThread(2, "Thread-2", 5)
thread3 = myThread(3, "Thread-3", 2)
thread4 = myThread(4, "Thread-4", 3)
thread5 = myThread(5, "Thread-5", 4)


# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

print("Exiting Main Thread")







