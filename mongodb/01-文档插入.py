import pymongo
from pymongo import MongoClient

# 创建连接
client = MongoClient('localhost', 27017)

# 获取一个数据库， 没有就新建
db = client['test-database']    

# 插入一条数据
db.jack.insert_one({'name':'jack', 'age':22, 'desc':'美男子'})

# 修改一条数据
db.jack.update_one({'name':'jack'},{'$set': {'name': 'Marry'}}, True)

# 修改多条数据
db.jack.update_many({'name':'jack'}, {'$set': {'name': 'Hello'}}, True)

# 删除docucment
db.jack.delete_many({'name': 'jack'})

# 删除collection
db.jack.drop()

print(db.jack.find_one_and_delete({'name': 'Marry'}))