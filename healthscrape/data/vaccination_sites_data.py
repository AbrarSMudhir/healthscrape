import pkg_resources
import pandas as pd

from unidecode import unidecode

from ..utils import constant as cst


def vaccination_sites_as_df(country=None):
    """
    This function retrieves all the vaccination sites data stored in `vaccination_sites.csv` file.

    Args:
        country (:obj:`str`, optional): name of the country
    Returns:
        :obj:`pandas.DataFrame` - vaccination_sites_df:
            The resulting :obj:`pandas.DataFrame` contains all the vaccination sites data
            retrieved by healthscrape and stored on a csv file.
            So on, the resulting :obj:`pandas.DataFrame` will look like::
                country | region | body | trust_or_site_name | address | postcode
                --------|--------|------|--------------------|---------|---------
                xxxxxxx | xxxxxx | xxxx | xxxxxxxxxxxxxxxxxx | xxxxxxx | xxxxxxxx
    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
        FileNotFoundError: raised if `vaccination_sites.csv` file was not found.
        IOError: raised when `vaccination_sites.csv` file is missing or empty.
    """

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0001: specified country value not valid.")

    resource_package = 'healthscrape'
    resource_path = '/'.join(('resources', 'vaccination_sites.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        vaccination_sites = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0002: vaccination_sites file not found or errored.")

    if vaccination_sites is None:
        raise IOError("ERR#0003: vaccination_sites list not found or unable to retrieve.")

    vaccination_sites = vaccination_sites.where(pd.notnull(vaccination_sites), None)

    if country is None:
        vaccination_sites.reset_index(drop=True, inplace=True)
        return vaccination_sites
    else:
        country = unidecode(country.strip().lower())

        if country not in vaccination_sites_countries_as_list():
            raise ValueError("ERR#0004: country " + country + " not found, check if it is correct.")

        vaccination_sites = vaccination_sites[vaccination_sites['country'] == country]
        vaccination_sites.reset_index(drop=True, inplace=True)

        return vaccination_sites


def vaccination_sites_countries_as_list():
    """
    This function returns a listing with all the available countries.
    Returns:
        :obj:`list` - countries:
            The resulting :obj:`list` contains all the available countries with vaccination sites

    """

    return list(cst.COUNTRIES.keys())
