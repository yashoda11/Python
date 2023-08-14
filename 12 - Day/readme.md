# For Loop :

**For Loop :**
- In Python, a `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The loop continues until all items in the sequence have been processed.

**Syntax :**
 - The basic syntax of a for loop in Python is as follows:
```
for item in sequence:
    # Code block to be executed for each item in the sequence
```

**Example:**
- Printing numbers from 1 to 5 using a for loop
```
for num in range(1,6):
    print(num)
```

**Output :**
```
1
2
3
4
5
```

**Explanation :**
- In this example, we use a `for` loop to iterate over a range of numbers from 1 to 5 (excluding 6). 
- The `range` function generates a sequence of numbers starting from the first argument (1) and up to, but not including, the second argument (6). 
- For each value of `num` in the sequence, the loop executes the code block, which prints the value of `num`.
- The loop iterates five times, printing the numbers 1 to 5, and then stops when all items in the sequence have been processed.