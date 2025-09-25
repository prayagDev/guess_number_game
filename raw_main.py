from constants import YES, NO
from validations import validate_number, validate_is_ready, validate_range
import random

print("Welcome to the Number Guessing Game!")

is_ready = input(f"Are you ready? {YES}/{NO}: ")

is_ready, is_valid = validate_is_ready(is_ready=is_ready)

if is_valid:

    if is_ready:

        print("Okay Great!\nNow lets select the start and end range below")

        min_range = input("Min Range: ")
        min_range, is_valid = validate_number(number=min_range)

        if is_valid:

            max_range = input("Max Range: ")
            max_range, is_valid = validate_number(number=max_range)

            if is_valid:
                valid_msg, is_valid = validate_range(min_range, max_range)

                if is_valid:

                    number = random.randint(min_range, max_range)
                    try_count = 5
                    tried_count = 0
                    guess_number = 0

                    while tried_count < try_count and number!=guess_number:
                        tried_count+=1
                        guess_number = input("enter guess number: ")

                        guess_number, is_valid = validate_number(number=guess_number)

                        if is_valid:

                            if number==guess_number:
                                print("Congrats! You Won.")
                            
                    else:
                        print("Max Retries exceeded! Sorry.")
                
                else:
                    print(valid_msg)
            
            else:
                print(max_range)
        
        else:
            print(min_range)
    
    else:
        print("ok bye!")

else:
    print(is_ready)