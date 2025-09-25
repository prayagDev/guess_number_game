from constants import LOSS_MSG, WIN_MSG, YES, NO
from validations import validate_number, validate_is_ready, validate_range
import random
from typing import Tuple, Dict, Union

def play_game(min_range: int, max_range: int, max_try: int = 5) -> str:
    
    number = random.randint(min_range, max_range)
    
    max_tried = 0
    
    guess_number = 0

    while max_tried < max_try and number!=guess_number:
        
        max_tried+=1
        
        guess_number = input("enter guess number: ")

        guess_number, is_valid = validate_number(number=guess_number)

        if is_valid:

            if number==guess_number:
                return WIN_MSG
            
    return LOSS_MSG

def validate() -> Tuple[Dict[str, Union[str, int]], int]:
    
    is_ready = input(f"Are you ready? {YES}/{NO}: ")

    is_ready, is_valid = validate_is_ready(is_ready=is_ready)

    if not is_valid:
        return {"detail": is_ready}, 400
    
    if not is_ready:
        return {"detail": is_ready}, 400

    print("Okay Great!\nNow lets select the start and end range below")

    min_range = input("Min Range: ")
    min_range, is_valid = validate_number(number=min_range)

    if not is_valid:
        return {"detail": min_range}, 400

    max_range = input("Max Range: ")
    max_range, is_valid = validate_number(number=max_range)

    if not is_valid:
        return {"detail": max_range}, 400

    valid_msg, is_valid = validate_range(min_range, max_range)

    if not is_valid:
        return {"detail": valid_msg}, 400
    
    return {"min_range": min_range, "max_range": max_range}, 200
    
if __name__ == "__main__":
    validated_data, status_code = validate()
    if status_code==200:
        result = play_game(**validated_data)
        print(result)
    else:
        print(validated_data)