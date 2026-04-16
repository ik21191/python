import logging
import sys
from python_demo.utils import utils

def main():
    # Configure root logger with handlers
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("python_demo.log"),
        logging.StreamHandler(sys.stdout)
    ]
    )
    logging.info("Application started")


    a = 100
    b = 100
    logging.info(f'Sum of {a} and {b} is {utils.sum(a, b)}')

    #dictionary example

    # Creating a dictionary representing a car
    car_info = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    if "brand" in car_info:
        #way 1
        logging.info(f'Fetching brand value {car_info["brand"]}')
        #way 2
        logging.info('Fetching brand value %s', car_info["brand"])
    else:
        logging.info(f'brand is not presenting card_info')


    car_list = [
        { "brand": "Ford", "model": "Mustang", "year": 1964},
        { "brand": "BMW", "model": "7 Series", "year": 1998}
    ]

    for car in car_list:
        logging.info(car)


if __name__ == "__main__":
    main()
