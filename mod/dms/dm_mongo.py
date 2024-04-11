from pymongo import MongoClient
from gridfs import GridFS

import base64

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members

gridfs_db = GridFS(client["gridfs_database"])

def add_member(memberID, addID, return_type: int):
    if memberID == int(addID):
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
    return member_db.find_one({memberID: {"$exists": True}})

def add_file(filename, data):
    
    if gridfs_db.exists({"filename": filename}):
        raise "相同文件名已存在於數據庫中。"
    
    with gridfs_db.new_file(filename=filename) as file:
        file.write(data)
        
    return "圖片已成功存入數據庫中。"