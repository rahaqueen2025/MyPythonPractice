import time
import asyncio

#async,await     keyword of this module
#await = only use in functions that is "async"
#await = روی هر تابعی قابل اجرا نیست یعنی هرجا نمیتونه بگه صبر کن

async def toast_bread():
    await asyncio.sleep(2)          
    return"Your bread is ready"

async def cook():
    await asyncio.sleep(3) 
    return"Your breakfast is ready"

async def main(): 
    current = time.time()  

    result =asyncio.gather(toast_bread(),cook()) 
    bread,cook_result = await result
    print("First result", bread)
    print("second result",cook_result)

    #await toast_bread()
    #await cook()

    now = time.time()
    print("Elappsed time is:", now - current)
   
if __name__ =="__main__":
    asyncio.run(main())