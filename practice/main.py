a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

a = 10
b = 25
c = 15

largest = max(a, b, c)
print("Largest number is:", largest)

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

n = int(input("Enter number of terms: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


n = int(input("Enter limit: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


def factors(n):
    print("Factors are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

factors(12)


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter terms: "))
for i in range(n):
    print(fib(i), end=" ")


def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

n = int(input("Enter n: "))
print("Sum =", sum_n(n))


s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

print("Result:")
for row in result:
    print(row)

s = "Hello World"

print("Length:", len(s))
print("Index of 'W':", s.index("W"))
print("Slicing:", s[0:5])
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Startswith 'Hello':", s.startswith("Hello"))
print("Endswith 'World':", s.endswith("World"))
print("Concatenation:", s + "!!!")


list1 = [1, 2, 3]
list2 = [4, 5]

print("Concatenation:", list1 + list2)
print("Repetition:", list1 * 2)
print("Slicing:", list1[0:2])
print("Max:", max(list1))
print("Min:", min(list1))

list1.append(6)
print("Append:", list1)

list1.remove(2)
print("Remove:", list1)

list1.sort()
print("Sort:", list1)

list1.reverse()
print("Reverse:", list1)
