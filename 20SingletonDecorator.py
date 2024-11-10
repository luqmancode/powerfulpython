def SingletonDecorator(klass):
    instances = {}
    def get_instance():
        if klass not in instances:
            instances[klass] = klass()
        return instances[klass]
    return get_instance
    

# @SingletonDecorator # id instances will be same
class MYDB:
    pass

db1 = MYDB()
db2 = MYDB()
print(id(db1), id(db2)) # 133538007021376 133538007021232 different but same on decorator applied
