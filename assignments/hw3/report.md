<!-- hotfix: KaTeX -->
<!-- https://github.com/yzane/vscode-markdown-pdf/issues/21/ -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: { inlineMath: [['$', '$']] }, messageStyle: 'none' });</script>

# Learning report

## Question 1

> Did you complete your assignment and did your program run without errors?

I have completed the assignment with no known errors.

## Question 2

> Did your program produce the correct result?

Yes, although it was not immediately clear because the question sheet expects
matrix result

$$
\begin{pmatrix}
  5.3 & 23.9 & 24 \\\\
  11.6 & 56.3 & 58.2 \\\\
  \color{red} 111.9 & 88.7 & 92.4
\end{pmatrix}
$$

While my solution produced

$$
\begin{pmatrix}
  5.3 & 23.9 & 24 \\\\
  11.6 & 56.3 & 58.2 \\\\
  \color{red} 17.9 & 88.7 & 92.4
\end{pmatrix}
$$

However, having consulted the result with [Matrix Multiplication Calculator](https://matrix.reshish.com/multiplication.php),
I am confident that my solution is correct.

## Question 3

> Did you test your program thoroughly?

I tested my solution with standard sample data, edge cases and incorrect input.

## Question 4

> How much time did you spend completing your assignment?

Having grasped the basics from earlier assignments, completing the homework took
me several hours.

## Question 5

> Did you write the program yourself? Did you get any help from anyone?

I wrote my program alone using online resources as a knowledge base.

## Question 6

> How did you resolve the issues when you encountered obstacles to completing
  your program? Did you use Google or other resources to get help? Describe how
  Google or other resources was abled or not able to assist you.

Google has always been helpful as a starting point, but it only works well if
the problems are common enough to appear in discussion boards and forums. For a
more specific issue, I'd spend a considerable amount of time skimming official
documentation and other wikis.

## Question 7

> What did you learn from doing this assignment?

I gain knowledge of multi-dimension list/array in this assignment, particularly
how to create one with default values:

```python
c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
# or
c = [[0] * len(b[0]) for _ in range(len(a))]
```

I also learned about Anaconda distribution and have started to embrace it as a
full-fledged Python replacement in my working environment.

## Question 8

> Any other information you would like to share with your instructor?

I was told to believe that Python is effortless to master compared to other
similarly [popular languages](https://www.python.org/doc/essays/comparisons/)
like Java and C++. However, I still find some Python syntaxes harder to grasp.
Consider the examples below.

- Python

  ```python
  c = [[0] * len(b[0]) for _ in range(len(a))]
  ```

- Java

  ```java
  int[][] c = new int[a.length][b[0].length];
  // custom default value
  for (int[] row : c) Arrays.fill(row, defaultValue);
  ```

- C++

  ```cpp
  std::vector<std::vector<int>> c(a.size(), std::vector<int>(b[0].size(), 0));
  ```

Python arguably retains the smallest code implementation. But in my opinion, its
intent to populate the array is not immediately clear. Nevertheless, I still
enjoy the learning process and I thank you for the opportunity.
