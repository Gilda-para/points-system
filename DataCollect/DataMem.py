#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""

"""
import time
import redis
import json
import glob
import configparser

#get the config file content
currencys = 'currencys'
tickers = 'tickers'
huobi_kline_1m = 'huobi_kline_1m'
huobi_kline_15m = 'huobi_kline_15m'
huobi_kline_1d = 'huobi_kline_1d'
order_detail = 'order_detail'
flag = 'flag'
depth0 = 'depth0'
ACC_BALANCE = 'ACC_BALANCE'
OBJ_INVENTORY = 'OBJ_INVENTORY'
OBJ_ACCOUNT = 'OBJ_ACCOUNT'
OBJ_PROFIT = 'OBJ_PROFIT'

#end
#init the mem of redis
__r = redis.Redis(host='localhost',port=6379,db=1)

def setTickers(entity=''):
    __r.set(tickers, json.dumps(entity))

def getTickers():
    tmpReturn = json.loads(__r.get(tickers))
    return tmpReturn

def setCurrencys(entity=''):
    __r.set(currencys, json.dumps(entity))

def getCurrencys():
    tmpReturn = json.loads(__r.get(currencys))
    return tmpReturn

def setKline_15m(entity=''):
    __r.set(huobi_kline_15m, json.dumps(entity))

def getKline_15m():
    tmpReturn = json.loads(__r.get(huobi_kline_15m))
    return tmpReturn

def setKline_1m(entity=''):
    __r.set(huobi_kline_1m, json.dumps(entity))

def getKline_1m():
    tmpReturn = json.loads(__r.get(huobi_kline_1m))
    return tmpReturn

def getflag():
    tmpReturn=str(__r.get(flag))
    return tmpReturn

def setOrderdetail(entity=''):
    json_entity=json.dumps(entity)
    __r.set(order_detail, json_entity)

def getOrderdetail():
    tmpReturn=str(__r.get(order_detail))
    return tmpReturn

def setKline1day(entity=''):
    __r.set(huobi_kline_1d, json.dumps(entity))
    #print("huobi_kline_1d key: ",huobi_kline_1d)

def getKline1day():
    tmpReturn=json.loads(__r.get(huobi_kline_1d))
    return tmpReturn

def getDepth_step0():
    tmpReturn=json.loads(__r.get(depth0))
    return tmpReturn

def setDepth_step0(entity=''):
    __r.set(depth0, json.dumps(entity))


def getBalance():
    tmpReturn=json.loads(__r.get(ACC_BALANCE))
    return tmpReturn

def setBalance(entity=''):
    __r.set(ACC_BALANCE, json.dumps(entity))

def getTmp(tmp='tmp'):
    tmpReturn=''
    if __r.exists(tmp):
        tmpReturn=json.loads(__r.get(tmp))
    return tmpReturn

def setTmp(key='',entity=''):
    __r.set(key, json.dumps(entity))

def setInventory(entity=''):
    #print("json.dumps(entity): ",json.dumps(entity))
    __r.set(OBJ_INVENTORY, json.dumps(entity))

def getInventory():
    tmpReturn=''
    if __r.keys(OBJ_INVENTORY):
        tmpReturn=json.loads(__r.get(OBJ_INVENTORY))
    return tmpReturn

def getAccount():
    tmpReturn=''
    if __r.get(OBJ_ACCOUNT):
        tmpReturn=json.loads(__r.get(OBJ_ACCOUNT))
    return tmpReturn

def setAccount(entity=''):
    #print("json.dumps(entity): ",json.dumps(entity))
    __r.set(OBJ_ACCOUNT, json.dumps(entity))

def getProfit():
    tmpReturn=''
    if __r.get(OBJ_PROFIT):
        tmpReturn=json.loads(__r.get(OBJ_PROFIT))
    return tmpReturn

def setProfit(entity=''):
    #print("json.dumps(entity): ",json.dumps(entity))
    __r.set(OBJ_PROFIT, json.dumps(entity))

def getStrKeys(pattern=None):
    reStrKeys=[]
    if pattern:
        for reStrKey in __r.keys(pattern):
            reStrKeys.append(str(reStrKey, encoding='utf-8'))
    else:
        for reStrKey in __r.keys():
            reStrKeys.append(str(reStrKey, encoding='utf-8'))
    return reStrKeys

def getKeys():
    return __r.keys()

def setExchangeHostUrlResps(hostUrlResps=None,ordHostUrlResps=None):
    setTmp('hostUrlResps', hostUrlResps)
    setTmp('ordHostUrlResps', ordHostUrlResps)

def getOrdHostUrlResps():
    return getTmp('ordHostUrlResps')

def getHostUrlResps():
    return getTmp('hostUrlResps')
