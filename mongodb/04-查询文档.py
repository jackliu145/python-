from pymongo import MongoClient
from datetime import datetime
from collections.abc import Iterable
client = MongoClient()

# 获取数据库，切换数据库，如果数据库不存在，则创建数据库
db = client.test

# 插入一批
# db.inventory.insert_many([
#     {"item": "journal",
#      "qty": 25,
#      "size": {"h": 14, "w": 21, "uom": "cm"},
#      "status": "A"},
#     {"item": "notebook",
#      "qty": 50,
#      "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "status": "A"},
#     {"item": "paper",
#      "qty": 100,
#      "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "status": "D"},
#     {"item": "planner",
#      "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"},
#      "status": "D"},
#     {"item": "postcard",
#      "qty": 45,
#      "size": {"h": 10, "w": 15.25, "uom": "cm"},
#      "status": "A"}])

#  查看单个document
doc = db.inventory.find_one()

# 查找所有的document
docs = db.inventory.find()
# print(isinstance(docs, Iterable))
# for doc in docs:
#     print(doc)

# 按相等条件查找
doc_d = db.inventory.find({"title": "jack"})
# print(list(doc_d))

# 模糊插叙
doc_status_in = db.inventory.find({"status": {"$in": ["A", "D"]}})
# print(list(doc_status_in))

# 多个条件查询
doc_status_a_qty_lt_30 = db.inventory.find({'status':'A', "qty": {"$lt": 30}})
# print(list(doc_status_a_qty_lt_30))

# like模糊查询 SELECT * FROM inventory WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")
result = db.inventory.find({
    "status": "A", 
    "$or": [
        {"qty": {"$lt": 30},},
        {"item": {"$regex": '^p'}}
    ]
})
print(list(result))
