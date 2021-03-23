import asyncio

class Shop(object):
    def __init__(self,breads):
        self.breads = breads
        self.saleCount = 0
    
    async def consume(self,name):
        if (self.breads == 0):
            await self.produce()
        self.breads -= 1
        self.saleCount += 1
        print("total sale {0},buyer is {1}".format(self.saleCount,name))
    
    async def produce(self):
        await asyncio.sleep(1)
        self.breads += 1
        print("shop has made one bread")

shop=Shop(5)
tasks=asyncio.wait([shop.consume((i+1)) for i in range(10)])
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
loop.close()

 