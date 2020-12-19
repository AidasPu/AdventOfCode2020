def replace_count(file):
    possible = set(range(1024))
    for line in file.splitlines():
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('R', '1').replace('L', '0')
        possible.discard(int(line, 2))

    for candidate in possible:
        if candidate - 1 not in possible and candidate + 1 not in possible:
            return candidate


with open("input.txt") as f:
    print(replace_count(f.read()))
