import requests
import functools
import asyncio

async def get(url, *args, **kwargs):
    resp = await asyncio.get_running_loop().run_in_executor(None, functools.partial(requests.get, url, *args, **kwargs))
    return resp

async def post(url,data, *args, **kwargs):
    resp = await asyncio.get_running_loop().run_in_executor(None, functools.partial(requests.post, url, data, *args, **kwargs))
    return resp
