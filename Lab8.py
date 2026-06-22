def calculate_paths(W, H, matrix):
    dp = [[0] * W for _ in range(H)]
    char_sum = {chr(i): 0 for i in range(97, 123)} 

    for r in range(H):
        dp[r][0] = 1
        char_sum[matrix[r][0]] += 1

    for c in range(1, W):
        for r in range(H):
            char = matrix[r][c]
            dp[r][c] = dp[r][c-1] + char_sum[char]

            if matrix[r][c-1] == char:
                dp[r][c] -= dp[r][c-1]

        for r in range(H):
            char = matrix[r][c]
            char_sum[char] += dp[r][c]

    if H == 1:
        return dp[0][W-1]
    else:
        return dp[0][W-1] + dp[H-1][W-1]

def solve():
    try:
        with open('ijones.in', 'r') as f:
            lines = f.read().split()
    except FileNotFoundError:
        return

    if not lines:
        return

    W = int(lines[0])
    H = int(lines[1])
    matrix = lines[2:2+H]

    ans = calculate_paths(W, H, matrix)

    with open('ijones.out', 'w') as f:
        f.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()