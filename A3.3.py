from typing import List

def fun():
    arr = list()
    num = int(input("Enter the number of elements"));
    for i in range(num):
        numbers = int(input("Enter number"));
        arr.append(numbers);

    print("Maximum number is", min(arr));


fun()

Output:
Enter the number of elements4
Enter number33
Enter number22
Enter number55
Enter number66
Maximum number is 22