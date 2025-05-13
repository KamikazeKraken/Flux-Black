from datetime import datetime


def current_year() -> str:
    """
    Returns the current year in string format.
    """
    return str(datetime.now().year)
