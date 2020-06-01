
from collections import defaultdict 
  

#  Check connectivity using DFS

class Graph: 
  
    def __init__(self): 
        self.adList = defaultdict(list)
        self.vertex=[]
        self.visited=[None]*1000
        self.length=0

    def add_vertex(self,u):
        if u in self.vertex:
            return True
        self.vertex.append(u)
        self.visited[u]=False
        self.length = self.length+1

    def delete_vertex(self,u):
        self.vertex.remove(u)
        for i in self.adList:
            if u in self.adList[i]:
                self.adList[i].remove(u)
        del self.adList[u]
        # return "Vertex ("+str(u)  + ") successfully deleted."

    def add_edge(self,u,v):
        if v in self.adList[u] and u in self.adList[v]:
            # return "Edge ("+str(u) +","+ str(v) + ") already there."
            return 
        self.adList[u].append(v)
        self.adList[v].append(u)
        # return "Edge ("+str(u) +","+ str(v) + ") successfully added."

    def delete_edge(self,u,v):
        if v in self.adList[u]:
            self.adList[u].remove(v)
            self.adList[v].remove(u)
            # return "Edge ("+str(u) +","+ str(v) + ") successfully deleted."
        else:
            # return "Edge ("+str(u) +","+ str(v) + ") isn't a direct edge or may be already deleted."
            pass



    def dfs(self,v):
        # print(self.visited)
        self.visited[v]=True
        # print(v)

        for u in self.adList[v]:
            # print(u)
            if self.visited[u] == False:
                self.dfs(u)


    def is_connected(self,u,v):
        # print(self.length)
        # self.visited=[False]*(self.length)
        if v in self.adList[u]:
            # return "Edge, ("+str(u) +","+ str(v) + ") connected"
            return 
        self.visited=[False]*1000
        self.dfs(u)
        # print(self.visited)
        # for i in ((self.adList)):
        #     # print("yes")
        #     if self.visited[i] == False:
        #         # print("yeahhhh...")
        #         return False
        # return True
        if self.visited[v] == True:
            # return "Edge, ("+str(u) +","+ str(v) + ") connected" 
            return True
        else:
            # return "Edge, ("+str(u) +","+ str(v) + ") not connected" 
            return False



# Driver code 
# g = Graph()
# g.add_vertex(2)
# g.add_vertex(25)
# g.add_vertex(100)
# g.add_vertex(900)
# g.add_vertex(889)
# g.add_vertex(111)
# g.add_vertex(1)
# g.add_vertex(15)
# g.add_vertex(99)
# g.add_edge(2,25)
# g.add_edge(889,15)
# g.add_edge(111,15)
# g.add_edge(100,111)
# g.add_edge(100,25)
# g.add_edge(2,900)
# g.add_edge(889,25)
# g.add_edge(1,2)
# g.add_edge(1,99)

# print(g.is_connected(99,15))
# print(g.delete_edge(2,25))
# # print(g.delete_edge(2,25))
# print(g.is_connected(99,15))
# print(g.add_edge(2,25))
# print(g.is_connected(99,15))
# print(g.delete_edge(889,25))
# print(g.delete_edge(100,111))
# print(g.is_connected(99,15))
# print(g.delete_vertex(25))
# print(g.is_connected(100,25))
# print(g.is_connected(99,100))
# print(g.add_edge(889,100))
# print(g.is_connected(99,15))
# g.add_vertex(112)
# print(g.add_edge(111,112))
# print(g.is_connected(1,112))
# print(g.adList)
# print(g.vertex)


