import random
import time
from bubble import bubble_sort
from shaker import shaker_sort
from insertion import insertion_sort
from selection import selection_sort


# --------------------------------------
# Генерация входных данных
# --------------------------------------
def generate_data(n):
    return {
        "sorted": list(range(n)),
        "reversed": list(range(n, 0, -1)),
        "random": random.sample(range(n), n)
    }


# --------------------------------------
# Замер времени
# --------------------------------------
def measure(func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    comparisons, moves = func(arr_copy)
    end = time.perf_counter()
    return end - start, comparisons, moves


# --------------------------------------
# Главный тест
# --------------------------------------
def run_all(n=5000):
    print(f"\n===== ТЕСТ n={n} =====")

    data = generate_data(n)

    algorithms = {
        "Bubble": bubble_sort,
        "Shaker": shaker_sort,
        "Insertion": insertion_sort,
        "Selection": selection_sort
    }

    for name, algo in algorithms.items():
        print(f"\n--- {name} sort ---")
        for dtype, arr in data.items():
            t, cmp_, mov_ = measure(algo, arr)
            print(f"{dtype:<10}  time={t:.5f}s  cmp={cmp_}  moves={mov_}")


# --------------------------------------
# Точка входа
# --------------------------------------
if __name__ == "__main__":
    # Можно менять список размеров
    for size in [1000, 5000, 10000]:
        run_all(size)