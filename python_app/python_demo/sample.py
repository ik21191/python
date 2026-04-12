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

if __name__ == "__main__":
    main()
