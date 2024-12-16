from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
import grpc
import test_pb2 as pb
import test_pb2_grpc as rpc
import random
import log

def new_task_id():
    return random.randrange(1, 101)

class Tasks(rpc.TasksServicer):
    def add(self, request, context):
        log.info(f"task {request}")
        
        task_id = new_task_id()
        return 
print(help(Tasks))