```sh
poetry run python lib/day4/main.py data/day4/input.txt
```

```sh
poetry run python lib/day4/main.py data/day4/input.test.txt
```

### Notes on part 2 solution. 

The key to solving this problem is to keep track of the number of duplicates.

I conceptualised the duplicates as a grid that keeps track of the number of cards. First, add all the cards as count 1; these are the originals. Next, add the copies from card 1. Card 1 has four copies (cards 2-5), so increment cards 2-5 by 1. Next, for card 2, card 2 has two copies (cards 3-4), so increment the count of cards 3 and 4. The count for these cards is 4 because there are 2 of each card, 3 and 4 plus 2 more incoming from the 2 card 2's in the hand (this is the step I have annotated in the grid).


<img src="https://github.com/jdockeray/advent-of-code-24/assets/2040040/8c1c5819-f836-4edb-9805-57c3ed471db5" style="width: 50%;" alt="Image">
