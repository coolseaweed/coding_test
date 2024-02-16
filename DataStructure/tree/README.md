# Tree

## Graph vs Tree

||Graph|Tree|
|:---:|:---|:---|
|Definition|Node와 그 Node를 연결하는 Edge을 하나로 모아 놓은 자료 구조|그래프의 한종류로 방향성이 있는 비순환 그래프 (Directed Acyclic Graph a.k.a DAG)의 한 종류|
|Direction|Directed, Undirected 모두 존재|Directed Graph|
|Cycle|Cycle (o), self-loop (o), A/Cyclic graph|Cycle (x), self-loop (x), Acyclic Graph|
|Root node|Root node 개념이 없음|한 개의 Root node만이 존재, 모든 children node는 한 개의 parent node 만을 가짐|
|Parent-Children|parent-children 개념이 없음|parent-children 관계 존재, top-bottom 또는 bottom-top으로 이루어짐|
|Model|네트워크모델|계층모델|
|Traversal|DFS,BFS|DFS, BFS안의 Pre-, In-, Post-order|
|Edge #|Graph에 따라 Edge의 수가 다름, Edge가 없을 수도 있음|node의 갯수가 `N`인 Tree는 항상 `N-1`의 Edge를 가짐|
|Path|-|임의의 두 Node 간의 경로는 유일|
|Examples|지도, 지하철 노선도의 최단 경로, 전기 회로의 소자들, 도로, 선수 과목|이진트리, 이진 탐색 트리, 균형 트리(AVL 트리, Red-Black 트리), 이진 힙(Max 힙, Min 힙) 등| 