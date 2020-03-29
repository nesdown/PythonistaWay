x = 0

while (x < 4):
    print(x)
    x += 1

print("---------")

for x in range(7):
    print(x)

print("---------")

Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

for m in Months:
    print(m)

print("---------")

for x in range(10, 20):
    if (x % 2 == 0):
        continue
    print(x)

print("---------")

for i, m in enumerate (Months):
    print(i, m)

print("---------")

for i in '123':
    print("Z-Digital", i)