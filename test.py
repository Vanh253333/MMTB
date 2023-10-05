import networkx as nx
import random

n = 100  
m = 350

G = nx.DiGraph()
G.add_nodes_from(range(n))

for _ in range(m):
    u, v = random.sample(range(n), 2)  
    G.add_edge(u, v)

Nin = {}
Nout = {}
for v in G.nodes():
    Nin[v] = list(G.predecessors(v))  
    Nout[v] = list(G.successors(v)) 


def save_graph_info_to_txt(graph, file_path):
    n = len(graph.nodes())  # Số đỉnh
    m = len(graph.edges())  # Số cạnh

    # Lưu thông tin số đỉnh và số cạnh vào tệp tin
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Số đỉnh: {n}\n")
        file.write(f"Số cạnh: {m}\n")
        file.write("Danh sách cạnh:\n")

        # Lưu danh sách các cạnh vào tệp tin
        for edge in graph.edges():
            u, v = edge
            file.write(f"{u} {v}\n")

save_graph_info_to_txt(G, "test.txt")

# In kết quả
print("Danh sách các đỉnh:")
print(G.nodes())
print("\nDanh sách các cạnh:")
print(G.edges())
print("\nTập đỉnh láng giềng vào (Nin):")
print(Nin)
print("\nTập đỉnh láng giềng ra (Nout):")
print(Nout)
