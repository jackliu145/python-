from pymongo import MongoClient
from datetime import datetime
client = MongoClient()

# 获取数据库，切换数据库，如果数据库不存在，则创建数据库
db = client.test

# 插入一条记录到指定的集合中
db.inventory.insert_one(
    {"item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})

# 插入多条文档到指定的集合中

db.inventory.insert_many([{
    'title':'jack',
    'name':'hello'
}, {
    'fdf':'fdf',
    'time': datetime.utcnow(),
}])

# Additional Methods for Inserts¶
# The following methods can also add new documents to a collection:

# db.collection.update() when used with the upsert: true option.
# db.collection.updateOne() when used with the upsert: true option.
# db.collection.updateMany() when used with the upsert: true option.
# db.collection.findAndModify() when used with the upsert: true option.
# db.collection.findOneAndUpdate() when used with the upsert: true option.
# db.collection.findOneAndReplace() when used with the upsert: true option.
# db.collection.save().
# db.collection.bulkWrite().
# See the individual reference pages for the methods for more information 