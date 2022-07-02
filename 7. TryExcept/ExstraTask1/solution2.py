inp1 = input()
inp2 = input()

try:
    print(int(inp1) + int(inp2))
except ValueError:
    print(inp1 + inp2)