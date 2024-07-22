"""Miscellaneous utility functions. Can duplicate the distutils.util functionality because it is deprecated."""


def strtobool(val: str | bool | None) -> bool:
    """Convert a string representation of truth to true or false.

    Notes:
        True values are True, 'y', 'yes', 't', 'true', 'on', and '1'; false values
        are False, None, 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
        'val' is anything else.

    Returns:
        bool: Boolean value.

    """
    if isinstance(val, bool):
        return val

    if val is None:
        return False

    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True

    if val in ("n", "no", "f", "false", "off", "0"):
        return False

    raise ValueError(f"invalid truth value {val}")
