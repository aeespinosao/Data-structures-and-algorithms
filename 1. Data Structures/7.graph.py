class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        
    def add_vertex(self, vertex) -> bool:
        if self.adj_list.get(vertex) == None:
            self.adj_list[vertex] = []
            return True
    
        return False
    
    def add_edge(self, v1, v2) -> bool:
        if self.adj_list.get(v1) != None and self.adj_list.get(v2) != None:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        
        return False
    
    def remove_edge(self, v1, v2) -> bool:
        if self.adj_list.get(v1) and self.adj_list.get(v2):
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        
        return False
    
    def remove_vertex(self, vertex):
        if self.adj_list.get(vertex):
            for other_vertex in self.adj_list.get(vertex):
                try:
                    self.adj_list[other_vertex].remove(vertex)
                except ValueError:
                    pass
            del self.adj_list[vertex]
            return True
        
        return False