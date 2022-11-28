from graph.graph import Graph
from dijkstra.dijkstra import dijkstra_prunning, dijkstra_prediction
import time


def main():
    example = Graph(
        {
            (1, 2): 1,
            (1, 3): 2,
            (2, 3): 3,
            (2, 4): 4,
            (3, 4): 5,
            (3, 5): 6,
            (4, 5): 7,
            (4, 6): 8,
            (5, 6): 9,
            (5, 7): 10,
        }
    )

    prunning_time = time.time()
    print(dijkstra_prunning(example, 1, [6]))
    print(f"Prunning time: {((time.time() - prunning_time) * 1000):.6f}ms\n")

    prediction_time = time.time()
    print(dijkstra_prediction(example, 1, [6], 2, 0.5, 0.5))
    print(f"Prediction time: {((time.time() - prediction_time) * 1000):.6f}ms")


if __name__ == '__main__':
    main()
