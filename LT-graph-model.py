import networkx as nx
import random

class Graph:
    def __init__(self):
        self.G = nx.DiGraph() 

    def load_graph_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        n = int(lines[0].split()[2])
        m = int(lines[1].split()[2])

        self.G.add_nodes_from(range(n))
        for line in lines[3:]:
            u, v = map(int, line.split())
            self.G.add_edge(u, v)

    def assign_thresholds_and_weights(self):
        for node in self.G.nodes():
            self.G.nodes[node]['g'] = random.uniform(0, 1) 
        for edge in self.G.edges():
            u, v = edge
            weight = 1 / self.G.in_degree(v) 
            self.G[u][v]['weight'] = weight

    def get_graph(self):
        return self.G
    
    def print_graph_info(self):
        print("Thông tin đồ thị:")
        print(f"Số đỉnh: {len(self.G.nodes())}")
        print(f"Số cạnh: {len(self.G.edges())}")
        
        print("\nThông tin về đỉnh và ngưỡng:")
        for node in self.G.nodes():
            print(f"Đỉnh {node}: Ngưỡng g = {self.G.nodes[node]['g']}")

        print("\nThông tin về cạnh và trọng số:")
        count = 0
        for u, v, data in self.G.edges(data=True):
            count += 1
            weight = data['weight']
            print(f"Cạnh ({u}, {v}): Trọng số w = {weight}")
        print(count)
file_path = 'test.txt'
graph_obj = Graph()
graph_obj.load_graph_from_file(file_path)
graph_obj.assign_thresholds_and_weights()
# graph = graph_obj.get_graph()
graph_obj.print_graph_info()