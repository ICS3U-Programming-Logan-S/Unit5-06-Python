#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 26, 2022
# This program rounds decimals.

def round_decimal(decimal_round_to, decimal_num):

    multi_dec = decimal_num[0] * (10 ** decimal_round_to)
    multi_dec = multi_dec + 0.5
    multi_dec_int = int(multi_dec)
    multi_dec_final = multi_dec_int / (10 ** decimal_round_to)
    decimal_num[0] = float(multi_dec_final)


def main():
    user_number_array = []

    user_number = input("Enter a decimal:\n>")
    decimal_count = input("How many number would you like to round to?\n> ")
    try:
        user_num_float = float(user_number)
        decimal_count_int = int(decimal_count)
        user_number_array.append(user_num_float)
        round_decimal(decimal_count_int, user_number_array)
        print(user_number_array[0])
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
