import collections

def flood_fill(matrix, start_row, start_col, new_color):
    """
    Flood fill
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0 

    if rows == 0 or cols == 0 or start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols:
        return matrix
    
    target_color = matrix[start_row][start_col]
    
    if target_color == new_color:
        return matrix

    queue = collections.deque([(start_row, start_col)])
    matrix[start_row][start_col] = new_color

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == target_color:
                matrix[nr][nc] = new_color
                queue.append((nr, nc))

    return matrix

    гг8
def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
            
        if len(lines) < 4:
            print("Помилка: Недостатньо даних у файлі input.txt")
            return
        
        height, width = map(int, lines[0].split(','))
        start_row, start_col = map(int, lines[1].split(','))
        new_color = lines[2].strip(" '\"‘’")
        matrix = []

        for line in lines[3:]:
            clean_elements = [char.strip(" '\"‘’[]") for char in line.split(',')]
            row = [char for char in clean_elements if char]
            if row:
                matrix.append(row)

        result_matrix = flood_fill(matrix, start_row, start_col, new_color)

        with open('output.txt', 'w', encoding='utf-8') as f:
            for i, row in enumerate(result_matrix):
                line_str = str(row)
                if i < len(result_matrix) - 1:
                    line_str += ','
                f.write(line_str + '\n')
                
        print("Успіх! BFS алгоритм виконав заливку. Перевірте файл output.txt.")

    except FileNotFoundError:
        print("Помилка: Файл input.txt не знайдено.")
    except Exception as e:
        print(f"Сталася неочікувана помилка під час обробки: {e}")

if __name__ == '__main__':
    main()