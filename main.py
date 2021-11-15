#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon/Sep 13/2021
# This program is a simple calculator


def main():
    # This is the main function

    # Starting
    print("This is a simple calculator that calculates two numbers only.\n")

    # Input & Output & calculation
    try:
      counter_1 = int(input("Insert Number One: "))
      arithmetic = input("Insert (+ - x /): ")
      counter_2 = int(input("Insert Number Two: "))

      if arithmetic == "+" :
        process = (counter_1 + counter_2)
        print("\ncalculated number = ",process)
      elif arithmetic == "-" :
        process = (counter_1 - counter_2)
        print("\ncalculated number = ",process)
      elif arithmetic == "x" :
        process = (counter_1 * counter_2)
        print("\ncalculated number = ",process)
      elif arithmetic == "/" :
        process = (counter_1 / counter_2)
        print("\ncalculated number = ",process)

    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
