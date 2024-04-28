# This program checks if from start point to end point is
# the way to reach but not vice versa.
# The program analyze the data based on alphabet graph (defined in main function).


def is_reachable(graph, start_point, end_point):
    visited = None
    if visited is None:
        visited = []
    visited.append(start_point)

    if start_point == end_point:
        return True

    for value in graph[start_point]:
        if value not in visited and is_reachable(graph, value, end_point):
            return True

    return False


def main():
    graph = {
        'A': ['C', 'K', 'L', 'J'],
        'B': [],
        'C': ['B', 'E', 'M', 'O', 'F', 'G', 'N', 'Q', 'R'],
        'D': ['S', 'T', 'X', 'Z', 'Y'],
        'E': [],
        'F': ['H', 'P'],
        'G': [],
        'H': [],
        'I': [],
        'J': [],
        'K': [],
        'L': ['W', 'V', 'U', 'I'],
        'M': [],
        'N': [],
        'O': [],
        'P': [],
        'Q': [],
        'R': [],
        'S': [],
        'T': [],
        'U': [],
        'V': [],
        'W': [],
        'X': [],
        'Y': [],
        'Z': [],
    }

    start_point = input("Enter start point: ").upper()
    end_point = input("Enter end point: ").upper()

    if is_reachable(graph, start_point, end_point):
        print(f"There is a way to reach from {start_point} to {end_point}.")
    else:
        print(f"There is no way to reach from {start_point} to {end_point}.")


if __name__ == "__main__":
    main()
