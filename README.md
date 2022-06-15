# Test project to show GiHub Actions
## Prequisites
A python repository with name **test_package** must be created that contains a action with the following code

```python
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.10
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        pip install . # Install the package neede to run the tests
        python -m pytest # Dot the test
```
To create the above action on [github](https://github.com). Open a repository, use the Actions menu and chose the *Python Application*. Edit out the references to flake8 and press the **Start commit** button.

