def convert(my_name):
    """
    Print a line about converting a notebook.
    Args:
        my_name (str): person's name
    Returns:
        None

    """
    if not isinstance(my_name, str):
        raise TypeError("Please provide a string argument.")

    print(f"I'll convert a notebook for you some day, {my_name}.")
