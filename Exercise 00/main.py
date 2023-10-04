import numpy as np
import matplotlib.pyplot as plt

def createNormalRandomVar(mean: float = 5, standard_dev: float = 2, size: int= 100_000) -> np.ndarray:
    return np.random.normal(mean, standard_dev, size)

def createUniformRandomVar(low: float = 0, high: float = 10, size: int= 100_000) -> np.ndarray:
    return np.random.uniform(low, high, size)


def computeMean(vector: np.ndarray) -> np.float64:
    return np.mean(vector)

def computeStandardDev(vector: np.ndarray) -> np.float64:
    return np.sqrt(np.mean(np.power(vector - np.mean(vector), 2)))


def plotHist(vector: np.ndarray):
    plt.hist(vector)
    plt.xlim(np.min(vector) - 0.5, np.max(vector) + 0.5)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    vector = createNormalRandomVar()
    print(computeMean(vector), computeStandardDev(vector))
    plotHist(vector)
    vector = createUniformRandomVar()
    print(computeMean(vector), computeStandardDev(vector))
    plotHist(vector)