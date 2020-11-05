# validate user input for the maximum k value
def validate_k(k_max):
    # ensure that the given k value is an integer
    if not isinstance(k_max, int):
        raise ValueError("Maximum k value must be an integer")
    # ensure that the given k value is at least 3 and no more than 24
    if k_max < 3 or k_max > 24:
        raise ValueError("Maximum k value must be within [3, 24]")

# validate user input for a polynomial degree        
def validate_deg(deg):
    # ensure that the given degree is an integer
    if not isinstance(deg, int):
        raise ValueError("Polynomial degree must be an integer")
    # ensure that the given degree is at least 1 and no more than 6
    if deg < 1 or deg > 6:
        raise ValueError("Polynomial degree must be within the range [1,6]")
