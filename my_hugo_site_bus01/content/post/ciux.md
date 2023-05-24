---
title: "CI and UX Tests"
date: 2023-04-04T09:28:12+01:00
draft: true
---

## Testing

The importance of CI (Continuous Integration) and UX (User Experience) testing lies in ensuring the quality, reliability, and usability of your code. These tests help you identify and fix issues early in the development process, reducing the risk of introducing bugs or usability problems in the final product.

### UX testing

In this section, we'll perform User Experience (UX) testing using Python, pytest, and selenium.

1. Open the command prompt and navigate to the website folder using `cd ...`.
2. Install necessary packages:

```
pip install pytest
```

```
pip install selenium
```

1. Navigate to the `\tests\ux` folder using `cd ...`.
2. Create a virtual environment and activate it:

```
python -m venv .venv
```

```
.venv\Scripts\activate
```

1. Install the required packages from `requirements.txt`:

```
pip install -r .\requirements.txt
```

1. Run the tests using pytest and provide the URL as an argument:

```
pytest --url <localhost-url>
```

```
pytest --url <website-url>
```

Note: Make sure the URL contains 'http' at the beginning as it's the protocol the browser uses to communicate.

### CI testing

In this section, we'll perform Continuous Integration (CI) testing using Python, pytest, flake8, pylint, and pymarkdown.

1. Navigate to the folder containing tests.
2. Ensure the testing file name (`.py`) begins with 'test\_'.
3. In PowerShell terminal, create a virtual environment and activate it:

```
python -m venv .venv
```

```
..venv\Scripts\activate
```

4. Install the required packages from `requirements.txt`:

```
pip install -r .\requirements.txt
```

5. Run the tests using pytest:

```
pytest
```

This returns a list of failed tests. Search through pytest failures individually.

## Handling Linter and Markdown Errors

When encountering issues with linting or Markdown errors, you can follow these steps:

1. **Search through pytest failures individually**: Go through the test results to find the specific failures and errors.
2. **Search in .py files for each type of test in the CI folder**: Look for relevant flags or settings that might be causing the issue.

#### Ignoring Linter Rules

To ignore specific linter rules in your code:

- For flake8, add a comment with `# noqa: <lint rule id>` to the line you want to ignore.
- For pylint, add a comment with `# pylint: disable=<lint rule id>` to the line you want to ignore.

#### Fixing Linter Errors

To fix flake8 and pylint errors, run the following command:

```
flake8 "../..\tests\ux\<failed-file>" --isolated --max-complexity 10
```

```
pylint <filepath> --persistent=n --score=y
```

#### Fixing Markdown Errors

To fix Markdown errors using pymarkdown, run the following command:

```
pymarkdown -d heading-style,blanks-around-headings scan "<filepath>"
```
