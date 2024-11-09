import numpy as np
import pandas as pd  
from MonteCarlo.Game import Game

class Analyzer:
    """
    Analyzes the results of a game, computing statistical properties about it.

    Attributes:
        game: The Game object to analyze its results.
        results: DataFrame containing the results of the most recent game.
    """
    def __init__(self, game):
        """
        Initializes the Analyzer with game object.

        Parameters:
            game: The Game object to analyze its results.
        """
        # Throws a ValueError if the passed value is not a Game object.
        if not isinstance(game, Game):
            raise ValueError("the passed value must be Game object.")
        
        self.game = game
        self.results = game.show('wide')  # the most results in wide format

    def jackpot(self):
        """
        Calculates the number of jackpot rolls, a result in which all faces are the same.

        Returns: Integer, the number of jackpots in game.
        """
        # Count rows where all values in a roll are the same
        jackpot_count = (self.results.nunique(axis=1) == 1).sum()
        return int(jackpot_count)

    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled in each event..

        Returns:DataFrame with an index of the roll number, 
            face values as columns, and count values in the cells 
        """
        # Count occurrences of each face for each roll
        face_counts = self.results.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        face_counts.index.name = 'roll_number'
        return face_counts

    def combo_count(self):
        """
        Calculates distinct combinations of faces rolled, along with their counts.
            order-independent and may contain repetitions.
        Returns:DataFrame with MultiIndex(combinations as index and counts as a single column).
        """
        # Find distinct combinations (order-independent) and their counts
        sorted_rolls = self.results.apply(lambda x: tuple(sorted(x)), axis=1)
        combo_counts = sorted_rolls.value_counts().to_frame('count')
        combo_counts.index.name = 'combination'
        return combo_counts

    def permutation_count(self):
        """
        Calculate distinct permutations of faces rolled, along with their counts,
            permutaton: order-dependent and may contain repetitions.

        Returns:DataFrame with MultiIndex(permutations as index and counts as a single column).
        """
        # Find distinct permutations (order-dependent) and their counts
        perm_counts = self.results.apply(tuple, axis=1).value_counts().to_frame('count')
        perm_counts.index.name = 'permutation'
        return perm_counts
