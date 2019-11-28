#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program accepts user address information

def mailing(name_one, address_one, city_one, province_one, postal_code_one):
    print(name_one)
    print(address_one)
    print(city_one, province_one, postal_code_one)


def main():
    while True:
        name = input("Enter the name of the receiver: ")
        address = input("Enter the address: ")
        city = input("Enter the city: ")
        province = input("Enter the province: ")
        postal_code = input("Enter the postal code: ")
        print()

        try:
            mailing(name, address, city, province, postal_code)
        except ValueError:
            print("Invalid Input")
            continue
        else:
            break


if __name__ == "__main__":
    main()
