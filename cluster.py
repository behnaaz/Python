from operator import itemgetter
a = [93,7,97,12,-54,-5]
n = 1
m = []

print(a)
for i in range(len(a)):
    for j in range(len(a)):
        d = {"diff": abs(a[i] - a[j]), "from": i, "to": j}
        m.extend([d])
        m = sorted(m, key = itemgetter("diff"), reverse = True)
print(m[0])
one = [m[0]["from"]]
two = [m[0]["to"]]
for i in range(len(a)):
    if not i in one and not i in two:
        yek = m[0]["diff"]
        for j in one:
            t = abs(a[i] - a[j])
            if t < yek:
               yek = t
        dow = m[0]["diff"]
        for j in two:
            t = abs(a[i] - a[j])
            if t < dow:
               dow = t
        if yek < dow:
           one.extend([i])
        else:
           two.extend([i])
print(one)
for i in range(len(one)):
    print(a[one[i]])
print(two)
for i in range(len(two)):
    print(a[two[i]])
