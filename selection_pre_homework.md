#Reading and Research - Selection Statements

These tasks are designed to introduce you to the programming topic we will be studying in class next lesson. You **must** complete these activities prior to the lesson.

##Boolean Expressions
One of the most common tasks in computer programming is to **evaluate an expression**. An expression allows us to test whether a value (or set of values) meets particular criteria. The Python shell can evaluate expressions, we will use this to investigate expressions further.

###Task 1
Use the Python shell to investigate the expressions given below, describe what each symbol represents and indicate whether the expression evaluates to `True` or `False`.

![](https://www.dropbox.com/s/2yaariz84s3kf5z/task_one.jpg?dl=1)

|Expression|Symbol description|Result|
|:--------:|------------------|------|
|`2 == 4`|*equals*|`False`|
|`5 > 3`| | |
|`4 >= 4`| | |
|`3 < 2`| | |
|`7 <= 7`| | |
|`8 != 9`| | |

The symbols in **Task 1** are called **relational operators** and when an expression containing a relational operator is evaluated it returns a **boolean value** (True or False) as an answer.


In addition to evaluating expressions containing numbers we can also use **variables** in expressions. For example, imagine we had the following variable:

```python
test_score = 56
```

We could use boolean expressions to evaluate whether testScore meets certain criteria (for example whether it is greater than the pass mark of 50). Let’s test this out:

###Task 2
Enter `testScore = 56` into the Python shell and then investigate the expressions below.

![](https://www.dropbox.com/s/9mh1ob3uxqdhvz0/task_two.png?dl=1)


|Expression|Symbol description|Result|
|:--------:|------------------|------|
|`test_score == 50`|*equals*|`False`|
|`test_score > 40`| | |
|`test_score >= 60`| | |
|`test_score < 40`| | |
|`50 <= test_score`| | |
|`56 != test_score`| | |

##More complex boolean expressions
Sometimes it is not enough to evaluate an expression on a single criteria. We can create more complicated boolean expressions using boolean operators. There are three boolean operators that we must consider in programming:

|Operator|
|:------:|
|`and`|
|`or`|
|`not`|

The `and` and `or` operators can be used to join expressions together into more complex expressions. The `not` operator is used to invert an expressions evaluation. For example if an expression evaluated to `True` using the `not` operator would make the result equal `False`.

###Task 3
Let’s look at some straightforward examples. Use the Python shell to evaluate the following expressions:

|Expression|Result|
|:--------:|------|
|`True and True`|`True`|
|`True and False`| |
|`False and True`| |
|`False and False`| |
|`True or True`| |
|`True or False`| |
|`False or True`| |
|`False or False`| |
|`not(True)`| |
|`not(False)`| |

Having completed the above table, use the space below to describe when `and` and `or` evaluate to `True`:

|Operator|When it evaluates to `True`|
|:------:|---------------------------|
|`and`| |
|`or`| |

##Selection statements
Before we find out more about selection statements let look at an example:

```python
test_score = 56
if test_score >= 50:
    print("Pass")
if test_score < 50:
    print("Fail")
```

###Task 4
Without entering the code into Python, attempt to explain what the code does, using the space below for your answer:

|answer|
|------|
| |

Now that we have looked at an example it is time to investigate selection statements in more detail. We will use the  [Python School website](http://www.pythonschool.net) to do this.

###Task 5
Read the following two pages on Python Summer School and attempt the exercises mentioned.

1. [The IF Statement in Python](http://pythonschool.github.io/basics/the-if-statement/)
    - The exercise at the bottom of the page
2. [More on IF Statements in Python](http://pythonschool.github.io/basics/more-on-if/)
    - The **first** exercise at the bottom of the page

###Task 6
In the space below **paste** the code from each of the exercises in Task 5 and include a screenshot of you running each program successfully.

```python
#task 5.1
```

![Screenshot of task 5.1]()

```python
#task 5.2
```

![Screenshot of task 5.2]()

##Summary
In this R&R you have investigated selection statements. You have seen how expressions are constructed from relational operators and boolean operators. You have have seen the structure and syntax of a basic selection statement and had the opportunity to create programs that use this statement.

Please make sure you have completed this R&R fully before your next programming lesson as it will form the basis of the initial classroom discussion and starter tasks.