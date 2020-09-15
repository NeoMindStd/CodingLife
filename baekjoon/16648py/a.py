t, p = map(int, input().split())
ec = max(0, 20-p)
tpb = t / (2*ec + min(80, 100-p))
print(min(20,p)*tpb*2 + max(0, p-min(20,p))*tpb)
