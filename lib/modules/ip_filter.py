import re
from lib.settings import parsed_path


def ip_filter(filename2):
    filename = 'parsed-default-15-Jan-2021-07:07pm.log'
    path = parsed_path + filename
    pattern = 'Client ([0-9].+?) '

    hand = open(path, 'rt')


    for line in hand:
        line = line.rstrip()
        stuff = re.findall(pattern, line)
        ip = str(stuff)[2:-3]
        print('The IP is: ' + str(ip))
        if len(stuff) != 1 : continue

    print('done')