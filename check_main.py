# import time
# import threading,time
# from webwhatsapi import WhatsAPIDriver
# from webwhatsapi.objects.message import Message
# import pdb
# import sys
# import json


# with open('data.json') as data_file:    
#     data = json.load(data_file)

# file = open("numbers9.txt","a")
# MAX_THREAD = 5
# def checknumber(phoneNumberStr):
#     # if (driver.check_number_status(phoneNumberStr + '@c.us').status == 200):
#     if (driver.check_number_status(phoneNumberStr).status == 200):
#         return True
#     else:
#         return False

# def createListOfNumbers(number):
#     rs = number + " " + str(checknumber(number))+"\n"
#     file.write(rs)

        

# def main():
#     number_array = []
#     for obj in data:
#         number = str(obj['number'])
#         number_array.append(f'{number}@c.us')
#         # number_array.append(f'97252{number}@c.us')
#     # arr1 = ["972528913345","972528913346","972528913347","972528913348"]
#     # for i in arr1:
#     #     number_array.append(str(i) + '@c.us')

#     print(number_array)
#     import ipdb; ipdb.set_trace()
#     print(number_array)

#     driver = WhatsAPIDriver()
#     print("Waiting for QR")
#     driver.wait_for_login()

#     print("Bot started")


#     threads = []

#     counter = 0
#     while counter < len(number_array):
#         if threading.active_count() > MAX_THREAD:
#             time.sleep(0.1)
#         else:
#             t = threading.Thread(target=createListOfNumbers,args=(number_array[counter],))
#             threads.append(t)
#             t.start()
#             counter += 1

#     print("done")
#     driver.quit()



# if __name__ == '__main__':
#     print('before main')
#     main()
#     print('after main')
# print('always no-main')
