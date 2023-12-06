```sh
poetry run python lib/day5/main.py data/day5/input.txt
```

```sh
poetry run python lib/day5/main.py data/day5/input.test.txt
```


### Notes on part 2 solution. 
There are two parts to the problem. The first is that, given we are now using ranges instead of int to determine the next state of the seed, it means that there can be leftovers. I found thinking about them as database joins helpful:

![image](https://github.com/jdockeray/advent-of-code-23/assets/2040040/840fbe4e-dc44-469d-bdde-db7643dc6fb6)

