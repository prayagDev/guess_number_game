from constants import YES, NO
from typing import Tuple, Union


def validate_is_ready(is_ready: str) -> Tuple[Union[int, str], bool]:
    if is_ready == YES:
        return 1, True
    elif is_ready == NO:
        return "ok bye!", False
    else:
        return "please provide yes or no", False


def validate_number(number: str) -> Tuple[Union[int, str], bool]:
    try:
        number = int(number)
        return number, True
    except Exception:
        return "please provide valid number", False


def validate_range(min_range: int, max_range: int) -> Tuple[str, bool]:
    if max_range <= min_range:
        return "please enter valid range", False
    else:
        return "", True

