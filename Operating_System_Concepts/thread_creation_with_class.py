import threading
import time
import os


class SoftwareEngineer(threading.Thread):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        print("Ramesh is a Software Engineer @ NetApp")
        time.sleep(2)
        print("Ramesh is an Member of Technical Staff - 3 @ Nutanix")


if __name__ == "__main__":
    print("Instantiating the Class")
    S = SoftwareEngineer()

    print("Software Engineering is gonna start up")
    S.start()
    print(f"Status : {S.is_alive()}")

    print("Main thread")
    time.sleep(1)
    print(f"Status : {S.is_alive()}")

    print("Distraction can wait, Until I became an Disciplined Software Engineer")
    S.join()
    print(f"Status : {S.is_alive()}")
