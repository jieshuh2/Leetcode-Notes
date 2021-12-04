def build(pairs, node1, node2):
    #build tree
    childToParent = {}
    parentToChild = {}
    for parent, child in pairs:
        if child not in childToParent:
            childToParent[child] = set()
        childToParent[child].add(parent)
        if parent not in parentToChild:
            parentToChild[parent] = set()
        parentToChild[parent].add(parent)
    visited = set()
    def findAllParent(node, ancestor):
        if node in visited:
            return
        visited.add(node)
        ancestor.add(node)
        for parent in childToParent[node]:
            findAllParent(parent, ancestor)
    def earlistAncestor(node):
        maxdist = [0]
        earlynode = [-1]
        # queue = []
        # queue.add((0, node))
        # while len(queue) != 0:
        #     dist, n = queue.pop(0)
        #     if n in visited:
        #             continue
        #     visited.add(n)
        #     if dist > maxdist:
        #         maxdist = dist
        #         earlynode =  n
        #     if n not in childToParent:
        #         continue
        #     for parent in childToParent[n]:
        #         queue.append((dist + 1, parent))
        visited = set()
        def dfs(node, dist):
            if node in visited:
                return
            visited.add(node)
            if dist > maxdist[0]:
                maxdist[0] = dist
                earlynode[0] = node
            if node in childToParent:
                for n in childToParent[node]:
                    dfs(node, dist + 1)
        if maxdist[0] > 0:
            return node[0]
            

