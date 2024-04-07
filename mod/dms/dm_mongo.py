from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members

class mongo_dm():
    def __init__(self, memberID, addID,return_type:int):
        self.addID = addID
        self.memberID = memberID
        self.type = return_type

    def add_member(self):
        if self.memberID == self.addID:
            return "Id duplication"
        existing_doc = member_db.find_one({self.memberID: {"$exists": True}})
        
        if existing_doc:
            member_db.update_one({self.memberID: {"$exists": True}}, {"$addToSet": {self.memberID: self.addID}})
        else:
            member_db.insert_one({self.memberID: [self.addID]})
        return {
            1: member_db.find_one({self.memberID: {"$exists": True}}),
            2: "done"
        }.get(self.type, "unknown type")
    
    def fetch_member(self):
        pass
