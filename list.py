N = int(input())
l = []
for i in range(N):
    cm = input().split()
    if cm[0] == "insert":
        l.insert(int(cm[1]),int(cm[2]))
    elif cm[0] == "print":
        print(l)
    elif cm[0] == "remove":
        l.remove(int(cm[1]))
    elif cm[0] == "append":
        l.append(int(cm[1]))
    elif cm[0] == "sort":
        l.sort()
    elif cm[0] == "pop":
        l.pop()
    elif cm[0] == "reverse":
        l.reverse()