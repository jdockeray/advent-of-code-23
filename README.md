```
### Activates the virtual environment
poetry shell
```

```
### install dependencies
poetry install
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
```
fix, feat, chore, docs, style, refactor, perf, test
```

### Days

1. Day 1 - `iterator`
1. Day 2 - `tuples`, `collections`, `lamdas`
1. Day 3 - `matrices`, `tuples`, `loops`
1. Day 4 - `map`, `cache` (with notes)
1. Day 5 - `ranges`, `range splitting` (with notes)
1. Day 6 - 🚧 not attempted
1. Day 7 - `sort`, `logic elimination`
