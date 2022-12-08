from priority_queue.priority_queue import PriorityQueue


def dijkstra_pruning(graph, source, targets):
    d = {v: float('inf') for v in graph.get_vertices()}
    d[source] = 0
    B = float('inf')
    pq = PriorityQueue()
    pq.insert(source, d[source])

    while not pq.empty():
        u = pq.remove_min()
        if u in targets:
            break
        for (u, v) in graph.get_edges():
            tent = d[u] + graph.get_weight(u, v)
            if tent > B:
                continue
            if v in targets:
                B = min(B, tent)
            relax(d, v, tent, pq)

    return d


def relax(d, v, tent, pq):
    if d[v] > tent:
        if d[v] == float('inf'):
            pq.insert(v, tent)
        else:
            pq.decrease_prio(v, tent)
        d[v] = tent


def dijkstra_prediction(graph, source, targets, i0, alpha, beta):
    d = {v: float('inf') for v in graph.get_vertices()}
    d[source] = 0
    B = float('inf')
    P = float('inf')
    X = []
    i = 0
    pq = PriorityQueue()
    pq.insert(source, d[source])
    R = set()

    while not pq.empty() and pq.min_prio() <= P:
        u = pq.remove_min()
        if u in targets:
            break
        i += 1
        if i <= i0:
            X.append(d[u])
        if i == i0:
            P = alpha * prediction(X)
        for (u, v) in graph.get_edges():
            tent = d[u] + graph.get_weight(u, v)
            if tent > min(B, P):
                continue
            if v in targets:
                B = min(B, tent)
            relax_smart(v, tent, P, d, R, pq)
        smart_restart(P, R, beta, d, B, pq)

    return d


def smart_restart(P, R, beta, d, B, pq):
    P = beta * P
    for v in R:
        if d[v] <= min(B, P):
            R.remove(v)
            pq.insert(v, d[v])


def relax_smart(v, tent, P, d, R, pq):
    if d[v] > tent:
        if d[v] == float('inf'):
            if tent <= P:
                pq.insert(v, tent)
            else:
                R.add(v)
        else:
            if tent not in R:
                pq.decrease_prio(v, tent)
            else:
                if tent <= P:
                    return
                R.remove(v)
                pq.insert(v, tent)
        d[v] = tent


def prediction(X):
    return sum(X) / len(X)
