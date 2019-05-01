# lines = tuple(open('./zones', 'r'))
lines = open('./zones').read().splitlines()
# l = len(lines)
print lines[0].split(',')
# for i in range(0, l):
