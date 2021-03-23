import asyncio
import time
import sys
sys.path.append(".")
import requestx


async def getHtml(url):
    print("begin to request {0}".format(url))
    headers = {
        'user-agent':"Mozilla"
    }
    resp = await requestx.get(url,headers=headers)
    print("{1} end to request {0}".format(url,resp.status_code))

def main():
    tasks=asyncio.wait([getHtml(url) for url in ['http://www.cnblogs.com', 'http://www.sina.com.cn','https://www.jianshu.com','https://xueqiu.com']])
    # tasks=[asyncio.ensure_future(download(i)) for i in ['http://www.cnblogs.com', 'http://www.sina.com.cn']]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    loop.close()
    # asyncio.run(tasks)
    print("main over")

main()

    


        



