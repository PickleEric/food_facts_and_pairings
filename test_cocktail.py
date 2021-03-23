import unittest
from unittest.mock import patch 

import cocktail_api_setup

class TestCocktailAPI(unittest.TestCase):

    @patch('cocktail_api_setup.make_cocktail_api_request', return_value={  })   # fill in example response
    def test_get_cocktail_info(self, mock_api_call):
        self.assertIsNone(cocktail_api_setup.getcockaildrink('cheese'))
