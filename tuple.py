n = int(input("Enter: "))
integer_list = map(int, input("Enter:").split())
t = tuple(integer_list)
print(hash(t))