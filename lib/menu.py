from lib.modules.log_parser import log_parser
from lib.modules.ip_filter import log_finder
from lib.modules.geo_ip import geo_ip
def menu():
    print('''
############################################################
##                                                        ##
##  What do you want to do?                               ##
##                                                        ##
##  1-> look for injection requests in your default.log   ##
##  2-> filter your results                               ##
##                                                        ##
############################################################''')
    #try:
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
        import os
        os.system('exit')
    elif response == 1:
        response = 0
        log_parser()
    elif response == 2:
        response = 0
        log_finder()
    elif response == 3:
        response = 0
        geo_ip()
    else:
        print('error invalid choice')
        return menu()

    #except:
     #   print('You need to chose a number')
      #  return menu()