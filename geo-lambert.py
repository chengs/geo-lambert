from __future__ import print_function


def _docstring_example(x, y):
    """
    This is an example of Google style.

    Args:
        x: This is the first param.
        y: This is a second param.

    Returns:
        This is a description of what is returned.

    Raises:
        KeyError: Raises an exception.
    """


def _check_input(x, y):
    if isinstance(x, int):
        x = x * 1.0
    if isinstance(y, int):
        y = y * 1.0

    assert isinstance(x, float)
    assert isinstance(y, float)

    return x, y


def lambert93_to_wgs84(x, y):
    # type (float, float) -> (float, float)
    """
    Covert a corrdinate (x,y) from Lambert 93 to WGS84 (lon/lat in radius).

    Args:
        x (float): easting
        y (float): northing 

    Returns:
        lat, lon (float, float): WGS84 corrdinate in radius
        
    >>> lambert93_to_wgs84(668832.5384, 6950138.7285)
    (2.5686536, 49.6496110)
    >>> lambert93_to_wgs84(668850, 6950151)
    (2.5688944, 49.6497221)
    """
    _x, _y = _check_input(x, y)
    # TODO: compute lon lat
    lat = 0.
    lon = 0.
    return lon, lat

def lambertIIe_to_wgs84(x, y):
    # type (float, float) -> (float, float)
    """
    Covert a corrdinate (x,y) from Lambert II etendu to WGS84 (lon/lat in radius).

    Args:
        x (float): Easting
        y (float): Northing 

    Returns:
        lat, lon (float, float): WGS84 corrdinate in radius

    >>> lambertIIe_to_wgs84(369419.0, 1986498)
    (-0.5791343, 44.8407050)
    >>> lambertIIe_to_wgs84(668850, 6950151)
    (6.6597230, 84.7306541)

    """
    _x, _y = _check_input(x, y)
    # TODO: compute lon lat
    lat = 0.
    lon = 0.
    return lon, lat

if __name__ == '__main__':
    import doctest
    doctest.testmod()