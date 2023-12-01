```
### Activates the virtual environment
poetry shell
```

```
### install dependencies
poetry install
```

```
### Run a day
poetry run python lib/day1/main.py
```

### Install pre-commit hooks
Docs here https://pre-commit.com/

```
pre-commit install
pre-commit install --hook-type commit-msg
```

It's important that you run pre-commit install --hook-type commit-msg, even if you've already used pre-commit install before. pre-commit install does not install commit-msg hooks by default!

### Commits
Commits should start with one of
