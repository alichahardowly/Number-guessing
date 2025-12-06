import random

class Error(Exception):
    pass

class NegativeValueError(Error):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

# رکوردها {'attempts': X, 'range': (min,max)}
records = []

def print_records():
    if not records:
        print("No records yet.")
        return
    print("\nLast 5 records:")
    for idx, rec in enumerate(records[-5:], start=1):
        print(f"{idx}. Range {rec['range'][0]}-{rec['range'][1]}, Attempts: {rec['attempts']}")
    print("")

print("Welcome to the Advanced Number Guessing Game!\n")

while True:
    # انتخاب سطح سختی
    print("Choose difficulty level:")
    print("1. Easy (0-10)")
    print("2. Medium (0-50)")
    print("3. Hard (0-100)")

    while True:
        level = input("Enter 1, 2, or 3 (or type End to exit): ")
        if level.lower() == "end":
            print("Game ended. Goodbye!")
            exit()
        if level not in ("1","2","3"):
            print("Invalid choice. Try again.")
            continue
        break

    if level == "1":
        min_num, max_num = 0, 10
    elif level == "2":
        min_num, max_num = 0, 50
    else:
        min_num, max_num = 0, 100

    number = random.randint(min_num, max_num)
    attempts = 0
    print(f"\nNew number has been generated! Range: {min_num}-{max_num}")

    while True:
        try:
            num = input('Enter a number or type End: ')

            if num.lower() == "end":
                print("Game ended. Goodbye!")
                exit()

            if not num.isdigit():
                print("Please enter a valid number.")
                continue

            num = int(num)
            attempts += 1

            if num < min_num:
                raise NegativeValueError
            elif num < number:
                raise ValueTooSmallError
            elif num > number:
                raise ValueTooLargeError
            else:
                print(f'\nCorrect! Your number is {num}')
                print(f'You guessed it in {attempts} attempts.')

                # ثبت رکورد
                records.append({'attempts': attempts, 'range': (min_num,max_num)})

                # نمایش رکوردها
                print_records()

                print('Starting next round...\n')
                break

        except NegativeValueError:
            print(f'This value is below the minimum ({min_num}), try again.')
        except ValueTooSmallError:
            print('Too small, try again.')
        except ValueTooLargeError:
            print('Too large, try again.')
        except Error:
            print("Please enter a valid number.")
