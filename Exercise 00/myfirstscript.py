import sys
import numpy as np
import matplotlib.pyplot as plt


def func(x: np.float64) -> np.float64:
    return np.round(np.cos(x) * np.exp(x), 4)


def plot(func: callable, domain: tuple[float] = (-2 * np.pi, 2 * np.pi)):
    x = np.linspace(*domain, 100)
    plt.plot(x, func(x), color="red")
    plt.show()


if __name__ == "__main__":
    try:
        inputs = sys.argv[1:]
        graph = False

        if not inputs[-1].isnumeric():
            graph = inputs.pop() == "g"

        values = list(map(int, inputs))
        print(" ".join([str(func(i)) for i in values]))

        if graph:
            plot(func)
    except:
        print("Error only numbers allowed!!")
