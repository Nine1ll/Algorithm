import sys
from collections import defaultdict

TREE_LENGTH = 100_000 + 1
INF = 1_000_000_000 + 1

leaf = [False] * TREE_LENGTH
visited = [False] * TREE_LENGTH
tree = [0] * TREE_LENGTH
tree_path = defaultdict(list)


def find_max(node):
    # 리프 노드면 본인 값 반환
    if leaf[node]:
        return tree[node]
    # 아니면
    visited[node] = True # 방문 완료
    max_value = -1
    for j in tree_path[node]:
        if visited[j]: #방문했으면 제끼고
            continue
        max_value = max(max_value, find_min(j)) #방문 안했으면 max값 계산

    tree[node] = max_value
    return max_value


def find_min(node):
    if leaf[node]:
        return tree[node]

    visited[node] = True
    min_value = INF
    for j in tree_path[node]:
        if visited[j]:
            continue
        min_value = min(min_value, find_max(j))

    tree[node] = min_value
    return min_value


n, root_number = map(int, sys.stdin.readline().split())
for _ in range(1, n):
    u, vertex = map(int, sys.stdin.readline().split())
    tree_path[u].append(vertex)
    tree_path[vertex].append(u)

leaf_cnt = int(sys.stdin.readline())
for _ in range(leaf_cnt):
    leaf_number, node_value = map(int, sys.stdin.readline().split())
    leaf[leaf_number] = True
    tree[leaf_number] = node_value

find_max(root_number)

target = int(sys.stdin.readline())
for _ in range(target):
    node_number = int(sys.stdin.readline())
    print(tree[node_number])