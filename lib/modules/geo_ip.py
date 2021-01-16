from lib.settings import results_path

def geo_ip():
    from urllib.request import urlopen
    import json

    ct = 0

    path = results_path + 'ip-list.log'
    result_path = results_path + 'geo-ip.json'
    info = list()

    hand = open(path, 'rt')
    for line in hand:
        ip = line
        url = 'https://ipinfo.io/' + ip[:-1] + '/json'
        res = urlopen(url)
        data = json.load(res)
        info.append(data)
        ct = ct + 1
    with open(result_path, 'w+') as outfile:
        json.dump(info, outfile, sort_keys=True, indent=4)
    print('I\'ve made a total of ' + str(ct) + ' requests to https://ipinfo.io/ and wrote the raw json output into geo-ip.json in the results folder')
