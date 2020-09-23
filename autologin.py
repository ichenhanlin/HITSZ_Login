#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import math
import time
import json
import socket
import re

import config

# js2py files
from md5 import md5
from script import script
from sha1 import sha1
from b64encode import base64

# get the timestamp and the the length is 13
def timestamp():
    return int(round(time.time() * 1000))

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

CALLBACK = 'jQuery112402485404066979351_1600776710877'
IP = get_host_ip()
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

def getChallenge():
    params = {
        'callback': CALLBACK,
        'username' : USERNAME,
        'ip' : IP,
        '_': timestamp()
    }
    resp = requests.get('http://10.248.98.2/cgi-bin/get_challenge', params=params)
    if resp.status_code == 200:
        data = re.match(r'^jQuery.*\(({.*})\)$', resp.text).group(1)
        data = json.loads(data)
        return data['challenge']
    else:
        print('------------------[ERROR]------------------\n')
        print(resp.headers)
        exit(-1)

def login():
    def info(d, k):
        return "{SRBX1}" + base64._encode(script.xEncode(json.dumps(d), k))
    # prepare params
    enc = "srun_bx1"
    ac_id = '1'
    n = 200
    os = {
        'device': "Windows 10",
        'platform': 'Windows'
    }
    token = getChallenge()
    i = info({
        "username": USERNAME,
        "password": PASSWORD,
        'ip': IP,
        'acid': ac_id,
        'enc_ver':enc
    }, token)
    hmd5 = md5.md5(PASSWORD, token)
    chkstr = token + USERNAME
    chkstr += token + hmd5
    chkstr += token + ac_id;
    chkstr += token + IP
    chkstr += token + str(n);
    chkstr += token + '1';
    chkstr += token + i;
    params = {
        'callback': CALLBACK,
        'action': "login",
        'username': USERNAME,
        'password': "{MD5}"+hmd5,
        'ac_id': ac_id,
        'ip': IP,
        'chksum': sha1.sha1(chkstr),
        'info': i,
        'n': n,
        'type': 1,
        'os': 'Windows 10',
        'name': "Windows",
        'double_stack': 0,
        '_': timestamp()
    }
    resp = requests.get('http://10.248.98.2/cgi-bin/srun_portal', params=params)
    if resp.status_code == 200:
        data = re.match(r'^jQuery.*\(({.*})\)$', resp.text).group(1)
        data = json.loads(data)
        if(data['res'] != 'ok'):
            print(data['error_msg'])
    else:
        print('------------------[ERROR]------------------\n')
        print(resp.headers)
        exit(-1)

if __name__ == "__main__":
    login()
