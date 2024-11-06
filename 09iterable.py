class UniqueList:
    def __init__(self, items):
        self.items = []
        for item in items:
            self.append(item)

    def append(self, value):
        if value not in self.items:
            self.items.append(value)

    def __getitem__(self, key):
        return self.items[key]

    def __len__(self):
        return len(self.items)


ul = UniqueList([1,2,3,4,4])
print(ul.items)
ul.append(4)
ul.append(5)
print(ul[3])
print(len(ul))
