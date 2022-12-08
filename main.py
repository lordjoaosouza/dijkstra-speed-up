import random

from graph.graph import Graph
from dijkstra.dijkstra import dijkstra_pruning, dijkstra_prediction
import pandas as pd
import matplotlib.pyplot as plt
import time


def main():
    prediction_time_list = list()
    pruning_time_list = list()

    for i in range(1000):
        dict_graph = dict()
        vertexes = list()
        for j in range(1, 100):
            vertexes.append(j)

        for j in range(1, 100):
            dict_graph[(random.choice(vertexes), random.choice(vertexes))] = random.randint(1, 10)

        graph = Graph(dict_graph)

        prediction_time = time.time()
        dijkstra_prediction(graph, 1, [6], 2, 0.5, 0.5)
        prediction_time_final = time.time() - prediction_time
        prediction_time_list.append(prediction_time_final)

        pruning_time = time.time()
        dijkstra_pruning(graph, 1, [6])
        pruning_time_final = time.time() - pruning_time
        pruning_time_list.append(pruning_time_final)

    print(f"Prediction average time: {(sum(prediction_time_list) / len(prediction_time_list) * 1000):.6f}ms")
    print(f"Pruning average time: {(sum(pruning_time_list) / len(pruning_time_list) * 1000):.6f}ms")

    df_prediction = pd.DataFrame(prediction_time_list, columns=['Prediction'])
    df_pruning = pd.DataFrame(pruning_time_list, columns=['Pruning'])

    df = pd.concat([df_prediction, df_pruning], axis=1)
    df.plot(kind='bar', figsize=(20, 10))
    plt.xticks(range(0, 1000, 10))
    plt.xlabel('Number of executions')
    plt.ylabel('Time (ms)')
    plt.show()


if __name__ == '__main__':
    main()
