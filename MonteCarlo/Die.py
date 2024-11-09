import numpy as np
import pandas as pd

class Die:
    """
    Assign a die with faces and their weights for each face.
    Each face is distict and can be weighted to simulate a die. 
    Die to be rolled to produce outcomes based on given weights.

    Attributes:
        faces: An array of unique faces with symbols that may be all alphabetic or all numeric).
        weights: An array of weights for each face, default=1.
        _facesweights: A private DataFrame to store faces and weights.
    """
    def __init__(self, faces):
        """
        Initialize die with a set of faces.

        Parameters:
            faces:NumPy array of unique symbols that may be strings or numbers.
                Raises TypeError if not a NumPy array.
                Raises ValueError if faces are not unique.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("faces must be Numpy array.")
        if len(faces)!=len(set(faces)):
            raise ValueError("face values must be distint.")
        self.faces=faces
        self.weights = np.ones(len(faces))
        self._df=pd.DataFrame({'weights': self.weights}, index=self.faces)
        
    def change_weight(self, face, new_weight):
        """
        Change the weight of a certain face.

        Parameters:
            face: The face value whose weight to be changed.
            new_weight: The new weight for the specified face. Must be positive numeric value, including 0. Raises IndexError if face is not valid.
                        Raises TypeError if new_weights is non-numeric.
        
        Raises:
            IndexError: If face is not in the face value of die.
            TypeError: If new_weight is non-numeric.
        """
        if face not in self._df.index:
            raise IndexError("Your faces value is not your die.")
        try: 
            new_weight = float(new_weight)
            if new_weight<0:
                raise ValueError("weight must be positive number, including 0.")
        except ValueError:
            raise TypeError("weight must be numbers.")
        self._df.loc[face, 'weight'] = new_weight
    def roll(self, num_rolls=1):
        """
        Roll the die a given number of times.

        Parameters:num_rolls: The number of rolling the die(integer). Defaults=1.

        Returns:A list of outcomes from the rolls.
        """
        return self._df.sample(n=num_rolls, weights='weights', replace=True).index.tolist()
        
    def show(self):
        """
        Show the current state of the die(faces and weights).

        Returns:pd.DataFrame: the DataFrame containing faces and their weights.
        """
        return self._df.copy()
    