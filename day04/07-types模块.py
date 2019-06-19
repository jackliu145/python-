import types

print(types.__name__)
print(type(abs) == types.BuiltinFunctionType)
print(type(int) == types.BuiltinMethodType)  #False

print(types.BuiltinMethodType)
print(dir(types))
print(dir('abc'))