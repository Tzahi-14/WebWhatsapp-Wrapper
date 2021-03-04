import time
import threading
from concurrent.futures import ThreadPoolExecutor
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import pdb
import sys
import json
import csv
import phonenumbers

MAX_THREAD = 5
NUMBERS_COUNT = 115150
FILTERED_COUNTRIES = ["br","de","es","nl","mx","ng","th","az","sg","sa","om","bh","ae","kw","qa"]

ssuccess = 0


def format_number(number:str)->str:
    return f'{number}@c.us'


def lookup_numbers_parallel(driver, number_array):
    def check_number(number: str, country,mail):
        return number, country,mail, (200 == driver.check_number_status(number).status)

    with ThreadPoolExecutor(max_workers=MAX_THREAD) as executor:
        # yield from executor.map(check_number, number_array)
        for number, country,mail, status in executor.map(check_number, number_array):
            yield number, country,mail, status
        

def lookup_numbers_sync(driver, number_array):
    for number, country,mail in number_array:
        try:
            yield number, country,mail, 200 == driver.check_number_status(number).status
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


def main(numbers):
    #INPUT_PATH = r"C:\Users\Tzahi\Desktop\Phone to upload2.csv"
    INPUT_PATH = r"C:\Users\Tzahi\Downloads\phones2.csv"
    OUTPUT_PATH = r"output2.csv"
    number_array = []
    ssuccess = 0
    ffail = 0

    with open(OUTPUT_PATH, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for i, row in enumerate(spamreader):
            numbers[row[0]] = bool(row[1])

    with open(INPUT_PATH, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for i, row in enumerate(spamreader):
            if len(number_array) > NUMBERS_COUNT:
                break
            try:
                number = row[2]
                country = row[1]
                mail = row[3]
                try:
                    parsed_number = phonenumbers.parse(number, country)
                    pnumber = str(parsed_number.country_code)+str(parsed_number.national_number)
                    if country.lower() in FILTERED_COUNTRIES:
                        number_info = (format_number(pnumber), country,mail)
                        number_array.append(number_info)
                except Exception as e:
                    print(f'error ({row!r}): {e}')
                    continue
                
            except Exception as e:
                print(f'encountered error [line {i+1}]: {e}')
    

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
        for number, country, mail,status in lookup_numbers(number_array):
            if status:
                ssuccess +=1
            else:
                ffail = ffail + 1
            if ssuccess % 10 == 0:
                print("---------------")
                print("success:" + str(ssuccess))
                print("fail:" + str(ffail))
                print(country)
            writer.writerow([number,status,country,mail])

numbers = {}
if __name__ == '__main__':
    main(numbers)
