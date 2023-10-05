import networkx as nx
import random

class Graph:
    def __init__(self):
        self.G = nx.DiGraph() 
        self.node_status = {}
        # self.source_nodes = random.sample(range(100), 10)
        self.source_nodes = [1, 2]
        self.create_fake_graph()


    def create_fake_graph(self): 
        nodes_info = {
            1: {'g': 0.3},
            2: {'g': 0.3},
            3: {'g': 0.6},
            4: {'g': 0.5},
            5: {'g': 0.2},
            6: {'g': 0.7},
            7: {'g': 0.4},
            8: {'g': 0.3},
            9: {'g': 0.8}
        }
        self.G.add_nodes_from(nodes_info.keys())
        nx.set_node_attributes(self.G, nodes_info)

        # Thêm cạnh và trọng số của cạnh
        edges_info = [
            (1, 5, {'weight': 0.4}),
            (1, 3, {'weight': 0.1}),
            (2, 3, {'weight': 0.5}),
            (2, 4, {'weight': 0.8}),
            (2, 6, {'weight': 0.3}),
            (3, 1, {'weight': 0.2}),
            (3, 2, {'weight': 0.2}),
            (3, 6, {'weight': 0.1}),
            (4, 2, {'weight': 0.5}),
            (5, 1, {'weight': 0.2}),
            (5, 6, {'weight': 0.3}),
            (5, 9, {'weight': 0.3}),
            (6, 2, {'weight': 0.3}),
            (6, 3, {'weight': 0.2}),
            (6, 5, {'weight': 0.2}),
            (6, 7, {'weight': 0.1}),
            (7, 6, {'weight': 0.3}),
            (7, 8, {'weight': 0.1}),
            (8, 7, {'weight': 0.2}),
            (9, 5, {'weight': 0.3})
        ]
        self.G.add_edges_from(edges_info)

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

    def initialize_node_statuses(self, source_nodes):
        activate_nodes = []
        inactivate_nodes = []
        
        for node in self.G.nodes():
            if node in source_nodes:
                self.node_status[node] = 'activate'
                activate_nodes.append(node)
            else:
                self.node_status[node] = 'inactivate'
                inactivate_nodes.append(node)

        return activate_nodes, inactivate_nodes
    
    def spread_information(self):
        # activate_nodes = [node for node in self.G.nodes() if self.node_status[node] == 'activate']
        # inactivate_nodes = [node for node in self.G.nodes() if self.node_status[node] == 'inactivate']
        activate_nodes, inactivate_nodes = self.initialize_node_statuses(self.source_nodes)
        print(f'activate_nodes: {activate_nodes}')
        print(f'inactivate_nodes: {inactivate_nodes}')
        count = 0
        t = 0
        while inactivate_nodes:
            t+=1
            print(f't = {t}')
            activated_nodes = []
            # node = random.choice(inactivate_nodes)
            for node in inactivate_nodes:
                activation_threshold = self.G.nodes[node]['g']
                in_neighbors = list(self.G.predecessors(node))
                activation_sum = sum(self.G[u][node]['weight'] for u in in_neighbors if u in activate_nodes)

                if activation_sum >= activation_threshold:
                    activated_nodes.append(node)
                    count += 1
                    print(f'activate node: {node}')
                    self.node_status[node] = 'activate'
                    activate_nodes.append(node)
                    inactivate_nodes.remove(node)
                # else:
                    # print(f'Node {node} is not activated!')

            if not activated_nodes:
                break

            # for node in activated_nodes:
            #     self.node_status[node] = 'activate'
            #     activate_nodes.append(node)
            #     inactivate_nodes.remove(node)
        print(f'activate_nodes: {activate_nodes}')
        print(f'inactivate_nodes: {inactivate_nodes}')
        return count
    
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
# graph_obj.load_graph_from_file(file_path)
# graph_obj.assign_thresholds_and_weights()
# graph = graph_obj.get_graph()
# graph_obj.print_graph_info()
d = graph_obj.spread_information()
print(d)