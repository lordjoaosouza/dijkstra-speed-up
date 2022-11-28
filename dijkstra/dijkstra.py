from priority_queue.priority_queue import PriorityQueue


# DIJKSTRA_PRUNNING
# Tem o mesmo funcionamento do Dijkstra, porém rastreia um limite superior 'B' na distancia de caminho mais
# curto para um nó em T. B tende a infinito e vai diminuindo esse limite toda vez que um caminho mais curto
# para um nó em T encontrado.

def dijkstra_prunning(graph, source, targets):
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

    return d  # Exemplo: {1: 5, 2: 3, 3: 2} -> 1 até o source é 5, 2 até o source é 3, 3 até o source é 2


def relax(d, v, tent, pq):
    if d[v] > tent:  # menor distância provisória
        if d[v] == float('inf'):
            pq.insert(v, tent)  # adiciona 'v' para a PriorityQueue
        else:
            pq.decrease_key(v, tent)  # diminui a prioridade de 'v'
        d[v] = tent  # atualiza a distância de 'v'


# DIJKSTRA_PREDICTION Durante as primeiras i0 iterações, um array X é criado para armazenar o "traço" do algoritmo.
# Na iteração i0, o "traço" criado X é usado para computar uma predição inicial chamando o procedimento PREDICITON.
# X[i] armazena o par (d(u), B), que consiste na distância do nó estabelecido u e o valor limite superior B na
# iteração i.

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

    return d  # Exemplo: {1: 5, 2: 3, 3: 2} -> 1 até o source é 5, 2 até o source é 3, 3 até o source é 2


# SMART_RESTART
# Esse procedimento é criado caso a previsão P for muito pequena, onde ela vai ser aumentada e o algoritmo
# continua com a nova previsão.
# OBS: A utilização desse procedimento não deve acontecer com muita frequencia, uma vez que pode reduzir a 
# eficiência do algoritmo.

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
