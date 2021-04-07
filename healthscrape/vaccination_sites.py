from .data.vaccination_sites_data import vaccination_sites_as_df


def get_vaccination_sites(country=None):
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

    return vaccination_sites_as_df(country)