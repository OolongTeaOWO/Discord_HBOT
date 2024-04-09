from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members
files_db = db.files


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

def add_files(memberID):
    pass