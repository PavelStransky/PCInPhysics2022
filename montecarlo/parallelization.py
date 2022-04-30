from multiprocessing.dummy import Process
import numpy as np
import matplotlib.pyplot as plt

import time

from multiprocessing import Pool, Process, Value
import integration

def integrate_1D_Pool(p, n, f, a, b):
    #pool = Pool(processes=p)
    with Pool(processes=p) as pool:
        args = ((f, a, b, n), ) * p
        results = pool.starmap(integration.integrate, args)

    average = np.average(results)
    return average

def plot_1D_duration(processes=range(1, 20), n=50000000, f=integration.f, a=0, b=np.pi):
    durations = []

    for p in processes:
        start_time = time.time()
        result = integrate_1D_Process(p, n // p, f, a, b)
        duration = time.time() - start_time
        print(f"I({f.__name__}) = {result} (Doba výpočtu v {p} vláknech: {duration})")

        durations.append(duration)

    plt.plot(processes, durations)
    plt.title("Celkový čas výpočtu")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$T [s]$")
    plt.show()

def integrate_parallel(result, *args, **kwargs):
    result.value = integration.integrate(*args, **kwargs)

def integrate_1D_Process(p, n, f, a, b):
    processes = []
    results = []

    for _ in range(p):
        result = Value('d', 0)
        process = Process(target=integrate_parallel, args=(result, f, a, b, n))
        process.start()

        processes.append(process)
        results.append(result)
    
    for process in processes:
        process.join()

    results = [result.value for result in results]
    return np.average(results)


if __name__ == "__main__":
    #i = integrate_1D_Pool(4, 100000, integration.f, 0, 2 * np.pi)
    #print(i)
    #print(integrate_1D_Process(4, 1000000, integration.f, 0, 2 * np.pi))
    plot_1D_duration()
