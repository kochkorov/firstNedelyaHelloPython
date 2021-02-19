a = "один два три четыри"
b = len(a)
c = a.lower()
d = a.upper()
t = b-(b//2)
u = c[:t] + d[t:]
print(u)