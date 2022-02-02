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




def ch10():
    try:
        os.system("clear")
        ch10 = "welcome to challenge 10 \n The system on which you are working does not have the lsof command installed, and you are not allowed to install software without going through four levels of approval and scheduling the installation weeks in advance. However, the netstat command is available. Which option to netstat will show the process ID to which a given network port is connected?"
        print (ch10)

        ch10_ch10 = """
        A. ~/.ssh/authorized_keys
        B. ~/.ssh/keys
        C. ~/.ssh/keyauth
        D. ~/.sshd/authkeys
        """

        print (ch10_ch10)
        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "f1290186a5d0b1ceab27f4e77c0c5d68":
                    sleep(2)
                    print ("game over !")
                else :
                    sleep(2)
                    print ("winner")
                    print ("Congratulations my friend, I hope you are successful wherever you are ")

            if isd == "f1290186a5d0b1ceab27f4e77c0c5d68":
                sleep(2)
                print ("you win")
                break
    except:
        sleep(2)

        print ("please try again !")






def ch9():
    try:
        os.system("clear")
        ch9 = "welcome to challenge 9 \n Within which file should you place public keys for servers from which you will accept key-based ssh authentication?"
        print (ch9)

        ch9_ch9 = """
        A. ~/.ssh/authorized_keys
        B. ~/.ssh/keys
        C. ~/.ssh/keyauth
        D. ~/.sshd/authkeys
        """

        print (ch9_ch9)
        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "f1290186a5d0b1ceab27f4e77c0c5d68":
                    print ("game over !")
                else :
                    print ("winner")
                    ch10()
            if isd == "f1290186a5d0b1ceab27f4e77c0c5d68":
                print ("you win")
                ch10()
                break
    except:
        print ("please try again !")


def ch8():
    try:

        os.system("clear")
        ch8 = "welcome to challenge 8 \n You need to examine who is currently logged in to the system. Which of the following commands will display this information?"
        print (ch8)
        
        ch8_ch8 = """
        A. listuser
        B. fuser
        C. ls -u
        D. w
        """

        print (ch8_ch8)
        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "f1290186a5d0b1ceab27f4e77c0c5d68":
                    print ("game over !")
                else :
                    print ("winner")
                    ch9()
            if isd == "f1290186a5d0b1ceab27f4e77c0c5d68":
                print ("you win")
                ch9()
                break
    except:
        print ("please try again !")



def ch7():
    try:
        os.system("clear")
        ch7 = "welcome to challenge 7 \n In a scripting scenario, which command will return the domain name configured for the server?"
        print (ch7)
        ch7_ch7 = """
        A. dnsname
        B. fqdn
        C. hostname
        D. hostname -d
        """
        print (ch7_ch7)

        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "837ec5754f503cfaaee0929fd48974e7":
                    print ("game over !")
                else :
                    print ("winner")
                    ch8()
            if isd == "837ec5754f503cfaaee0929fd48974e7":
                print ("you win")
                ch8()
                break
    except:
        print ("please try again !")




def ch6():
    try:
        os.system("clear")
        ch5 = "welcome to challenge 6 \n Which of the following addresses represents the localhost in IPv6? (3)"
        print (ch5)
        ch5_ch5 = """
        A. 0:1
        B. ::1
        C. 127:0:1
        D. :127:0:0:1
        """
        print (ch5_ch5)

        for i in range(1,4):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "837ec5754f503cfaaee0929fd48974e7":
                    print ("game over !")
                else :
                    print ("winner")
                    ch7()
            if isd == "837ec5754f503cfaaee0929fd48974e7":
                print ("you win")
                ch7()
                break
    except:
        print ("please try again !")




def ch5():
    try:
        os.system("clear")
        ch5 = "welcome to challenge 5 \n Which of the following commands queries the mail servers for the domain example.com ? (5)"
        print (ch5)
        ch5_ch5 = """
        A. dig example.com mx
        B. dig example.com
        C. host -t smtp example.com
        D. dig example.com smtp
        """
        print (ch5_ch5)

        for i in range(1,6):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "c5a9b309744c165d140cb3d66a872da0":
                    print ("game over !")
                else :
                    print ("winner")
                    ch6()
            if isd == "c5a9b309744c165d140cb3d66a872da0":
                print ("you win")
                ch6()
                break
    except:
        print ("please try again !")



def ch4():
    try:
        os.system("clear")
        ch4 = "welcome to challenge 4 \n Which of the following commands queries the mail servers for the domain example.com ?"
        print (ch4)
        ch4_ch4 = """
        A. dig example.com mx
        B. dig example.com
        C. host -t smtp example.com
        D. dig example.com smtp
        """
        print (ch4_ch4)

        for i in range(1,5):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 4 :
                if isd != "c5a9b309744c165d140cb3d66a872da0":
                    print ("game over !")
                else :
                    print ("winner")
                    ch5()
            if isd == "c5a9b309744c165d140cb3d66a872da0":
                print ("you win")
                ch5()
                break
    except:
        print ("please try again !")



def ch3():
    try: 
        os.system("clear")
        ch3 = " welcome to challenge 3 \n Which command is used to format a swap partition?"
        print (ch3)
        ch3_ch3 = """
        A. mkfs -swap
        B. mkswap
        C. format -swap
        D. mksw
        """
        print (ch3_ch3)
        for i in range(1,4):
            isd = hashlib.md5(input("%i ~$" % i ).encode()).hexdigest()
            if i == 3 :
                if isd != "93939cfda4dbd38c5946fa40989c8c6c":
                    print ("game over !")
                
                else :
                    print ("winner")
                    ch4()

            if isd == "93939cfda4dbd38c5946fa40989c8c6c":
                print ("you win")
                ch4()
                break
    except:
        print("please try again !") 


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