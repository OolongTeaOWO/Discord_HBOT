from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
member_db = db.members

# 要新增的資料
new_data = ["1173583289890648155", "541668345748991286"]

# 檢查該資料集是否已存在
existing_doc = member_db.find_one({"503043347246743567": {"$exists": True}})

if existing_doc:
    # 如果資料集已存在，將新資料添加到現有的資料集中
    member_db.update_one({"503043347246743567": {"$exists": True}}, {"$addToSet": {"503043347246743567": {"$each": new_data}}})
else:
    # 如果資料集不存在，則插入新的資料集
    member_db.insert_one({"503043347246743567": new_data})

# 打印更新後的結果
print(member_db.find_one({"503043347246743567": {"$exists": True}}))
