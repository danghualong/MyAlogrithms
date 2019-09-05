
class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict,self).__init__(*args, **kwargs)
        self.__dict__ = self

    @staticmethod
    def toDotDict(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, dict):
                    data[k] = DotDict(v)
                    DotDict.toDotDict(data[k])
        else:
            return data
        return DotDict(data)

if __name__=="__main__":
    a={'name':'李梦','age':40,'friend':{'name':'孟达'}}
    b=DotDict.toDotDict(a)
    print(b.name)
    print(b.friend.name)