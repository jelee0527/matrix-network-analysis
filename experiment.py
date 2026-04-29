import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# 1. 데이터 정의
# =========================
labels = ['A', 'B', 'C', 'D']

A = np.array([
    [0,   0.9, 0.3, 0],
    [0.2, 0,   0.5, 0.4],
    [0,   0.1, 0,   0.8],
    [0.6, 0,   0.2, 0]
])

# =========================
# 2. 행렬곱 계산
# =========================
A2 = np.linalg.matrix_power(A, 2)
A3 = np.linalg.matrix_power(A, 3)

print("A^2:\n", A2)
print("A^3:\n", A3)

# =========================
# 3. 평균 영향력 분석
# =========================
avg_values = [
    np.mean(A),
    np.mean(A2),
    np.mean(A3)
]

steps = ['1-step', '2-step', '3-step']

plt.figure()
plt.plot(steps, avg_values, marker='o')
plt.title("Multi-step Influence Propagation")
plt.xlabel("Step")
plt.ylabel("Average Influence")
plt.grid()
plt.savefig("influence_graph.png")

# =========================
# 4. 네트워크 그래프 생성
# =========================
G = nx.DiGraph()

for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] > 0:
            G.add_edge(labels[i], labels[j], weight=A[i][j])

pos = nx.spring_layout(G, seed=42)

plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Weighted Network Graph (Enhanced)")
plt.savefig("network_graph.png")

print("완료: 그래프 생성됨")