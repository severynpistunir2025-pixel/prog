import heapq

def main():
    try:
        with open('gamsrv.in', 'r') as fin:
            lines = [line.strip() for line in fin if line.strip()]
    except FileNotFoundError:
        return

    if not lines:
        return

    N, M = map(int, lines[0].split())
    
    clients = set(map(int, lines[1].split()))
    
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(2, 2 + M):
        if i < len(lines):
            u, v, w = map(int, lines[i].split())
            graph[u].append((v, w))
            graph[v].append((u, w))
            
    best_max_latency = float('inf')
    potential_servers = [i for i in range(1, N + 1) if i not in clients]

    for server in potential_servers:
        dist = {i: float('inf') for i in range(1, N + 1)}
        dist[server] = 0

        pq = [(0, server)]
        
        visited_clients_count = 0
        current_max_dist = 0
        
        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            if d >= best_max_latency:
                break

            if u in clients:
                visited_clients_count += 1
                current_max_dist = max(current_max_dist, d)
                if visited_clients_count == len(clients):
                    break
                    
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        if visited_clients_count == len(clients):
            best_max_latency = min(best_max_latency, current_max_dist)

    with open('gamsrv.out', 'w') as fout:
        fout.write(str(best_max_latency) + '\n')

if __name__ == '__main__':
    main()