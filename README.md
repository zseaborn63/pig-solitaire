# Pig Solitaire

## Description

Use Object Oriented concepts to implement a game of Pig Solitaire

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Modeling games
* Classes
* Object Oriented concepts

### Performance Objectives

After completing this assignment, you should be able to:

* Play Pig well
* Use Classes
* Use subclasses

## Details

### Deliverables

* A Git repo called pig-solitaire containing at least:
  * a pig.py file containing your game
  * a `requirements.txt` file

### Requirements

* A game that plays Pig Solitaire

## The Rules of Pig Solitaire

In 7 turns, you are attempting to get the highest score possible.

Each turn, you have two choices:

* __Roll__. Roll a six-sided die. If it comes up one, your turn is over and you add nothing to your score. If it comes up two through six, you add that number to your turn total and choose again.
* __Hold__. If you hold, you add the turn total to your score.

An example:

> The first turn, I roll a 1 immediately. I receive no points.

> The second turn, I roll a 5. I choose to roll again. I roll a 3, for a turn total of 8. I choose to roll again. I roll a 3, for a turn total of 11. I hold, receiving 11 points. My score is 11.

> The third turn, I roll a 5 again. I choose to roll again. I roll a 6, for a turn total of 11. I choose to roll again. I roll a 4, for a turn total of 15. I decide to roll once more. I roll a 6, for a turn total of 21. I hold, receiving 21 points. My score is 32.

> The fourth turn, I roll a 6. I choose to roll again. I roll a 3, for a turn total of 9. I choose to roll again. I roll a 3, for a turn total of 12. I choose to roll again. I roll a 4, for a turn total of 16. I hold, receiving 16 points. My score is 48.

> The fifth turn, I roll a 6. I choose to roll again. I roll a 6, for a turn total of 12. I choose to roll again. I roll a 3, for a turn total of 15. I choose to roll again. I roll a 4, for a turn total of 19. I choose to roll again. I roll a 6, for a turn total of 25. I hold, receiving 25 points. My score is 73.

> The sixth turn, I roll a 6. I choose to roll again. I roll a 1, and receive no points.

> The seventh turn, I roll a 5. I choose to roll again. I roll a 1, and receive no points.

> My final score is 73.

## Normal Mode

Create a game of Pig Solitaire to the above specifications that allows a user to play against a computer opponent.

A hard requirement of this is that you use classes and explore the concept of `class inheritance`.  This will allow
you to more flexibly create AI opponents with different game strategies.

## Hard Mode

In addition to the requirements from **Normal Mode**:

Once you have your optimal Pig Solitaire player, create a second pig solitaire game. This could be in a separate `.py` or
the same one. The difference with this mode is that you are playing to a score of 100 points. There is no round limit.

## Additional Resources

* [Classes in the Python documentation](https://docs.python.org/3/tutorial/classes.html#class-objects)
* [SOLID principles](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design))
