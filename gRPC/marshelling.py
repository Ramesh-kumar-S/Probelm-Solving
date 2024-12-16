from datetime import datetime
import test_pb2 as pb
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
import logging

print(pb.taskStatus.Name(pb.IN_PROGRESS))

timeTaken = pb.duration(
    startTime="13:00",
    endTime="17:00",
)

request = pb.InitTask(
    taskId=1000,
    taskName="gRPC Exploration",
    ETA="30-10-2024",
    status=pb.COMPLETED,
    priority="P1",
    duration=timeTaken
    # duration=pb.duration(
    #                 startTime="13:00",
    #                 endTime="17:00"
    #             )
)

time = datetime(2024, 10, 30, 19, 15, 40)
request.time.FromDatetime(time)

time2 = request.time.ToDatetime()
print(request)

print(f'Un-marshaled  Date : {time2}')
# print(f'Start time : {request.duration.startTime}') #Print the Attribute from Nested Message type

# region Marshal
data = request.SerializeToString()
print(len(data))
print(type(data))
# End


# region UnMarshal
request2 = pb.InitTask()
request2.ParseFromString(data)
print(request2)
# End

#Get current timestamp
from google.protobuf.timestamp_pb2 import Timestamp
now = Timestamp()
now.GetCurrentTime()
print(now)

#Json Encoding
from google.protobuf.json_format import MessageToJson
JsonData = MessageToJson(request)
print(f'JSON Formatted Data : {JsonData}')
print(f'Size of JSON Data : {len(JsonData)}')
print(f'Size of ProtoBuf Data : {len(request.SerializeToString())}')
