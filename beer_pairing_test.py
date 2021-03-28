import beer_pairing
import unittest
from unittest import TestCase
from unittest import patch
import requests

class TestBeer(TestCase):

    @patch('beer_pairing.get_beer')
    def test_beer_api_response(self, mock_beer_api):
        mock_beer_api = requests.get('https://api.punkapi.com/v2/beers/1')
        #arrange
        
        #action 
        self.assertTrue(mock_beer_api.ok)
        #assert
        
    @patch('builtins.print')
    def test_display_beer(self, mock_print):
        beer_pairing.display_beer('Cowboy', 6.5, 'Delicious smooth taste', 'chicken' )
        mock_print.assert_called_once_with('Name of beer: Cowdboy', 'ABV: 6.5', 'Beer description: Delicious smooth taste', 'Pairs best with: chicken')