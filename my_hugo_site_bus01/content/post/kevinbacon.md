---
title: "Kevin Bacon"
date: 2023-04-04T09:28:12+01:00
draft: true
---
## Six Degrees of Kevin Bacon

This code defines a `KevinBacon` class which calculates the "Six Degrees of Kevin Bacon" game. The class retrieves links from Wikipedia pages, starting from a given URL, and finds a chain of links to Kevin Bacon's page within six degrees.

### Class Definition

```python
class KevinBacon:
    """Six Degrees of Kevin Bacon Class"""
```

The class is named `KevinBacon`, and its docstring briefly explains its purpose.

### Class Variables

```python
urlLinks = []
```

The class variable `urlLinks` is a list that will store the Wikipedia URLs traversed in the search.

### Make Wikipedia URL Method

```python
def make_wikipedia_url(self, article_url: str) -> str:
    """Create Wikipedia compatible string"""
    return f'http://en.wikipedia.org{article_url}'
```

This method takes an `article_url` string and returns a full Wikipedia URL.

### Constructor

```python
def __init__(self, url: str):
    """Initialise class with starting url"""
    self.urlLinks.clear()
    self.url = url
    random.seed(int(round(datetime.datetime.now().timestamp())))
```

The constructor initializes the class with a starting URL and clears the `urlLinks` list. It also seeds the random number generator with the current timestamp.

### Get Links Method

```python
def get_links(self, article_url):
    """Get links from the wikipedia page"""
    ...
```

This method takes an `article_url` and returns a list of links found within the 'bodyContent' div of the Wikipedia page.

### Six Degrees Method

```python
def six_degrees(self) -> int:
    """six degrees mechanism"""
    ...
```

This method implements the "Six Degrees of Kevin Bacon" search mechanism. It retrieves links from the starting URL and continues traversing links until either a chain of 6 links is found or there are no more links to follow.

### As List Method

```python
def as_list(self):
    """Return Python List"""
    return self.urlLinks
```

This method returns the `urlLinks` list as a Python list.

### As JSON Method

```python
def as_json(self):
    """Return JSON List"""
    return json.dumps(self.urlLinks)
```

This method returns the `urlLinks` list as a JSON-formatted string.
