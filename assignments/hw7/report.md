# Learning report

## Summary

Following the guidance on the question sheet, I began my work by reading what
[NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/) and [SciPy](https://scipy.org/)
are to understand their capabilities and limitations. Pandas and Scipy seem
exceptionally extensive, with SciPy having more than over 30 sub-packages
attributed to each scientific field like linear algebra, signal processing, and
imaging. However, I am thankful this assignment is only scratching the surface
of the mentioned third-party libraries. After hours of skimming and reading,
completing the homework proved to be easier because we could utilize the
acquired skills from previous assignments such as 2-D array operations, map data
structure and graphical charts with Matplotlib.

## Question 1

> Did you successfully get your assignment done? Did it run? Any error? Did you
  get the correct result? Did you test your program thoroughly?

My solution produced the correct results that are identical to the example in
the question sheet. Although there is some confusion about the starting point of
an index, I put a note suggesting that in this script, the index starts at `0`.

## Question 2

> How much time did you spend completing your assignment?

Due to time constraints during my time in my home country, I can only allocate
two hours each day to work on assignments for this semester's courses. With this
in mind, it took me three days to complete the homework.

## Question 3

> Did you find the assignment easy or challenging for you?

It is challenging to learn about new libraries and their APIs. This is
especially true with Python libraries because some functions have a lot of
parameters. Take [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
for example. It has 50 configurable function parameters.

## Question 4

> Did you write the program yourself? Did you get any help from anyone?

I work alone in scrounging online resources and writing the solutions.

## Question 5

> When you encountered obstacles to completing your program, how did you resolve
  the issues? Did you use Google to get help? Describe how Google was able or
  not able to assist you?

For this particular assignment, NumPy and SciPy have already published user
guides that to me are more helpful than Google and StackOverflow. But when I do
encounter an issue, I will be sure to reach out to others in StackOverflow.

## Question 6

> What did you learn from doing this assignment?

I learned that NumPy is the foundation of all the subsequent libraries mentioned
here: SciPy, pandas, and Matplotlib.

## Question 7

> Any other information you would like to share with your instructor? Make sure
  you provide program output on each option.

I have accepted Anaconda distribution as a better Python development environment
mainly because of the automatic package dependency resolution (despite its large
file size). A library or package installation typically comes with its
dependencies. For example, importing a Java library via Maven will include
subsequent artifacts, and installing an NPM package extends to the declared
dependencies. However, the dependency resolution is unavailable in PIP,
requiring us to specify each package separately or risk triggering an
`ImportError` on runtime.
