t = int(input())

if t <= 3500:
    s = t
elif t <= 4955:
    s = 3500 + (t-3500)/0.97
elif t <= 7655:
    s = 5000 + (t-4955)/0.9
elif t <= 11255:
    s = 8000 + (t-7655)/0.8
elif t <= 30755:
    s = 12500+(t-11255)/0.75
elif t <= 44755:
    s = 38500 + (t-30755)/0.7
elif t <= 61005:
    s = 58500 + (t-44755)/0.65
else:
    s = 83500 + (t-61005)/0.55
s = int(s)
print(s)