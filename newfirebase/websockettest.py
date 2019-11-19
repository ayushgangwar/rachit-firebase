import asyncio
import random
import websockets
import datetime
import pandas as pd  
import time 
import csv 
from rachitnew import websocketcall

# import BankNiftyExecution
# from BankNiftyExecution import on_ticks

async def time(websocket, path):
    i=1
    print("loop started")
    while True:
        cc=websocketcall(i)
        i=i+1
        dd=[]
        print(cc)
        dd=cc.to_string(index=False)

        await websocket.send(str(dd))
        await asyncio.sleep(random.random() * 3)

# var connection = new websockets('ws://localhost:8080/', 'echo-protocol')
start_server = websockets.serve(time, "127.0.0.1", 5675)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()