from pymongo import MongoClient


MONGODB_URI = "mongodb+srv://ramesh2:ramesh@cluster0.go7fnt6.mongodb.net/"
client = MongoClient(MONGODB_URI)
print(client['admin'])
for db_name in client.list_database_names():
    print(db_name)
client.close()

