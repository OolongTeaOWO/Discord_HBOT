from pymongo import MongoClient
from gridfs import GridFS
from io import BytesIO

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members

gridfs_db = GridFS(client["gridfs_database"])

def add_member(memberID, addID, return_type: int):
    print(type(memberID))
    print(type(addID))
    if memberID == addID:
        raise "ID 重複"
    memberID = str(memberID)
    existing_doc = member_db.find_one({memberID: {"$exists": True}})
    
    if existing_doc:
        member_db.update_one({memberID: {"$exists": True}}, {"$addToSet": {memberID: addID}})
    else:
        member_db.insert_one({memberID: [addID]})
    return {
        1: member_db.find_one({memberID: {"$exists": True}}),
        2: "完成"
    }.get(return_type, "未知類型")

def fetch_member(memberID):
    data = member_db.find_one({memberID: {"$exists": True}})
    if data:
        last_list = None
        for key, value in data.items():
            last_list = value

        if last_list:
            return last_list

def fetch_data(memberID):
    file_data = gridfs_db.find_one({'filename': memberID})
    if file_data:
        return BytesIO(file_data.read())
    else:
        return None

def add_file(filename, data):
    existing_file = gridfs_db.find_one({'filename': filename})
    
    if existing_file:
        gridfs_db.delete(existing_file._id)
        
        with gridfs_db.new_file(filename=filename) as file:
            utf8_data = data.encode('utf-8')
            file.write(utf8_data)
            file.close()
        message = f'圖片 {filename} 已更新至數據庫中。'
    else:
        
        with gridfs_db.new_file(filename=filename) as file:
            file.write(data)
            file.close()
        message = f'圖片 {filename} 已成功存入數據庫中。'

    return message