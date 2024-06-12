# Minimum Operations

For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently <br> 
calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:<br>

Concepts Needed:<br>
1. Dynamic Programming:<br>

Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.<br>
[Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)<br>
2. Prime Factorization:<br>

Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of <br> 
the target number n.<br>
[Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiplespre-algebra-prime-factorization-prealg/v/prime-factorization)<br>
3. Code Optimization:

Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
How to optimize Python code<br>
4. Greedy Algorithms:<br>

The problem can also be approached with greedy algorithms, choosing the best option at each step.<br>
[Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)<br>
5. Basic Python Programming:<br>

Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.<br>
[Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)<br>
By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem <br> effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

## Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=h4i4kjwncoU)
# Requirements
## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

``` 
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$ 
```
```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```


## Tasks To Complete

+ [x] 0. **Minimum Operations**<br/>[0-minoperations.py](0-minoperations.py) contains a script that meets the following requirements:
  + In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.
    + Prototype: `def minOperations(n)`.
    + `boxes` is a list of lists.
    + Returns an integer.
    + If `n` is impossible to achieve, return `0`.