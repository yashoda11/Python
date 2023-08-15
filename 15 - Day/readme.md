# Loop Control Statements :

**Loop Control Statements :**
1. break
2. continue
3. and pass.

**1. `break` Statement :**
- The `break` statement is used to terminate a loop prematurely when a certain condition is met.

```
# Example: Using 'break' to stop the loop when the value reaches 3
for num in range(1, 6):
    if num == 3:
        break
    print(num)
```

Output:
```
1
2
```

**Explanation :**
- In this example, the loop runs from 1 to 5, but when num becomes 3, the break statement is encountered, and the loop is terminated immediately.

**`continue` Statement :**
- The `continue` statement is used to skip the current iteration of a loop and move to the next iteration.

```
# Example: Using 'continue' to skip printing even numbers
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)
```

Output:
```
1
3
5
```

**Explanation :**
- In this example, the loop runs from 1 to 5, but when an even number is encountered (2 and 4), the `continue` statement is used, skipping the `print` statement, and the loop moves to the next iteration.

**`pass` Statement :**
- The `pass` statement is used as a placeholder when you don't want to execute any code inside a loop or a conditional block.

```
# Example: Using 'pass' to do nothing inside the loop
for num in range(1, 6):
    pass
```

**Explanation :**
- In this example, the loop runs from 1 to 5, but the `pass` statement does nothing inside the loop.