class Graph:
    def __init__(self, dict_graph):
        self.dict_graph = dict_graph
        self.vertices = set()
        for key in self.dict_graph:
            self.vertices.add(key[0])
            self.vertices.add(key[1])
        self.edges = set()
        for key in self.dict_graph:
            self.edges.add(key)

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.dict_graph.keys()

    def get_weight(self, vertex_a, vertex_b):
        try:
            return self.dict_graph[(vertex_a, vertex_b)]
        except KeyError:
            return "edge not found"

    def get_weights(self):
        return self.dict_graph.values()
