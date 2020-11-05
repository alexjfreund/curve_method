def validate_k(k_max):
    """
    Validates user input for the maximum k-value by checking that k_max is both
    an integer and within the range [3,24] inclusive.
    
    Parameters
    ----------
    k_max : int
        The maximum desired k-value.

    Raises
    ------
    ValueError
        If the given k_max does not pass validation.
    """
    # ensure that the given k-value is an integer
    if not isinstance(k_max, int):
        raise ValueError("Maximum k-value must be an integer.")
    # ensure that the given k-value is at least 3 and no more than 24
    if k_max < 3 or k_max > 24:
        raise ValueError("Maximum k-value must be within [3, 24].")
   
def validate_deg(deg):
    """
    Validates user input for the degree of a polynomial approximation function
    by checking that the degree is both an integer and within the range [1,6]
    inclusive.

    Parameters
    ----------
    deg : int
        The desired polynomial degree.

    Raises
    ------
    ValueError
        If the given degree does not pass validation.
    """
    # ensure that the given degree is an integer
    if not isinstance(deg, int):
        raise ValueError("Polynomial degree must be an integer.")
    # ensure that the given degree is at least 1 and no more than 6
    if deg < 1 or deg > 6:
        raise ValueError("Polynomial degree must be within the range [1,6].")
