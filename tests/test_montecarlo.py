#Unittest
import unittest
import numpy as np
from pandas import DataFrame
from MonteCarlo.Die import Die
from MonteCarlo.Game import Game
from MonteCarlo.Analyzer import Analyzer

class TestDie(unittest.TestCase):
    def setUp(self):
        """Set up a die with numeric faces for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(faces)

    def test_init(self):
        """Test if Die initializes with correct structure."""
        self.assertIsInstance(self.die._df, DataFrame)
        self.assertEqual(len(self.die._df), 6)
        
    def test_change_weight(self):
        """Test if changing weight updates the weight in the DataFrame."""
        self.die.change_weight(2, 3.5)
        self.assertEqual(self.die._df.at[2, 'weight'], 3.5)
        


    def test_roll(self):
        """Test if roll returns a list with correct number of elements."""
        rolls = self.die.roll(5)
        self.assertIsInstance(rolls, list)
        self.assertEqual(len(rolls), 5)

    def test_show(self):
        """Test if show returns a DataFrame copy."""
        df_copy = self.die.show()
        self.assertIsInstance(df_copy, DataFrame)
        self.assertEqual(len(df_copy), len(self.die._df))
        self.assertNotEqual(id(df_copy), id(self.die._df))  # Ensure it's a copy

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a game with two dice for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])

    def test_play(self):
        """Test if play stores results in a DataFrame with correct structure."""
        self.game.play(5)
        self.assertIsInstance(self.game._results_df, DataFrame)
        self.assertEqual(self.game._results_df.shape, (5, 2))  # 5 rolls, 2 dice

    def test_show_wide(self):
        """Test if show returns a wide DataFrame by default."""
        self.game.play(5)
        result_df = self.game.show()
        self.assertIsInstance(result_df, DataFrame)
        self.assertEqual(result_df.shape, (5, 2))  # 5 rolls, 2 dice

    def test_show_narrow(self):
        """Test if show returns a narrow DataFrame when specified."""
        self.game.play(5)
        narrow_df = self.game.show('narrow')
        self.assertIsInstance(narrow_df, DataFrame)
        self.assertEqual(narrow_df.index.names, ['roll_number', 'die_number'])
        self.assertEqual(narrow_df.shape, (10, 1))  # 5 rolls * 2 dice = 10 entries

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        """Set up an Analyzer with a Game object for testing."""
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        game = Game([die1, die2])
        game.play(10)
        self.analyzer = Analyzer(game)
    
    def test_analyzer_init_invalid_game(self):
        """Test if Analyzer raises ValueError when initialized with a non-Game object."""
        with self.assertRaises(ValueError):
            invalid_game = "not_a_game"  # Not a Game object
            Analyzer(invalid_game)

    
    def test_jackpot(self):
        """Test if jackpot returns an integer."""
        jackpot_count = self.analyzer.jackpot()
        self.assertIsInstance(jackpot_count, int)

    def test_face_counts_per_roll(self):
        """Test if face_counts_per_roll returns a DataFrame with correct structure."""
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertIsInstance(face_counts, DataFrame)
        self.assertEqual(face_counts.index.name, 'roll_number')

    def test_combo_count(self):
        """Test if combo_count returns a DataFrame with combinations and counts."""
        combo_counts = self.analyzer.combo_count()
        self.assertIsInstance(combo_counts, DataFrame)
        self.assertEqual(combo_counts.index.name, 'combination')
        self.assertIn('count', combo_counts.columns)

    def test_permutation_count(self):
        """Test if permutation_count returns a DataFrame with permutations and counts."""
        perm_counts = self.analyzer.permutation_count()
        self.assertIsInstance(perm_counts, DataFrame)
        self.assertEqual(perm_counts.index.name, 'permutation')
        self.assertIn('count', perm_counts.columns)

# Run the tests
if __name__ == '__main__':
    unittest.main()
