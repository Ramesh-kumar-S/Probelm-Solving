import atexit

class Knox:
    def __init__(self) -> None:
        atexit.register(self.exit_handler)
        exit(1)
    
    def hey(self):
        print("Entering Hey")
        print("Exitting Hey")
        # exit(0)
        
    def hello(self):
        print("Entering Hello")
        print("Exitting Hello")
        # exit(1)
        
    def exit_handler(self):
        self.hello()
        print("Exiting program")


ex = Knox()
# ex.hey()
# ex.hello()
    