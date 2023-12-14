from collections import deque


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def create_graph(m):
    graph = {}
    rows, cols = len(m), len(m[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 1:
                neighbors = []
                for dx, dy in directions:
                    new_x, new_y = i + dx, j + dy
                    if is_valid(new_x, new_y, rows, cols) and m[new_x][new_y] == 1:
                        neighbors.append((new_x, new_y))
                graph[(i, j)] = neighbors

    return graph


def find_shortest_path(m):
    if not m or not m[0]:
        return -1

    rows, cols = len(m), len(m[0])

    start_vertexes = []
    end_vertexes = []

    for i in range(rows):
        if m[i][0] == 1:
            start_vertexes.append((i, 0))
        if m[i][cols - 1] == 1:
            end_vertexes.append((i, cols - 1))

    if len(start_vertexes) == 0 or len(end_vertexes) == 0:
        return -1

    graph = create_graph(m)

    distances = []

    for start in start_vertexes:
        for end in end_vertexes:
            visited = set()
            queue = deque([(start, 0)])
            visited.add(start)

            while queue:
                (x, y), distance = queue.popleft()

                if (x, y) == end:
                    distances.append(distance)

                for neighbor in graph.get((x, y), []):
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
                        visited.add(neighbor)

    return min(distances) if len(distances) > 0 else -1


if __name__ == "__main__":
    inputFile = open("input.txt", "r")
    matrix = [list(map(int, line.strip().split())) for line in inputFile]

    result = find_shortest_path(matrix)

    outputFile = open("output.txt", "w")
    outputFile.write(str(result))
