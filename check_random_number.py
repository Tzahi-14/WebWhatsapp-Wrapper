import time
import threading,time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import pdb
import sys
import random
from random import randint

file = open("numbers11.txt","a")
MAX_THREAD = 25
def checknumber(phoneNumberStr):
    # if (driver.check_number_status(phoneNumberStr + '@c.us').status == 200):
    if (driver.check_number_status(phoneNumberStr).status == 200):
        return True
    else:
        return False

def createListOfNumbers(number):
    country = str(number)[:2]
    rs = number + " " + str(checknumber(number)) + " " + country +"\n"

    file.write(rs)

        

number_array = []
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
first_digit_br = ['11','31','13','22','43','77','81','21','51','24']
first_digit_th = ['6','7','8','9']
first_digit_mx = ['55','81','33']
first_digit_kw = ['22','23','40','24','65','25','67','55']
first_digit_qa = ['33','44','55','66','77']

# first_digit_az = ['55','40','50','51','70','77']
# first_digit_om = ['55','40','50','51','70','77']
# second_digit_om = ['55','40','50','51','70','77']

for mciNumbers in range(0,100000):
    # number_array.append('55' + random.choice(first_digit_br) + '9' + str(random_with_N_digits(8)) + '@c.us')
    # number_array.append('659' + str(random_with_N_digits(7)) + '@c.us')
    # number_array.append('9665' + str(random_with_N_digits(8)) + '@c.us')
    
    number_array.append('52' + random.choice(first_digit_mx) + str(random_with_N_digits(8)) + '@c.us')
    number_array.append('3106' + str(random_with_N_digits(8)) + '@c.us')
    number_array.append('9715' + str(random_with_N_digits(8)) + '@c.us')
    # number_array.append('234' + str(random_with_N_digits(10)) + '@c.us')
    # number_array.append('66' + random.choice(first_digit_th) + str(random_with_N_digits(8)) + '@c.us')
    ## number_array.append('944' + random.choice(first_digit_az) + str(random_with_N_digits(7)) + '@c.us')

    # number_array.append('968' + '71' + str(random_with_N_digits(2)) + '72' + str(random_with_N_digits(2)) + '@c.us')
    # number_array.append('965' + random.choice(first_digit_kw) + str(random_with_N_digits(6)) + '@c.us')
    # number_array.append('974' + random.choice(first_digit_qa) + str(random_with_N_digits(6)) + '@c.us')
    # number_array.append('973' + str(random_with_N_digits(8)) + '@c.us')
    # number_array.append('656' + str(random_with_N_digits(7)) + '@c.us')
	# print('55'+str(random_with_N_digits(11)))

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")


threads = []

counter = 0
while counter < len(number_array):
    if threading.active_count() > MAX_THREAD:
        time.sleep(0.1)
    else:
        t = threading.Thread(target=createListOfNumbers,args=(number_array[counter],))
        threads.append(t)
        t.start()
        counter += 1

print("done")
driver.quit()


# from random import randint
# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)

# for mciNumbers in range(0,10):
# 	print('55'+str(random_with_N_digits(11)))

