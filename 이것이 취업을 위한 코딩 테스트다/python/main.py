# DFS 구현 예제

def dfs(graph, v, isVisit):
  isVisit[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not isVisit[i]:
      dfs(graph, i, isVisit)

graph = [
  [], 
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [1, 7],
]

isVisit = [False] * 9

dfs(graph, 1, isVisit)

