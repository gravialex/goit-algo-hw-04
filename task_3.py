import random
import timeit

# Збільшуємо ліміт рекурсії для сортування злиттям на великих масивах
import sys
sys.setrecursionlimit(200000)

# ==========================================
#  РЕАЛІЗАЦІЯ АЛГОРИТМІВ СОРТУВАННЯ
# ==========================================

# Сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_result.append(left[i])
            i += 1
        else:
            sorted_result.append(right[j])
            j += 1
    sorted_result.extend(left[i:])
    sorted_result.extend(right[j:])
    return sorted_result


# ==========================================
#  ТЕСТУВАННЯ ТА ЗАМІРИ
# ==========================================

def run_benchmarks():
    # Набори даних різного розміру
    sizes = [100, 1000, 5000, 10000]
    
    print(f"{'Розмір масиву':<15} | {'Алгоритм':<20} | {'Час виконання (сек)':<20}")
    print("-" * 70)

    for size in sizes:
        # Генеруємо випадковий масив
        data = [random.randint(0, 100000) for _ in range(size)]

        #  Замір для сортування вставками
        t_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=3)
        print(f"{size:<15} | {'Сортування вставками':<20} | {t_insertion:<20.6f}")

        #  Замір для сортування злиттям
        t_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=3)
        print(f"{size:<15} | {'Сортування злиттям':<20} | {t_merge:<20.6f}")

        #  Замір для Timsort (вбудований sorted)
        t_timsort = timeit.timeit(lambda: sorted(data.copy()), number=3)
        print(f"{size:<15} | {'Timsort (sorted)':<20} | {t_timsort:<20.6f}")
        print("-" * 70)

    # Додатковий тест на дуже великому масиві для Merge Sort та Timsort
    large_size = 500000
    large_data = [random.randint(0, 1000000) for _ in range(large_size)]
    
    print(f"\nТестування на великому масиві (n = {large_size}):")
    t_merge_large = timeit.timeit(lambda: merge_sort(large_data.copy()), number=1)
    t_timsort_large = timeit.timeit(lambda: sorted(large_data.copy()), number=1)
    
    print(f"Сортування злиттям: {t_merge_large:.6f} сек")
    print(f"Timsort (sorted):     {t_timsort_large:.6f} сек")
    print("-" * 70)


if __name__ == "__main__":
    run_benchmarks()