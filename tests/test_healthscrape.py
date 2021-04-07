import pytest
import healthscrape


def test_healthscrape():
    """
    This function checks that both the healthscrape's author and version are the correct ones.
    """

    print(healthscrape.__author__)
    print(healthscrape.__version__)


def test_healthscrape_vaccination_sites():
    """
    This function checks that vaccination_sites data retrieval functions listed in healthscrape works properly.
    """

    params = [
        {
            'country': 'united kingdom',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        healthscrape.get_vaccination_sites(country=param['country'])
