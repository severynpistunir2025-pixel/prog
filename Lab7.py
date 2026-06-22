import csv
from typing import List

def read_matrix_from_csv(file_path: str) -> List[List[int]]:

    matrix = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
             matrix.append([int(val) for val in row])
    return matrix

def prim_mst_length(matrix: List[List[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 0
    if n == 1:
        return 0

    selected = [False] * n
    selected[0] = True
    edges_count = 0
    min_cost = 0

    while edges_count < n - 1:
        minimum = float("inf")
        x = 0
        y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j] != 0:
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            x = i
                            y = j

        if minimum == float("inf"):
            return -1

        min_cost += minimum
        selected[y] = True
        edges_count += 1

    return min_cost

if __name__ == "__main__":
    try:
        islands_matrix = read_matrix_from_csv("islands.csv")
        result = prim_mst_length(islands_matrix)
        
        if result == -1:
            print("Неможливо з'єднати всі острови (граф незв'язний).")
        else:
            print(f"Мінімальна довжина підводних кабелів: {result}")
    except FileNotFoundError:
        print("Файл islands.csv не знайдено.")