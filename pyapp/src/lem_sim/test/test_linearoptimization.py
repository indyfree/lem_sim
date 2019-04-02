import unittest
import numpy as np
from scipy.optimize import linprog


class LinearOptimizationTest(unittest.TestCase):

    def test_solve_problem(self):
        target_coefs = np.array([1, -2, -1, -3])
        constraint_coefs = np.array([[2, 1, 0, 0], [0, 0, 2, 3], [1, 3, 2, 1], [1, 1, 1, 1]])
        constraint_bounds = np.array([4, 9, 8, 5])
        result = linprog(target_coefs, A_ub=constraint_coefs, b_ub=constraint_bounds)

    def test_split_array(self):
        constraint_coefs = np.array([[2, 1, 0, 0], [0, 0, 2, 3], [1, 3, 2, 1], [1, 1, 1, 1]])
        splitted_constraint_coefs = np.split(constraint_coefs, 2, axis=1)
        array = np.array([[2, 1], [0, 0], [1, 3], [1, 1]])
        
        self.assertTrue(np.array_equal(splitted_constraint_coefs[0], array))


if __name__ == '__main__':
    unittest.main()