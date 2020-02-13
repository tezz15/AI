#DEPTH FIRST SEARCH
nodelist = {'A':['B','C'],'B':['A','D','E'],'C':['A','F','G'],'D':['B','H'],'E':['B','K'],'F':['C'],'G':['C'],'H':['D'],'K':['E']}
start_node = input("Enter initial state")
goal_node = input("Enter goal state")

def dfs_search(nodelist,start_node,goal_node):
    explored_node = []
    queue = [[start_node]]
    if start_node == goal_node:
        print("Solution found")
    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node not in explored_node:
            neighbours = nodelist[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal_node:
                    return new_path
            explored_node.append(node)
    return "Solution doesnot exist."
A= dfs_search(nodelist,start_node,goal_node)
print(A)