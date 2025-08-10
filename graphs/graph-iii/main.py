'''
Directed, cyclic, dictionary graph representation
The keys leads to nodes
'''

graph = { 
    'a': ['c'], 
    'b': ['d'], 
    'c': ['e'], 
    'd': ['a', 'd'], 
    'e': ['b', 'c'] 
} 

def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 

def find_all_paths(graph, start, end, path =[]): 
    path = path + [start] 
    if start == end: 
        return [path] 
    paths = [] 
    for node in graph[start]: 
        if node not in path: 
            newpaths = find_all_paths(graph, node, end, path) 
        for newpath in newpaths: 
            paths.append(newpath) 
    return paths 

def find_shortest_path(graph, start, end, path =[]): 
		path = path + [start] 
		if start == end: 
			return path 
		shortest = None
		for node in graph[start]: 
			if node not in path: 
				newpath = find_shortest_path(graph, node, end, path) 
				if newpath: 
					if not shortest or len(newpath) < len(shortest): 
						shortest = newpath 
		return shortest 

print(find_path(graph, 'd', 'c')) 
print(find_all_paths(graph, 'd', 'c')) 
print(find_shortest_path(graph, 'd', 'c')) 