# **Nested Loops**

**1. Nested Loop to Print a Rectangular Pattern :**

- **Example :** Print a 3x3 rectangular pattern using nested loops

```
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # Move to the next line after each row

```

**Output :**
```
* * *
* * *
* * *
```

**2. Nested Loop to Print a Triangle Pattern :**

- **Example: Print a right-angled triangle pattern using nested loops :**
```
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after each row
```

**Output :**
```
*
* *
* * *
* * * *
* * * * *
```