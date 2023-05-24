---
title: "Python Circle"
date: 2023-03-10T11:00:56Z
draft: true
---
### Circle Class

This code defines a `Circle` class which represents a circle with a given radius. The class contains methods for calculating the area and perimeter (circumference) of the circle, as well as a summary method to provide a formatted output of these values.

### Class Definition

```python
class Circle:
    '''Circle to represent circle'''
```

The class is named `Circle`, and its docstring briefly explains its purpose.

### Constructor

```python
def __init__(self, radius: float):
    '''Circle constructor'''
    if radius <= 0.0:
        raise ValueError('Radius must be greater than 0.0')
    self.radius = radius
```

The constructor takes a single argument, the radius, which should be a float. The radius value is checked to ensure it is greater than 0.0; if it's not, a `ValueError` is raised. The radius value is then assigned to the `self.radius` variable.

### Area Method

```python
def area(self):
    '''Area access method'''
    return math.pi*self.radius**2
```

The `area` method calculates and returns the area of the circle using the formula `area = π * r^2`.

### Perimeter Method

```python
def perimeter(self):
    return 2 * math.pi * self.radius
```

The `perimeter` method calculates and returns the perimeter (circumference) of the circle using the formula `perimeter = 2 * π * r`.

### Summary Method

```python
def summary(self):
    area2dp = round(self.area(), 2)
    perimeter2dp = round(self.perimeter(), 2)
    return f'The area is {area2dp} and the perimeter is {perimeter2dp}'
```

The `summary` method first calculates the area and perimeter of the circle and rounds the results to 2 decimal places. It then returns a formatted string containing these values.
