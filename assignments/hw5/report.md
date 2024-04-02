# Learning report

## Summary

My work began with importing Python implementation of several sorting methods
from [Programiz](https://www.programiz.com/dsa/), which I then modified for
optimization and code style consistency. Using a map data structure, I then
populate the analysis of time spent on each custom sorting technique. Having
generated the analysis, I present them as multiple graphs simultaneously, thanks
to the knowledge of Matplotlib from the earlier assignment. I noticed that
bubble sorting is the worst performer of the bunch and slows the program
simultaneously, so I provided the ability to skip it to save testing time.

## Question 1

> Did you successfully get your assignment done? Did it run? Any error? Did you
  get the correct result? Did you test your program thoroughly?

I have completed the assignment successfully without an error. Although the
graphs produced by my solution differ from the ones on the question sheet, I am
confident of their accuracy.

## Question 2

> How much time did you spend completing your assignment?

Producing the source code took several hours. However, I did spend an extra day
writing the sorting essay and this report, totaling almost two days of work.

## Question 3

> Did you find the assignment easy or challenging for you?

It is more challenging because it requires some level of academic writing
skills.

## Question 4

> Did you write the program yourself? Did you get any help from anyone?

I wrote the essay and the program myself, even though I did get some help from
[Grammarly](https://www.grammarly.com/) and [Thesaurus](https://www.thesaurus.com/).

## Question 5

> How did you resolve the issues when you encountered obstacles to completing
  your program? Did you use Google to get help? Describe how Google was able or
  not able to assist you.

Since this homework utilizes knowledge we acquired from previous assignments
(dictionary, *Matplotlib*, etc.), I spent less time on online resources such as
Google and StackOverflow.

## Question 6

> What did you learn from doing this assignment?

I learned that, like Kotlin, Python supports an optional type declaration, also
known as type hinting. The applied restriction is valuable as an early warning
during a type mismatch.

## Question 7

> Any other information you would like to share with your instructor? Make sure
  you provide program output on each option.

Python does not have built-in access modifiers like `private` or `internal`.
Although the official documentation recommends [underscore naming conventions](https://peps.python.org/pep-0008/#public-and-internal-interfaces)
for such purposes, renaming them does not restrict their visibility. I accept
that the philosophy of Python prioritizes simplicity over total control, but I
still see this as a huge setback. I am concerned about the potential misuse or
execution of internal components. Software engineers should not trust each other
to make the right decision. After all, we are not all responsible human beings.
