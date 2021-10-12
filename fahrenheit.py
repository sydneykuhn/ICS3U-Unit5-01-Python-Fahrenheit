#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program converts a temperature from celcius to farenheit


def calculate_farenheit():
    # calculate farenheit

    # input
    c_temp_as_string = input("Enter a temperature (°C) : ")

    # process
    try:
        c_temp = int(c_temp_as_string)
        f_temp = round((c_temp * 9 / 5) + 32, 2)

        # output
        print("{0}°C is equal to {1}°F".format(c_temp, f_temp))
    except Exception:
        print("Invalid number entered, please try again.")


def main():

    # this function just calls another function

    # call function
    calculate_farenheit()
    print("\nDone.")


if __name__ == "__main__":
    main()
