import pickle

d = {'name':'jack', 'age':10}

r = pickle.dumps(d)

print(r)

d1 = pickle.loads(r)
print(d1)