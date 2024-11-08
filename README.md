# Monte-Carlo-Simulator
DS5100 project: Monte Carlo Simulator 

### Metadata
Project Name: Monte Carlo Simulator

Author: Heejeong Yoon (Angie): ID rpk3ve

### Synopsis
The Monte Carlo Simulator project includes three main classes—Die, Game, and Analyzer—which work together to simulate dice rolls, play games with multiple dice, and analyze game results.

### Installation

To install, clone the repository and navigate to the directory. Then run:
```bash
pip install -e .
```

### Usage Examples
1. Creating Dice

```python
import numpy as np
from MonteCarlo.Die import Die

# Create a 6-sided die with faces 1-6
faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)

# Roll the die 5 times
rolls = die.roll(5)
print("Rolls:", rolls)
```

2. Playing a Game
```python
from MonteCarlo.Game import Game

# Create a game with two dice
die1 = Die(faces)
die2 = Die(faces)
game = Game([die1, die2])

# Play the game with 10 rolls
game.play(10)
print("Game Results (Wide Format):")
print(game.show('wide'))
```

3. Analyzing a Game

```python
from MonteCarlo.Analyzer import Analyzer

# Create an analyzer for the game results
analyzer = Analyzer(game)

# Calculate the number of jackpots
jackpots = analyzer.jackpot()
print("Number of jackpots:", jackpots)

# Face counts per roll
print("Face Counts per Roll:")
print(analyzer.face_counts_per_roll())

# Combination counts
print("Combination Counts:")
print(analyzer.combo_count())

# Permutation counts
print("Permutation Counts:")
print(analyzer.permutation_count())
```

### API Description


### Die Class

The Die class represents a single die with a customizable number of faces and weights for each face.

- **`__init__(faces: np.ndarray)`**

  * Initializes the Die with a set of unique faces.
  * **Parameters**:
    * faces (np.ndarray): A NumPy array of unique symbols (strings or numbers).
  * **Raises**:
    * `TypeError` if `faces` is not a NumPy array.
    * `ValueError` if `faces` are not unique.
- `change_weight(face, new_weight)`
  * Changes the weight of a specific face.
  * **Parameters**:
    * `face`: The face value whose weight needs to be changed.
    * `new_weight`: A non-negative numeric weight.
  * **Raises**:
    * `IndexError` if `face` is not valid.
    * `TypeError` if `new_weight` is not numeric.
- `roll(num_rolls=1) -> list`
  * Rolls the die a specified number of times.
  * **Parameters**:
    * `num_rolls` (int): The number of rolls to perform. Default is 1.
  * **Returns**:
    * `list`: A list of rolled face values.
- `show() -> pd.DataFrame`
  * Displays the current state of the die (faces and weights).
  * **Returns**:
    * `pd.DataFrame`: A DataFrame with faces and their weights.

### Game Class

The Game class represents a game played with multiple dice.

- `__init__(dice: list)`
  * Initializes the Game with a list of `Die` objects.
  * **Parameters**:
    * `dice` (list): A list of Die objects to be used in the game.
- `play(num_rolls: int)`
  * Rolls each die a specified number of times.
  * **Parameters**:
    * `num_rolls` (int): The number of times each die should be rolled.
- `show(form='wide') -> pd.DataFrame`
  * Displays the results of the most recent play in wide or narrow format.
  * **Parameters**:
    * `form` (str): Format of the results (`'wide'` or `'narrow'`). Default is `'wide'`.
  * **Returns**:
   * `pd.DataFrame`: A DataFrame of the play results in the requested format.
  * **Raises**:
   * `ValueError` if form is not `'wide'` or `'narrow'`.


### Analyzer Class

The Analyzer class provides methods for analyzing the results of a game.

- `__init__(game: Game)`
  * Initializes the Analyzer with a `Game` object.
  * **Parameters**:
    * `game` (Game): A Game object whose results will be analyzed.
  * **Raises**:
    * `ValueError` if `game` is not a `Game` object.
- `jackpot() -> int`
  * Counts the number of jackpots (rolls with all faces the same).
  * **Returns**:
    * `int`: The number of jackpots in the game.
- `face_counts_per_roll() -> pd.DataFrame`
  * Computes the count of each face for each roll.
  * **Returns**:
    * `pd.DataFrame`: A DataFrame with counts of each face per roll.
- `combo_count() -> pd.DataFrame`
  * Calculates distinct combinations of faces rolled (order-independent).
  * **Returns**:
    * `pd.DataFrame`: A DataFrame with combinations as index and counts as a single column.
- `permutation_count() -> pd.DataFrame`
  * Calculates distinct permutations of faces rolled (order-dependent).
  * **Returns**:
    * `pd.DataFrame`: A DataFrame with permutations as index and counts as a single column.
