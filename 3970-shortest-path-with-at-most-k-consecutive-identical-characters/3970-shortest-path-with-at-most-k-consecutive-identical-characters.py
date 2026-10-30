class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        # Build the adjacency list
        graph = [[] for _ in range(n)]


        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum cost to reach this state
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Start at node 0; its character run length is 1
        dist[0][1] = 0

        # Heap stores: (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            # Skip outdated entries
            if cost > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            # Explore neighboring nodes
            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Reject paths exceeding k consecutive characters
                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_count)
                    )

        return -1




        