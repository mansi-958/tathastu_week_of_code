a = int(input("Enter the size of tuple: "))
arr = []
for i in range(a):
    arr.append(input())
arr = tuple(arr)
b= input("Enter the element occurrences you want to know: ")
print("Tuple contains the element", arr.count(b), "times")

