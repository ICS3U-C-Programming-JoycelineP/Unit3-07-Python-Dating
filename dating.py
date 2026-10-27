#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Oct 27 2026
# This program asks the age to the user and tell you if you can date my grand child

import constants


def main():
    # Get user_age from user as a string
    user_age_as_string = input("Enter your age: ")

    try:
        user_age_as_int = int(user_age_as_string)
        if user_age_as_int > constants.MIN_AGE and user_age_as_int < constants.MAX_AGE:
            print("You can date my grand child.")
        else:
            print(
                "You can not date my grand child. The correct age range is {} to {}.".format(
                    constants.MIN_AGE, constants.MAX_AGE
                )
            )

    except:
        print("{} is not a valid integer".format(user_age_as_string))

    finally:
        print("Thanks for your interest in my grand child!")


if __name__ == "__main__":
    main()
