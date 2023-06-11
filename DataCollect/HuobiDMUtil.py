#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 20180917
# @Author  : zhaobo
# @github  : 

import base64
import hmac
import hashlib
import json

import urllib3
import datetime
import requests
#import urlparse   # urllib.parse in python 3
import aiohttp
import time

# timeout in 5 seconds:
TIMEOUT = 5

#各种请求,获取数据方式
async def aiohttp_get_request(url, params, add_to_headers=None):
    session = aiohttp.ClientSession()

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0 Chrome/39.0.2171.71'
    }
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'your bot 0.1'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = urllib3.parse.urlencode(params)
    try:
        #response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        response = await session.get(url,postdata, headers=headers, timeout=TIMEOUT)
        result = await response.text()
        if response.status_code == 200:
            return response.json()
        else:
            return {"status":"fail","status_code":response.status_code}
    except Exception as e:
        print("httpGet failed, detail is:%s" %e)
        return {"status":"fail","msg": "%s"%e}

#各种请求,获取数据方式
def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0 Chrome/39.0.2171.71'
    }
    # headers = {
    #     "Content-type": "application/x-www-form-urlencoded",
    #     'User-Agent': 'your bot 0.1'
    # }
    if add_to_headers:
        headers.update(add_to_headers)
    if params:
        postdata = urllib3.parse.urlencode(params)
    count = 0
    while count < 10:
        try:
            if params:
                response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
            else:
                response = requests.get(url, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status":"fail","status_code":response.status_code}
        except Exception as e:
            count += 1
            print("httpGet failed, detail is:%s" %e)
            time.sleep(5)
            #return {"status":"fail","msg": "%s"%e}

def http_tron_get_request(url, params, add_to_headers=None, _apikey=""):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "accept": "application/json",
        # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0 Chrome/39.0.2171.71',
        'User-TRON_PRO_API_KEY': _apikey
    }
    if add_to_headers:
        headers.update(add_to_headers)
    if params:
        postdata = urllib3.parse.urlencode(params)
    count = 0
    while count < 10:
        try:
            if params:
                response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
            else:
                response = requests.get(url, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status":"fail","status_code":response.status_code}
        except Exception as e:
            count += 1
            print("httpGet failed, detail is:%s" %e)
            time.sleep(5)
            #return {"status":"fail","msg": "%s"%e}


#add by xuj for https://api.yantoken.io
def http_get_request_yantoken(url, params, accessKey=None):
    headers = {
        "X-BH-APIKEY": accessKey,
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0 Chrome/39.0.2171.71'
    }
    postdata = urllib3.parse.urlencode(params)
    try:
        response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return {"status":"fail","status_code":response.status_code}
    except Exception as e:
        print("httpGet failed, detail is:%s" %e)
        return {"status":"fail","msg": "%s"%e}

def http_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = json.dumps(params)
    try:
        response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print("httpPost failed, detail is:%s" % e)
        return {"status":"fail","msg": "%s"%e}

async def aiohttp_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = json.dumps(params)
    try:
        session = aiohttp.ClientSession()
        #response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        response = await session.post(url, postdata, headers=headers, timeout=TIMEOUT)
        result = await response.text()
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print("httpPost failed, detail is:%s" % e)
        return {"status":"fail","msg": "%s"%e}

#add by xuj for https://api.yantoken.io
def http_post_request_temp(url, params, accessKey=None):
    headers = {
        "X-BH-APIKEY": accessKey,
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    postdata = json.dumps(params)
    try:
        response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print("httpPost failed, detail is:%s" % e)
        return {"status":"fail","msg": "%s"%e}


def api_key_get(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params.update({'AccessKeyId': ACCESS_KEY,
                   'SignatureMethod': 'HmacSHA256',
                   'SignatureVersion': '2',
                   'Timestamp': timestamp})

    host_url = url
    host_name = host_url
    #host_name = urlparse.urlparse(host_url).hostname
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()

    params['Signature'] = createSign(params, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path
    return http_get_request(url, params)

async def aioapi_key_get(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params.update({'AccessKeyId': ACCESS_KEY,
                   'SignatureMethod': 'HmacSHA256',
                   'SignatureVersion': '2',
                   'Timestamp': timestamp})

    host_url = url
    host_name = host_url
    #host_name = urlparse.urlparse(host_url).hostname
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()

    params['Signature'] = createSign(params, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path

    ## add by xuj
    session = aiohttp.ClientSession()

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0 Chrome/39.0.2171.71'
    }
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'your bot 0.1'
    }
    postdata = urllib3.parse.urlencode(params)
    try:
        #response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        response = await session.get(url,postdata, headers=headers, timeout=TIMEOUT)
        result = await response.text()
        if response.status_code == 200:
            return response.json()
        else:
            return {"status":"fail","status_code":response.status_code}
    except Exception as e:
        print("httpGet failed, detail is:%s" %e)
        return {"status":"fail","msg": "%s"%e}

    ## add by xuj end


def api_key_post(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': timestamp}

    host_url = url
    #host_name = urlparse.urlparse(host_url).hostname
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()
    params_to_sign['Signature'] = createSign(params_to_sign, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path + '?' + urllib3.parse.urlencode(params_to_sign)
    return http_post_request(url, params)

def aioapi_key_post(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': timestamp}

    host_url = url
    #host_name = urlparse.urlparse(host_url).hostname
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()
    params_to_sign['Signature'] = createSign(params_to_sign, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path + '?' + urllib3.parse.urlencode(params_to_sign)
    return aiohttp_post_request(url, params)

# add by xuj for https://api.yantoken.io/
def api_key_get_yantoken(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    tt = datetime.datetime.utcnow().timestamp()
    timestamp = int(round(tt * 1000))
    params.update({'recvWindow': 5000,
                   'timestamp': timestamp})

    host_url = url
    host_name = host_url
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()

    params['signature'] = createSign_yantoken(params, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path
    return http_get_request_yantoken(url, params,accessKey=ACCESS_KEY)

#add by xuj for  https://api.yantoken.io/
def api_key_post_temp(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    tt = datetime.datetime.utcnow().timestamp()
    timestamp = int(round(tt * 1000))


    params_to_sign = {
                      'recvWindow': 5000,
                      'timestamp': timestamp}

    host_url = url
    #host_name = urlparse.urlparse(host_url).hostname
    host_name = urllib3.parse.urlparse(host_url).hostname
    host_name = host_name.lower()
    params_to_sign['signature'] = createSign_yantoken(params_to_sign, method, host_name, request_path, SECRET_KEY)
    #add by xuj
    #params_to_sign['signature'] = "b72c290a2ea7db1499c152cd6a3a792052c01b4cd88d1897ea9f540443cfc5d4"
    url = host_url + request_path + '?' + urllib3.parse.urlencode(params_to_sign)
    return http_post_request_temp(url, params,accessKey=ACCESS_KEY)

def createSign(pParams, method, host_url, request_path, secret_key):
    sorted_params = sorted(pParams.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib3.parse.urlencode(sorted_params)
    payload = [method, host_url, request_path, encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = secret_key.encode(encoding='UTF8')
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    return signature

# add by xuj for https://api.yantoken.io/
def createSign_yantoken(pParams, method, host_url, request_path, secret_key):
    sorted_params = sorted(pParams.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib3.parse.urlencode(sorted_params)
    payload = [encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = secret_key.encode(encoding='UTF8')
    signature = hmac.new(secret_key, payload, digestmod=hashlib.sha256).hexdigest().lower()
    return signature

