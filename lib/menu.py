from lib.modules.log_parser import log_parser
from lib.modules.ip_filter import log_finder
def menu():
    print('''
############################################################
##                                                        ##
##  What do you want to do?                               ##
##                                                        ##
##  0-> Exit                                              ##
##  1-> look for injection requests in your default.log   ##
##  2-> filter your results                               ##
##                                                        ##
############################################################''')
    try:
        question = input('''
############################################################
##                                                        ##
##  What do you want to do? Chose a number!               ##
##                                                        ##
############################################################
INPUT: ''')
        response = int(question)
        if response == 0:
            print('''
############################################################
##                                                        ##
##                      GOOD BYE!                         ##
##                                                        ##
############################################################''')
        elif response == 1:
            response = 0
            log_parser()
        elif response == 2:
            response = 0
            log_finder()
        else:
            print('error invalid choice')
            return menu()

    except:
        print('You need to chose a number')
        return menu()