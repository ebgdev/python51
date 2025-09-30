class Graph:
    def __init__(self):
        self.adj_list = {}


    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        all_keys = self.adj_list.keys()
        if v1 not in all_keys and v2 not in all_keys:
            print('Not valid vertecies to connect')
            return False
        else:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True

    def remove_edge(self,v1,v2):
        all_keys = self.adj_list.keys()
        if v1 in all_keys and v2 in all_keys:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self,vertex):
        all_keys = self.adj_list.keys()
        if vertex in all_keys:
            for other_vertex in self.adj_list[vertex]: # B,E
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False 


    def print_graph(self):
        for vertex, edge in self.adj_list.items():
            print(vertex,':',edge)


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

graph.add_edge('A','B')
graph.add_edge('B','C')
graph.add_edge('A','C')
graph.remove_edge('A','B')

graph.print_graph()