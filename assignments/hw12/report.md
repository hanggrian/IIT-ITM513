# Learning report

## Question 1

> Did you complete your assignment and did it run without errors?

I have finished all the tasks of this assignment, I am fairly confident it
satisfies the user's requirements.

## Question 2

> Did your program produce the correct result?

The program achieves the desired behavior. Visually, it even mimics the design
wireframe provided by the question sheet.

## Question 3

> Did you test your program thoroughly?

I tested my solution manually with various inputs and automatically with unit
tests.

## Question 4

> How much time did you spend to complete your assignment?

I spent about 6 hours to complete this assignment. Writing a clean report took a
significant portion of the time as usual.

## Question 5

> Did you write the program yourself? Did you get any help from anyone?

I did not receive any assistance from anyone. However, certain parts of the
source code may be inspired by online resources.

## Question 6

> When you encountered obstacles to complete your program, how did you resolve
  the issues? Did you use Google to get help? Describe how Google was abled or
  not able to assist you?

Google services are invaluable in this assignment because I find
[Tkinter official documentation](https://docs.python.org/3/library/tkinter.ttk.html)
insufficient, leaving me to search for alternatives. For instance, GUI widgets
(`Frame` and `Button`) and their respective attributes are not immediately
available. One would assume they are located in [widgets section](https://docs.python.org/3/library/tkinter.ttk.html),
but even it does not list complete widgets. It is pitiful that third-party
libraries including NumPy and Matplotlib have better documentation than
built-in components like Tkinter.

## Question 7

> What did you learn from doing this assignment?

By far, the most valuable lesson I learned in this homework is declaring `main`
method and the ability to detect whether a script is running directly. This
allows the script to be importable by other scripts without triggering the main
function. I am organizing my files more consistently and I thank you for
introducing me to this technique.

## Question 8

> Any other information you would like to share with your instructor?

Certain features of Python programming in Linux are broken. For one, Tkinter
[renders incorrect fonts](https://stackoverflow.com/questions/54170918/tkinter-font-not-changing-on-python-3-6-8-ubuntu-18-04lts/) in an Anaconda
environment. Matplotlib is experiencing an
[issue displaying from a Wayland backend](https://github.com/NixOS/nixpkgs/issues/158806/), resulting in blurry graphs. I am somewhat confused by this incident considering
Python is included in most UNIX systems and is embraced by open-source
communities.
