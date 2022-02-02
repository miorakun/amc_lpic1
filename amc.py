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
