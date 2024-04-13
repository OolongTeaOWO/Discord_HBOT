from pymongo import MongoClient
from gridfs import GridFS

import base64

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members

gridfs_db = GridFS(client["gridfs_database"])

def add_member(memberID, addID, return_type: int):
    if memberID == str(addID):
        raise "ID 重複"
    memberNAME = str(memberID)
    existing_doc = member_db.find_one({memberID: {"$exists": True}})
    
    if existing_doc:
        member_db.update_one({memberID: {"$exists": True}}, {"$addToSet": {memberID: addID}})
    else:
        member_db.insert_one({memberID: [addID]})
    return {
        1: member_db.find_one({memberID: {"$exists": True}}),
        2: "完成"
    }.get(return_type, "未知類型")

def fetch_member(memberNAME):
    data = member_db.find_one({memberNAME: {"$exists": True}})
    if data:
        last_list = None
        for key, value in data.items():
            last_list = value

        if last_list:
            return last_list

def add_file(filename, data, code):
    binary_data = base64.b64decode(data)
    
    with gridfs_db.new_file(code=code,filename=filename) as file:
        file.write(binary_data)
    return "圖片已成功存入數據庫中。"

def fetch_data(Code):
    data = gridfs_db.find_one({Code: {"$exists": True}})
    if data:
        return "有檔案"
    else:
        return "沒檔案"