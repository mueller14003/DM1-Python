graph = [[1,2,3,4,5,6,7,8,9,10,11],[[1,2],[1,9],[1,10],[1,11],[2,3],[2,4],[2,5],[2,9],[2,10],[2,11],[3,4],[3,10],[3,11],[4,5],[4,10],[4,11],[5,6],[5,7],[5,9],[6,7],[6,9],[7,8],[7,9],[8,10],[8,9],[9,10],[10,11]]]
make_dict = lambda l: {i:[j[1] if j[0] == i else 0 or j[0] if j[1] == i else 0 for j in l[1]] for i in l[0]}
make_matrix = lambda d: [[1 if i in d[j] else 0 for i in d.keys()] for j in d.keys()]
[print(x) for x in make_matrix(make_dict(graph))]