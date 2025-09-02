def _convert(value):
    """
    Helper function to safely convert values to float or int if possible.
    Raises TypeError if conversion fails.
    """
    try:
        # Try converting to int if it’s an integer string
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return float(value)  # works for int, float, numeric strings like "3.5"
    except (ValueError, TypeError):
        raise TypeError(f"Invalid input: {value}. Must be a number or numeric string.")


def add(a, b):
    """Return sum of a and b with type safety."""
    a = _convert(a)
    b = _convert(b)
    return a + b


def sub(a, b):
    """Return difference of a and b with type safety."""
    a = _convert(a)
    b = _convert(b)
    return a - b
