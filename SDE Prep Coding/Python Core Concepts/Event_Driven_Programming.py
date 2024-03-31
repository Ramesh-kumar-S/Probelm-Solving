import asyncio


def printMessage():
    print("Get Busy Living or Get Busy Dying")
    
loop = asyncio.get_event_loop()

loop.call_later(1,printMessage)
loop.close()