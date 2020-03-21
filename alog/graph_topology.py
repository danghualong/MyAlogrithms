# 有向无环图的拓扑排序

class DAG(object):
    def __init__(self,vs,edges):
        self.vs=vs.copy()
        self.edges=edges
    
    def has_precursor(self,v):
        for edge in self.edges:
          if(not edge['removed'] and edge['to']==v['name']):
              return True
        return False 

    def remove_vertex(self,nodeName):
        for v in self.vs:
            if(nodeName==v['name']):
                self.vs.remove(v)
                break
    
    def toggle_edge_state(self,nodeName,state):
        for edge in self.edges:
            if(edge['from']==nodeName):
                edge['removed']=state

    def create_topoloy(self,items):
        for v in self.vs:
            if(not (v['removed'] or self.has_precursor(v))):
                nodeName=v['name']
                items.append(nodeName)
                v['removed']=True
                self.toggle_edge_state(nodeName,True)
                self.create_topoloy(items)
                if(len(items)==len(self.vs)):
                    print(items)
                # 回溯
                v['removed']=False
                items.pop()
                self.toggle_edge_state(nodeName,False)


vs=[{'name':'a','removed':False},{'name':'b','removed':False},{'name':'c','removed':False}
,{'name':'d','removed':False},{'name':'e','removed':False}]
edges=[{'from':'a','to':'b','removed':False},{'from':'a','to':'c','removed':False},
{'from':'b','to':'d','removed':False},{'from':'e','to':'d','removed':False}]
obj=DAG(vs,edges)
obj.create_topoloy([])
print(obj.vs)
print(obj.edges)


        


    
            

