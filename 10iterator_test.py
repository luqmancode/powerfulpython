class DictIterator:
    def __init__(self, dict_values):
        self.dict_set = dict_values

    def __iter__(self):
        return iter(self.dict_set)

    def __setitem__(self, key, value):
        self.dict_set[key] = value

    def __getitem__(self, key):
        return self.dict_set[key]

diter = DictIterator({1:"a", 2:"b"})
for key in diter:
    print(key)

# diter.add(3, "c") AttributeError without __setitem__ but had __add__(self, key, value)
diter[3] = "c"
for key in diter: # has no attribute on keys, values, items()
    print(key, diter[key])

# print(diter[3]) TypeError without __getitem__
print(diter[3])

