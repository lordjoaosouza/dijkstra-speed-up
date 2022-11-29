import random

from graph.graph import Graph
from dijkstra.dijkstra import dijkstra_prunning, dijkstra_prediction
import pandas as pd
import matplotlib.pyplot as plt
import time


def main():
    vertexes = list()
    weights = list()
    for i in range(1, 100):
        vertexes.append(i)
    for i in range(100):
        number = random.randint(1, 10)
        weights.append(number)

    dict_graph = dict()
    for i in range(1, 100):
        for j in range(1, 100):
            if i != j:
                dict_graph[(i, j)] = random.choice(weights)

    graph = Graph(dict_graph)

    prediction_time_list = list()
    prunning_time_list = list()

    for i in range(100):
        prediction_time = time.time()
        dijkstra_prediction(graph, 1, [6], 2, 0.5, 0.5)
        prediction_time_final = time.time() - prediction_time
        prediction_time_list.append(prediction_time_final)

        prunning_time = time.time()
        dijkstra_prunning(graph, 1, [6])
        prunning_time_final = time.time() - prunning_time
        prunning_time_list.append(prunning_time_final)

    print(f"Prediction average time: {(sum(prediction_time_list) / len(prediction_time_list) * 1000):.6f}ms")
    print(f"Prunning average time: {(sum(prunning_time_list) / len(prunning_time_list) * 1000):.6f}ms")

    df_prediction = pd.DataFrame(prediction_time_list, columns=['Prediction'])
    df_prunning = pd.DataFrame(prunning_time_list, columns=['Prunning'])

    df = pd.concat([df_prediction, df_prunning], axis=1)
    df.plot(kind='bar', figsize=(20, 10))
    plt.xlabel('Number of executions')
    plt.ylabel('Time (ms)')
    plt.show()


if __name__ == '__main__':
    main()
