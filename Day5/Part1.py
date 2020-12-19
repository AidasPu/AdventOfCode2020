def replace(s):
    maximum = 0
    for line in s.splitlines():
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('R', '1').replace('L', '0')
        maximum = max(maximum, int(line, 2))

    return maximum


with open("input.txt") as f:
    print(replace(f.read()))
