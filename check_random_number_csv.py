import time
import threading
from concurrent.futures import ThreadPoolExecutor
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import pdb
import sys
import json
import csv
import random
from random import randint
import phonenumbers

MAX_THREAD = 5
NUMBERS_COUNT = 115150
FILTERED_COUNTRIES = ["br","de","es","nl","mx","ng","th","az","sg","sa","om","bh","ae","kw","qa"]

ssuccess = 0


def format_number(number:str)->str:
    return f'{number}@c.us'


def lookup_numbers_parallel(driver, number_array):
    def check_number(number: str, country,mail):
        return number, (200 == driver.check_number_status(number).status)

    with ThreadPoolExecutor(max_workers=MAX_THREAD) as executor:
        # yield from executor.map(check_number, number_array)
        for number, status in executor.map(check_number, number_array):
            yield number, status
        

def lookup_numbers_sync(driver, number_array):
    for number in number_array:
        try:
            yield number, 200 == driver.check_number_status(number).status
        except Exception as e:
            print(f'error number {number!r}: {e}')


def lookup_numbers(number_array):
    driver = WhatsAPIDriver()
    print("Waiting for QR")
    driver.wait_for_login()

    print("Bot started")

    yield from lookup_numbers_sync(driver, number_array)

    print("done")
    driver.quit()

number_array = ['5511985730130@c.us']
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
first_digit = ['11','31','13','22','43','77','81','21','51','24']
for mciNumbers in range(0,100000):
    number_array.append('55' + random.choice(first_digit) + '9' + str(random_with_N_digits(8)) + '@c.us')
	# print('55'+str(random_with_N_digits(11)))

def main(numbers):
    #INPUT_PATH = r"C:\Users\Tzahi\Desktop\Phone to upload2.csv"
    OUTPUT_PATH = r"output3.csv"
    number_array = ['5511985730130@c.us']
    ssuccess = 0
    ffail = 0

    temp_arr = []
    for number in number_array:
        if number in numbers:
            continue
        else:
            temp_arr.append(number)
    number_array = temp_arr

    if len(number_array) == 0:
        print("empty number_array")
        return

    with open(OUTPUT_PATH, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number,status in lookup_numbers(number_array):
            if status:
                ssuccess +=1
            else:
                ffail = ffail + 1
            if ssuccess % 10 == 0:
                print("---------------")
                print("success:" + str(ssuccess))
                print("fail:" + str(ffail))
            writer.writerow([number,status])

numbers = {}
if __name__ == '__main__':
    main(numbers)
