from priority_queue.priority_queue import PriorityQueue


def dijkstra_prunning(graph, weight, source, target):
    d = {}
    B = float('inf')
    pq = PriorityQueue()
    pq.insert(source, 0)  # TODO: create this method in PriorityQueue
    d[source] = 0

    while not pq.empty():  # TODO: create this method in PriorityQueue
        u = pq.remove_min()  # TODO: create this method in PriorityQueue
        if u == target:
            break
        for v in graph[u]:
            tent = d[u] + weight(u, v)
            if tent > B:
                continue
            if v == target:
                B = min(tent, B)
            relax(v, tent)

    return d[target]


def relax(v, tent):
    if d[v] > tent:
        if d[v] == float('inf'):
            pq.insert(v, tent)
        else:
            pq.decrease_key(v, tent)  # TODO: create this method in PriorityQueue
        d[v] = tent


def dijkstra_prediction(graph, weight, source, target, i0, alpha):
    d = {}
    B = float('inf')
    P = float('inf')
    X = []
    i = 0
    pq = PriorityQueue()
    pq.insert(source, 0)  # TODO: create this method in PriorityQueue
    d[source] = 0
    R = set()

    while not pq.empty() and pq.min_prio() <= P:  # TODO: create this methods in PriorityQueue
        u = pq.remove_min()  # TODO: create this method in PriorityQueue
        if u == target:
            break
        i += 1
        if i <= i0:
            X[i] = (d[u], B)
        if i == i0:
            P = alpha * prediction(X)
        for v in graph[u]:
            tent = d[u] + weight(u, v)
            if tent > min(B, P):
                continue
            if v == target:
                B = min(B, tent)
            relax_smart(v, tent, P)
        smart_restart(P, R)

    return d[target]


def smart_restart(P, R):
    P = beta * P
    for v in R:
        if d[v] <= min(B, P):
            R.remove(v)
            pq.insert(v, d[v])  # TODO: create this method in PriorityQueue


def relax_smart(v, tent, P):
    if d[v] > tent:
        if d[v] == float('inf'):
            if tent <= P:
                pq.insert(v, tent)  # TODO: create this method in PriorityQueue
            else:
                R.add(v)
        else:
            if tent not in R:
                pq.decrease_prio(v, tent)  # TODO: create this method in PriorityQueue
            else:
                if tent <= P:
                    return
                R.remove(v)
                pq.insert(v, tent)  # TODO: create this method in PriorityQueue
        d[v] = tent
