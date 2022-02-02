import random 
import os
import hashlib 
from time import sleep

global md5
global ch3_ch3 
global ch4_ch4
global ch5_ch5
global ch6_ch6
global ch7_ch7
global ch8_ch8
global ch9_ch9
global ch10_ch10


# define for start write chalenges func name is start
def start(): # start function
    # try except for err handleing
    try:
        print("hello my friend this is amicheh's game you havehere for learning ")
        na = input("enter your name ~$")
        os.system("clear")
        print("hello my friend this is amicheh's game you have here for learning ")
        print ("In the first $amc1304$ challenge of 2022 you have to understand lpic1 you will have 10 questions and you will get a score at the end")
        st = input("are you redy? [Y/n]")
        if st == "y":
            os.system("clear")
            print ("welcome to amc1304")
            print ("theme is Company")
            print ("%s You are employed by a company and you have to meet their demands" % na)
            ch1()
    except:
        print ("please run again")



def ch2():
    try:
        os.system("clear")
        ch2 = "welcome to challenge 2 \nIn a company you have to get the path of all the files with pdf extension and type the command (4)"
        print (ch2)
        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "093906c48bcc2e585f54bed709f22222":
                    print ("game over !")

                else :
                    print ("winner")
                    ch3()
            if isd == "093906c48bcc2e585f54bed709f22222":
                print ("you win")
                ch3()
                break
    except:
        print ("please try again !")



def ch1():
    # try except for erro handling
    try:
        os.system("clear")
        # ch1 set quastion
        ch1 = "welcome to challenge 1 \n You are asked to list all the kernel modules and show them to the client # chance number (3)"
        print (ch1)
        # for loop and range chancess
        for i in range(1,4):
            # isd var is input client hash
            isd =  hashlib.md5(input("%i ~$" % i).encode()).hexdigest()
            # if i chance == 3 chance and isd != hash you are game over
            if i == 3 :
                if isd != "e44d12d4c5d06e7acfb04b826da858bd":
                    print ("game over !")
                # else you win
                else :
                    print ("winer")
                    ch2()
            # if you win programm is break
            if isd == "e44d12d4c5d06e7acfb04b826da858bd":
                print ("you win")
                ch2()
    except:
        print ("please try again")

start()