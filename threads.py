#I/O band
#import time

#def study_math():
#    time.sleep(3)
#    print("I have studied physics")

#def study_physics():
#    time.sleep(5)
#    print("I have studied phuysics")

#def study_english():
#    time.sleep(2)
#    print("I have studied english")

#current_time = time.time()

#study_math()
#study_physics()
#study_english()

#now = time.time()

#print("Elappsed time:",now - current_time)




#I/O band
#import time
#import threading

#def study_math():
#    time.sleep(3)
#    print("I have studied math")

#def study_physics():
#    time.sleep(5)
#    print("I have studied physics")

#def study_english():
#    time.sleep(2)
#    print("I have studied english")

#current_time = time.time()

#task_1 =threading.Thread(target = study_math)
#task_2 =threading.Thread(target = study_physics)
#task_3 =threading.Thread(target = study_english)

#task_1.start()
#task_2.start()
#task_3.start()

#task_1.join()
#task_2.join()
#task_3.join()

#study_math()
#study_physics()
#study_english()

#now = time.time()

#print("Elappsed time:",now - current_time)


import time
import threading

done =False


def my_counter(title):
    counter = 1
    print("This is title",title)
    while not done:
        time.sleep(1)
        print(counter)
        counter += 1

task_1 = threading.Thread(target = my_counter ,args =("Hello World",))
task_1.start()

input("wanna wxit?")
done = True    