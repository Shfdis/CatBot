class Alan:
    def __init__(self, stats):
        self.stats = stats

mass = []
for i in range(1):
    a, b = map(str, input().split())
    stats = {a: int(b)}
    c, d = map(str, input().split())
    stats.update({c: int(d)})
    mass.append(Alan(stats))

for i in mass:
    for j in i.stats:
        print(j)

