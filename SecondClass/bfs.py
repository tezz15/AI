#Breadth First Search
nodelist = {'A':['B','C'],'B':['A','D','E'],'C':['A','F','G'],'D':['B','H'],'E':['B','K'],'F':['C'],'G':['C'],'H':['D'],'K':['E']}
start_node = input("Enter initial state")
goal_node = input("Enter goal state")

def bfs_search(nodelist,start_node,goal_node):
    explored_node = []
    queue= [start_node]
    # if start_node == goal_node:
    #    print("Solution found")
    while queue:
        node=queue.pop(0)
        if node not in explored_node:
            explored_node.append(node)
            neighbour = nodelist[node]
            for neighbour in neighbour:
                queue.append(neighbour)
    return explored_node
a = bfs_search(nodelist,start_node,goal_node)
print(a)
