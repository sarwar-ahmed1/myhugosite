---
title: "Hailstone"
date: 2023-04-04T09:28:12+01:00
draft: true
---
## Hailstone Sequence

This code defines a `Hailstone` class which represents a Hailstone sequence. The class takes a starting integer and calculates the Hailstone sequence using the following rules: if the current number is even, divide it by 2; if it's odd, multiply it by 3 and add 1. The sequence continues until it reaches 1.

### Class Definition

```python
class Hailstone:
    '''Class to represent Hailstone'''
```

The class is named `Hailstone`, and its docstring briefly explains its purpose.

### Constructor

```python
def __init__(self, starting: int):
    if starting <= 0:
        raise ValueError('starting number must be greater than 0')
    if not isinstance(starting, int):
        raise TypeError('starting number must be an integer')
    self.starting = starting
    self.numbers = [starting]
```

The constructor takes a single argument, the starting integer, which should be greater than 0. It raises a `ValueError` if the starting integer is less than or equal to 0, and a `TypeError` if the starting integer is not an integer. The starting integer is then assigned to the `self.starting` instance variable, and the `self.numbers` list is initialized with the starting integer as its first element.

### Hailstone Method

```python
def hailstone(self):
    '''function to represent Hailstone'''
    ...
```

This method calculates the Hailstone sequence starting from the given integer and returns the sequence as a list.

### Summary Method

```python
def summary(self):
    '''Class to represent summary'''
    hailstone_list = self.hailstone()
    no_of_steps = len(hailstone_list)
    return f'The list of Hailstone numbers is {hailstone_list}, \
            the number of steps taken is {no_of_steps}'
```

The `summary` method first calls the `hailstone()` method to obtain the Hailstone sequence list, calculates the number of steps taken, and returns a formatted string containing these values.

