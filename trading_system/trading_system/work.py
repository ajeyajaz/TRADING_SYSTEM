import asyncio

async def say_hello(delay ,task):

   
    await asyncio.sleep(delay)
    print('hello' ,task)

async def main():
    print('hello world')


    await asyncio.gather(say_hello(2,'1'),say_hello(1,5),say_hello(1,'3'))
   



asyncio.run(main())