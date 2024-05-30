# This program checks if from start point to end point is
# the way to reach but not vice versa (based on the graph in main function).

GRAPH_POINTS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

cache = {}


def checking_points_existence():
    start_point = input("Enter start point: ").upper()
    while start_point not in GRAPH_POINTS:
        start_point = input(f"Wrong input. {start_point} does not exist in the Graph. Try again: ").upper()

    end_point = input("Enter end point: ").upper()
    while end_point not in GRAPH_POINTS:
        end_point = input(f"Wrong input. {end_point} does not exist in the Graph. Try again: ").upper()

    return start_point, end_point


def find_start_point(graph, start_point):
    if isinstance(graph, dict):
        for key, value in graph.items():
            if key == start_point:
                return value
            found = find_start_point(value, start_point)
            if found is not None:
                return found
    elif isinstance(graph, list):
        for item in graph:
            found = find_start_point(item, start_point)
            if found is not None:
                return found
    else:
        return None


def is_reachable(graph, start_point, end_point):
    if (start_point, end_point) in cache:
        return cache[(start_point, end_point)]

    if start_point == end_point:
        cache[(start_point, end_point)] = True
        return True

    subgraph = find_start_point(graph, start_point)
    if find_start_point(subgraph, end_point) is not None:
        cache[(start_point, end_point)] = True
        return True
    else:
        cache[(start_point, end_point)] = False
        return False


def main():
    graph = {
        'A': [
            {'C': [
                {'B': [
                    {'D': [
                        {'S': []},
                        {'T': []},
                        {'X': []},
                        {'Z': []},
                        {'Y': []}]},
                    {'E': []},
                    {'M': []},
                    {'O': []}]},
                {'F': [
                    {'H': []},
                    {'P': []}]},
                {'G': []},
                {'N': []},
                {'Q': []},
                {'R': []}
            ]},
            {'K': []},
            {'L': [
                {'W': []},
                {'V': []},
                {'U': []},
                {'I': []}
            ]},
            {'J': []}
        ]
    }

    start_point, end_point = checking_points_existence()
    result = is_reachable(graph, start_point, end_point)

    if result:
        print(f"Yes. There is a way to reach from {start_point} to {end_point}.")
    else:
        print(f"No. There is no way to reach from {start_point} to {end_point}.")


if __name__ == "__main__":
    main()
