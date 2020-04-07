from math import sqrt


import networkx as nx

def adj_list_to_matrix(fileName):
    G = nx.read_gml(fileName, 'id')
    mat = nx.to_numpy_matrix(G)
    return mat


def readNet2(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


def dist(x1, y1, x2, y2):
    return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))


def parseFile(fileName):
    n = 51
    tpl = []
    with open(fileName, "r") as f:
        for line in range(n):
            node, x, y = f.readline().split(" ")
            tpl.append((int(node), int(x), int(y)))

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for pct1 in tpl:
        for pct2 in tpl:
            matrix[pct1[0] - 1][pct2[0] - 1] = dist(pct1[1], pct2[1], pct1[2], pct2[2])
            matrix[pct1[0] - 1][pct2[0] - 1] = dist(pct1[1], pct2[1], pct1[2], pct2[2])
    return matrix

def readNet3(fileName):
    f = open(fileName, "r")
    net = {}

    distances = []
    distances = parseFile(fileName)
    net["mat"] = distances
    n = len(distances)
    net["noNodes"] = n
    f.close()
    return net
