import time
import datetime
import asyncio
import DatabaseMng.orm
from DatabaseMng.models import Kline, Contx, SwapInfo, WsSpotTrade, DexV2Info, UniPairInfo, CexPair, TokenInfo, paraspace_generic_events
import DataCollect.DataMem
import LogTeeter
import Configuration
import paraUsers

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def uniPairInfo():
    dataMem = DataCollect.DataMem
    objects = yield from UniPairInfo.findAll()
    for object in objects:
        object['reserve0'] = int(object['reserve0'])
        object['reserve1'] = int(object['reserve1'])
    keyRedis = "database|" + Configuration.Configure.redisKeysPrefix["uniswapPairs"]
    dataMem.setTmp(keyRedis, objects)

def pairs():
    dataMem = DataCollect.DataMem
    objects = yield from CexPair.findAll()
    keyRedis = "database|" + Configuration.Configure.redisKeysPrefix["cexPairs"]
    objList = {}
    for obj in objects:
        isAvai = True
        if obj['trade_status']!='tradable': isAvai = False
        objList.setdefault(obj['pair'], isAvai)
    dataMem.setTmp(keyRedis, objList)

def fun_paraspace_generic_events(_users=None, _where="", _args=None, _orderBy='block_time'):
    if _users:
        list_users = []
        for _user in _users:
            _where = "user0x='"+_user+"'" + " and event_type in ('supply_erc20', 'supply_erc721', 'withdraw_erc721', 'repay_erc20', 'withdraw_erc20', 'cape_withdraw', 'borrow_erc20', 'cape_deposit')"
            objects = yield from paraspace_generic_events.findAll(where=_where, orderBy=_orderBy)
            print("_user:", _user)
            if(len(objects)<1):continue
            paraUsers.ParaUsers.point_user["user0x"] = _user
            paraUsers.ParaUsers.point_user["asset20_bal"] = 0
            paraUsers.ParaUsers.point_user["asset20_acc"] = 0
            paraUsers.ParaUsers.point_user["asset721_bal"] = 0
            paraUsers.ParaUsers.point_user["asset721_acc"] = 0
            paraUsers.ParaUsers.point_user["borrow_bal"] = 0
            paraUsers.ParaUsers.point_user["borrow_acc"] = 0
            paraUsers.ParaUsers.point_user["staking_bal"] = 0
            paraUsers.ParaUsers.point_user["staking_acc"] = 0
            lastDate = objects[0].get('block_time')
            today = datetime.date.today()
            for obj in objects:
                dura = (obj.get('block_time') - lastDate)
                paraUsers.ParaUsers.point_user["asset20_acc"] += paraUsers.ParaUsers.point_user["asset20_bal"] * dura.days
                paraUsers.ParaUsers.point_user["asset721_acc"] += paraUsers.ParaUsers.point_user["asset721_bal"] * dura.days
                paraUsers.ParaUsers.point_user["borrow_acc"] += paraUsers.ParaUsers.point_user["borrow_bal"] * dura.days
                paraUsers.ParaUsers.point_user["staking_acc"] += paraUsers.ParaUsers.point_user["staking_bal"] * dura.days
                # print("point_user:", paraUsers.ParaUsers.point_user, "lastDate:", lastDate, "block_time:", obj.get('block_time'),
                #             "dura.days:", dura.days)

                if obj.get('event_type') == 'supply_erc721':
                    paraUsers.ParaUsers.point_user["asset721_bal"] += obj.get('usd_value')
                elif obj.get('event_type')=='withdraw_erc721':
                    paraUsers.ParaUsers.point_user["asset721_bal"] -= obj.get('usd_value')

                elif obj.get('event_type')=='supply_erc20':
                    paraUsers.ParaUsers.point_user["asset20_bal"] += obj.get('usd_value')
                elif obj.get('event_type')=='withdraw_erc20':
                    paraUsers.ParaUsers.point_user["asset20_bal"] -= obj.get('usd_value')

                elif obj.get('event_type')=='borrow_erc20':
                    paraUsers.ParaUsers.point_user["borrow_bal"] += obj.get('usd_value')
                elif obj.get('event_type')=='repay_erc20':
                    paraUsers.ParaUsers.point_user["borrow_bal"] -= obj.get('usd_value')

                elif obj.get('event_type')=='cape_deposit':
                    paraUsers.ParaUsers.point_user["staking_bal"] += obj.get('usd_value')
                elif obj.get('event_type')=='cape_withdraw':
                    paraUsers.ParaUsers.point_user["staking_bal"] -= obj.get('usd_value')

                lastDate = obj.get('block_time')
                # print("updated_lastDate:", lastDate, "update_userBalance:", paraUsers.ParaUsers.point_user)
                # print(obj)
            # update for today
            dura = (today - lastDate)
            paraUsers.ParaUsers.point_user["asset20_acc"] += paraUsers.ParaUsers.point_user["asset20_bal"] * dura.days
            paraUsers.ParaUsers.point_user["asset721_acc"] += paraUsers.ParaUsers.point_user["asset721_bal"] * dura.days
            paraUsers.ParaUsers.point_user["borrow_acc"] += paraUsers.ParaUsers.point_user["borrow_bal"] * dura.days
            paraUsers.ParaUsers.point_user["staking_acc"] += paraUsers.ParaUsers.point_user["staking_bal"] * dura.days
            # update for today end
            # calculate point
            paraUsers.ParaUsers.point_user["asset20_point"] = \
                paraUsers.ParaUsers.point_user["asset20_acc"]*paraUsers.ParaUsers.point_para.get("asset20").get("base") \
                *paraUsers.ParaUsers.point_para.get("asset20").get("yield")/paraUsers.ParaUsers.point_para.get("asset20").get("period")
            paraUsers.ParaUsers.point_user["asset721_point"] = \
                paraUsers.ParaUsers.point_user["asset721_acc"]*paraUsers.ParaUsers.point_para.get("asset721").get("base") \
                *paraUsers.ParaUsers.point_para.get("asset721").get("yield")/paraUsers.ParaUsers.point_para.get("asset721").get("period")
            paraUsers.ParaUsers.point_user["borrow_point"] = \
                paraUsers.ParaUsers.point_user["borrow_acc"]*paraUsers.ParaUsers.point_para.get("borrow").get("base") \
                *paraUsers.ParaUsers.point_para.get("borrow").get("yield")/paraUsers.ParaUsers.point_para.get("borrow").get("period")
            paraUsers.ParaUsers.point_user["staking_point"] = \
                paraUsers.ParaUsers.point_user["staking_acc"]*paraUsers.ParaUsers.point_para.get("staking").get("base") \
                *paraUsers.ParaUsers.point_para.get("staking").get("yield")/paraUsers.ParaUsers.point_para.get("staking").get("period")
            paraUsers.ParaUsers.point_user["total_point"] = \
                paraUsers.ParaUsers.point_user["asset20_point"] + paraUsers.ParaUsers.point_user["asset721_point"] \
                + paraUsers.ParaUsers.point_user["borrow_point"] + paraUsers.ParaUsers.point_user["staking_point"]
            # print("point_user:", paraUsers.ParaUsers.point_user)
            # calculate point end
            # print("today point_user:", paraUsers.ParaUsers.point_user, "lastDate:", lastDate, "today:", today,
            #       "dura.days:", dura.days)

            # store
            paraUsers.ParaUsers.users_point[_user] = paraUsers.ParaUsers.point_user.copy()
            dataMem = DataCollect.DataMem
            dataMem.setTmp("users_point", paraUsers.ParaUsers.users_point)
            # store end


    else:
        objects = yield from paraspace_generic_events.findAll(where=_where, orderBy=_orderBy)
        userBalance = 0
        lastDate = None
        accumulation = 0
        today = datetime.date.today()
        for obj in objects:
            if userBalance == 0:
                userBalance = obj.get('usd_value')
            else:
                dura = (obj.get('block_time')-lastDate)
                if dura.days==0:
                    accumulation += userBalance
                else:
                    accumulation += userBalance*dura.days
                print("accumulation:", accumulation, "lastDate:", lastDate, "block_time:", obj.get('block_time'), "dura.days:", dura.days, "last_userBalance:", userBalance)
                if obj.get('event_type')=='supply_erc721':
                    userBalance += obj.get('usd_value')
                elif obj.get('event_type')=='withdraw_erc721':
                    userBalance -= obj.get('usd_value')
            lastDate = obj.get('block_time')
            print("updated_lastDate:", lastDate, "update_userBalance:", userBalance)
            print(obj)
        dura = (today-lastDate)
        accumulation += userBalance*dura.days
        print("accumulation:", accumulation, "lastDate:", lastDate, "today:", today, "dura.days:", dura.days, "last_userBalance:", userBalance)

async def main(loop):
    pool = await DatabaseMng.orm.create_pool(
        loop=loop, user=Configuration.Configure.database.get('user'),
        prot=Configuration.Configure.database.get('prot'),
        host=Configuration.Configure.database.get('host'),
        password=Configuration.Configure.database.get('password'),
        db=Configuration.Configure.database.get('db'),
    )
    tasks = []
    coroutine_uniPairInfo = uniPairInfo()
    coroutine_pairs = pairs()
    # tasks.append(coroutine_uniPairInfo)
    # tasks.append(coroutine_pairs)
    # tasks.append(fun_paraspace_generic_events(
    #     _where="user0x=\'0x17D7ED120D36B7792F2608e9D6D8aBD970384D28\' AND (event_type=\'supply_erc721\' OR event_type=\'withdraw_erc721\') "))
    tasks.append(fun_paraspace_generic_events(_users=paraUsers.ParaUsers.users))
    if tasks:
        dones, pendings = await asyncio.wait(tasks)
        for task in dones:
            print(task)
            #Redis.flushPastKey(task.result())

while True:
    print('start database to redis')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    time.sleep(600)
