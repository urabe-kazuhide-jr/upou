print("Loop 1")
print("Hello, World!")
t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0

print("Initial value of t is:", t)
print("Initial value of a is:", a)
print("Initial value of n is:", n)
print("Initial value of M is:", M)
print("Initial value of d is:", d)
print("Initial value of m is:", m)
print("Initial value of B is:", B)

print("Initial total is:", total)
for k in range(1, n + 1):
    total = total + a * k
    print("Total after (k)", k, "iterations is:", total)


print("")
print("Loop 2")

t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0
x = M
count = 0
while x >= d:
    x = x - d
    count = count + 1
    print("Current value of x is:", x)
print("The value of x after the loop is:", x)
print("The number of iterations is:", count)


print("")
print("Loop 3")
t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0
best = -1
for k in range(n):             # k takes the values 0, 1, ..., n - 1
    value = (t + k * m) % 20   # a personal number from 0 to 19
    if value > best:
        best = value
    print("Current value of k is:", k, "and current best is:", best)

print("The best value found is:", best)


print("")
print("Flawed Loop 1")

t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0
best = 99

for k in range(n):
    value = (t + k * m) % 20
    if value > best:
        best = value
    print("Current value of k is:", k, "and current best is:", best)
print("The best value found is:", best)

print("")
print("Flawed Loop 2")
t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0
x = M
count = 0
while x >= d:
    x = x - d
    print("Current value of x is:", x)
count = count + 1
print("The value of x after the loop is:", x)
print("The number of iterations is:", count)


print("")
print("Flawed Loop 3")
t = 1080
a = 2 + 1080 % 7
n = 5 + 1080 % 4
M = 40 + 1080 % 37
d = 4 + 1080 % 5
m = 3 + 1080 % 6
B = 1080 % 3
total = 0
for k in range(1, n):
    total = total + a * k
    print("Total after", k, "iterations is:", total)
print("The total after the flawed loop is:", total)


print("first commit")