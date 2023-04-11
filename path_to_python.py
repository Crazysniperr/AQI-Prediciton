st = input()
res = ""
n = len(st)
for i in range(n):
    if st[i] == "\\":
        res+="/"
    else:
        res+=st[i]
print(res)
        