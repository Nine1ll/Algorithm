import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}
for i in range(1, n+1):
    pokemon[sys.stdin.readline().rstrip()] = str(i)

pokemon2 = {value: key for key, value in pokemon.items()}

for j in range(m):
    q = sys.stdin.readline().rstrip()
    if q in pokemon.keys():
        print(pokemon[q])

    if q in pokemon2.keys():
        print(pokemon2[q])