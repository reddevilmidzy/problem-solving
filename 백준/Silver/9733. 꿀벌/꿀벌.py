import sys
input = sys.stdin.readlines
# 코드가 지저분하지만 readline"s" 를 알게된 문제!
ans = input()
work = []
for i in range(len(ans)):
    ans[i] = ans[i].rstrip()
    ans[i] = ans[i].split()
    work.extend(ans[i])

re = work.count("Re")
pt = work.count("Pt")
cc = work.count("Cc")
ea = work.count("Ea")
tb = work.count("Tb")
cm = work.count("Cm")
ex = work.count("Ex")
print("Re", re, "%.2f" %(re/len(work))) if len(work) != 0 else print("Re", re, "0.00")
print("Pt", pt, "%.2f" %(pt/len(work))) if len(work) != 0 else print("Pt", pt, "0.00")
print("Cc", cc, "%.2f" %(cc/len(work))) if len(work) != 0 else print("Cc", cc, "0.00")
print("Ea", ea, "%.2f" %(ea/len(work))) if len(work) != 0 else print("Ea", ea, "0.00")
print("Tb", tb, "%.2f" %(tb/len(work))) if len(work) != 0 else print("Tb", tb, "0.00")
print("Cm", cm, "%.2f" %(cm/len(work))) if len(work) != 0 else print("Cm", cm, "0.00")
print("Ex", ex, "%.2f" %(ex/len(work))) if len(work) != 0 else print("Ex", ex, "0.00")
print("Total", len(work), "1.00")