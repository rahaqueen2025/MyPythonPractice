#cpu bounding tasks

import time
from multiprocessing import process

result_task_1 = []
result_task_2 = []

def calculate_1(value):
    for i in range(1,value + 1):
        result_task_1.append(i**2)

def calculate_2(value):
    for i in range(1,value + 1):
        result_task_2.append(i**2)


#current = time.time()

calculate_1(10000000)
calculate_2(10000000)

#now = time.time()
#print("Elappsed time is :", now - current)  
 
 
print(__name__)    # نشون میده برنامه ما ایمپورت شده هست یااینکه مستقیم کال شده
# main   اگر مستقیم اجرا بشه
#processing   اگر از طریق ایمپورت شدن اجرا بشه


if __name__ == "__main__":
    current = time.time()
    #print("You called this file directly")
    task_1 =process(target=calculate_1,args=(100000000,))
    task_2 =process(target=calculate_2,args=(100000000,))
    task_3 =process(target=calculate_1,args=(100000000,))
    task_4 =process(target=calculate_2,args=(100000000,))

    task_1.start()
    task_2.start()
    task_3.start()
    task_4.start()

   
    task_1.join()
    task_2.join()
    task_3.join()
    task_4.join()
    now = time.time()
    print("Elappsed time is :", now - current)
