
# Prim's Algorithm

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix (0 for no edge):")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True

edges = 0
total_cost = 0

print("\nEdges in Minimum Spanning Tree:")

while edges < n - 1:
    minimum = float('inf')
    x = -1
    y = -1

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    if x == -1:
        print("Graph is disconnected. MST is not possible.")
        break

    print(x + 1, "-", y + 1, ":", minimum)
    total_cost += minimum
    selected[y] = True
    edges += 1

if edges == n - 1:
    print("Total cost of MST:", total_cost)
print("\nEN.No:92460118606")