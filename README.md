# Advent of Code 2018

These are my solutions for the [2018 Advent of Code puzzles](https://adventofcode.com/2018). This is just a way for me
to practice python.

## Requirements

 1. Python 3
 
## Setup

None

## Running

Just use `python` to run the `aoc` module.

To run Day 1, Part 1 with the input I received:

```bash
$ python -m aoc 1 1
```

Or you can run it with any input file

```bash
$ python -m aoc 1 1 path/to/input/file.txt
```

Or you can run it with input directly as an argument

```bash
$ python -m aoc 1 1 abcdefg
```

## Notes

Within the comments of each file I'll be capturing some very simple notes about the algorithm and space/time complexity.
In any notes that reference Big O notation, `n` will always refer to the number of lines or items in the puzzle input,
unless otherwise noted.

### Puzzles

Here are my thoughts or lessons learned from the puzzles.

#### [Day 1](https://adventofcode.com/2018/day/1)

Looking back, I could have used a `deque` for part 2 instead of the circular iterator, but oh well.

#### [Day 2](https://adventofcode.com/2018/day/2)

Key insight for part 2 was realizing the wildcard strategy could be use to detect an off-by-one difference in linear
time.

#### [Day 3](https://adventofcode.com/2018/day/3)

Not much to say here but `defaultdict` certainly made the grid management simple.

#### [Day 4](https://adventofcode.com/2018/day/4)

All the non-linear time complexity comes from sorting the notes chronologically. After that it's just state management
to loop over the records for the puzzle solutions.

#### [Day 5](https://adventofcode.com/2018/day/5)

I know that using cursors to traverse an iterable is not a very pythonic way to do things, but I couldn't see how else
to make my `react()` function work.

#### [Day 6](https://adventofcode.com/2018/day/6)

I really struggled with this one. I think I had four or five false starts. It was realizing how infinite region
detection should work that got me over the hurdle.

#### [Day 7](https://adventofcode.com/2018/day/7)

Oof, graph problems. Not my strong suit. I first tried to do this by just traversing the graph and kept getting bogged
down in implementation - too much state to manage. Once I decided to progressively destroy the graph things become much
easier to manage.

#### [Day 8](https://adventofcode.com/2018/day/8)

I was really happy when I solved this one. I spent about 20x as much time thinking about the problem than I did typing.
It's the algorithm in `parse_license()` that does all the real work. Such a simple implementation but it was difficult
for me to visualize quickly.

#### [Day 9](https://adventofcode.com/2018/day/9)

This puzzle screamed for a circular data structure and `deque` made this almost trivial.

#### [Day 10](https://adventofcode.com/2018/day/10)

Super neat puzzle idea - it never dawned on me that one of these would require human judgment to find the answer. I very
quickly realized that the initial positions of the points puts them tens-of-thousands of grid places away from each
other, and that printing every single iteration would be foolhardy. I eventually figured that the final output would
print within a standard terminal, which was a bit of a guess, but turned out to work very well.

This is also the first puzzle where there's effectively a separate code path just for the integration tests.

#### [Day 11](https://adventofcode.com/2018/day/11)

For part 2 I originally had a fairly brute-force solution that took a couple minutes to run. It gave the right answer
but I wasn't super happy and figured a better algorithm existed. After checking the Reddit thread I learned about
[summed-area tables](https://en.wikipedia.org/wiki/Summed-area_table) and re-wrote my solution with this new knowledge
in hand and the updated function completes in less than 10 seconds.

## Testing

There are both unit tests and integration tests, all of which require `pytest`.

The integration tests prove the full solutions using the sample input data provided by the puzzle descriptions, when
available.

To run:

```bash
# All tests
$ pytest

# Unit Tests
$ pytest tests/unit/

# Integration Tests
$ pytest tests/integration/

```
