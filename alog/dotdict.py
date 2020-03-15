# 将dict转化为对象的类
class DictWrapper(dict):
    def __init__(self, *args, **kwargs):
        super(DictWrapper,self).__init__(*args, **kwargs)
        self.__dict__ = self

    @staticmethod
    def to_object(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, dict):
                    data[k]=DictWrapper.to_object(v)
            return DictWrapper(data)
        else:
            return data

    
if __name__=="__main__":
    a={'name':'李梦','age':40,'friend':{'name':'孟达'}}
    b=DictWrapper.to_object(a)
    print(DictWrapper.__dict__)
    print(b.__dict__)
    print(b.name)
    print(b.friend.name)
