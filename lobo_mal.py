T, D = input().split() 
V, P = input().split()
T, D, V, P = int(T), int(D), int(V), int(P)
V = V * T
P = (T // D) * P
print(V + P)