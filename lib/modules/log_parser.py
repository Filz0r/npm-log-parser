import re
import lib.settings as settings
import datetime
from lib.modules.ip_filter import ip_filter

def log_parser():
    ct = 0
    log_path = settings.log_path
    parsed_path = settings.parsed_path
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y-%I:%M%P")    

    pattern = 'GET http localhost-nginx-proxy-manager'

    public_ip = input('what is your public IP? ')

    hand = open(log_path + 'default.log', 'rt')
    parsed_log_file = 'parsed-default-' + timestamp + '.log'
    parsed_log = open(parsed_path + parsed_log_file, 'w+')

    for line in hand:
        line = line.rstrip()
        stuff = re.findall(pattern, line)
        if line.find(pattern) != -1 and line.find(public_ip) == -1:
            parsed_log.write(str(line + '\n'))
            ct = ct + 1
        if len(stuff) != 1 :
            continue
    print('done, found ' + str(ct) + ' results')
    
    question = input('Do you want me to filter the parsed logs? (y/n) ')
    try:
        reply = str(question)
        if reply.lower() == 'y':
            ip_filter(parsed_log_file)
        elif reply.lower() == 'n':
            print('Ok you can check the logs over at ' + parsed_path + parsed_log_file)
            from lib.menu import menu
            menu()
        else:
            print('invalid reply, quitting...')
    except:
        print('there was an error processing your reply :(')
        from lib.menu import menu
        menu()
