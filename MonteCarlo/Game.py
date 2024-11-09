import numpy as np
import pandas as pd
    
class Game:
    """
    Game consists of one or more rolls of similar dice (Die objects).
    
    Each game rolls a list of similar dice a given number of times and recording
    its results.

    Attributes:
        dice: list of Die objects representing the dice in the game.
        _results_df: Private DataFrame to store the results of the 
                                    most recent play.
    """
    def __init__(self, dice):
        """
        Initializes Game with die objects.

        Parameters:dice: list of die objects to play the game.
        """
        self.dice = dice
        self._results_df = None  # attribute to store the results of the most recent play
    def play(self, num_rolls):
        """
        Rolls each die in the game a given number of times.

        Parameters:
            num_rolls:Integer, the number of times to roll each die.
        
        Update:
            self._results_df: Stores the results of the rolls in a DataFrame, where
                              each row represents a roll and each column represents a die.
        """
        results = {}
        for i, die in enumerate(self.dice):
            results[i] = die.roll(num_rolls)  # Roll each die and store results with index as column name

        # Store the results into a DataFrame in wide format
        self._results_df = pd.DataFrame(results)
        self._results_df.index.name = 'roll_number'  # Name the index as 'roll_number'
    def show(self, form='wide'):
        """
        Show the results of the most recent play in the given format.

        Parameters:
            form:string,format of the results ('wide' or 'narrow'). Defaults='wide'.
                        Raises ValueError if form is invalid.

        Returns:DataFrame storing the results in the requested format.

        Raises: ValueError: If form is neither 'wide' nor 'narrow'.
        """
        if form == 'wide':
            return self._results_df.copy()
        elif form == 'narrow': # Convert to narrow format with MultiIndex (roll number and die number)
            narrow_df = self._results_df.stack().to_frame('outcome')
            narrow_df.index.names = ['roll_number', 'die_number']
            return narrow_df
        else:
            raise ValueError("Form must be either'wide' or 'narrow' only.")