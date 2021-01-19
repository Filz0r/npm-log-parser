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
##  3-> Find out GeoIP information on these requests      ##
##  4-> Create a final result file from all the gathered  ##
##      information so far                                ##
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
<<<<<<< Updated upstream
        elif response == 1:
            response = 0
            log_parser()
        elif response == 2:
            response = 0
            log_finder()
        else:
            print('error invalid choice')
            return menu()
=======
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
    elif response == 4:
        response = 0
        result()
    else:
        print('error invalid choice')
        return menu()
>>>>>>> Stashed changes

    except:
        print('You need to chose a number')
        return menu()