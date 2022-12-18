import unittest
import random

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main

class TestStringMethods(unittest.IsolatedAsyncioTestCase):

    def get_random_wine() -> main.Wine:
        wine = main.Wine(fixed_acidity=random.uniform(0, 100),
            volatile_acidity=random.uniform(0, 100),
            citric_acid=random.uniform(0, 100),
            residual_sugar=random.uniform(0, 100),
            chlorides=random.uniform(0, 100),
            free_sulfur_dioxide=random.randrange(0, 100),
            total_sulfur_dioxide=random.randrange(0, 100),
            density=random.uniform(0, 100),
            ph=random.uniform(0, 14),
            sulphates=random.uniform(0, 100),
            alcohol=random.uniform(0, 100))
        
        return wine

    async def test_predict_quality_return_type(self):
        wine = TestStringMethods.get_random_wine()
        return_value = await main.predict_quality(wine=wine)

        self.assertIsInstance(return_value, int)

if __name__ == '__main__':
    unittest.main()