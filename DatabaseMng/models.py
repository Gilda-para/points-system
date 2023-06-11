#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid
from DatabaseMng.orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Huobi_depth(Model):
    __table__ = 'Huobi_depth'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    symbol = StringField(ddl='varchar(20)')
    TYPE = StringField(ddl='varchar(10)')
    status = StringField(ddl='varchar(10)')
    TS = IntegerField(default=0)
    CH = StringField(ddl='bigint(40)')

class tick_ask(Model):
    __table__ = 'tick_ask'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    huobi_depth_id = StringField(ddl='varchar(50)')
    TS = IntegerField(default=0)
    ASK_PRICE = FloatField(default=0.0)
    ASK_QTY = FloatField(default=0.0)

class tick_bid(Model):
    __table__ = 'tick_bid'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    huobi_depth_id = StringField(ddl='varchar(50)')
    TS = IntegerField(default=0)
    BIDS_PRICE = FloatField(default=0.0)
    BIDS_QTY = FloatField(default=0.0)

class Kline1m(Model):
    __table__ = 'kline1m'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exchange = StringField(ddl='varchar(20)')
    symbol = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    amount = FloatField(default=0.0)
    count = FloatField(default=0.0)
    open = FloatField(default=0.0)
    close = FloatField(default=0.0)
    low = FloatField(default=0.0)
    high = FloatField(default=0.0)
    vol = FloatField(default=0.0) #sum(每一笔成交价 * 该笔的成交量)

#assistance kline
class Kline(Model):
    __table__ = 'kline'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    symbol = StringField(ddl='varchar(20)')
    exchange = StringField(ddl='varchar(20)')
    interval = StringField(ddl='varchar(20)')
    timestamp = IntegerField(default=0)
    vol = FloatField(default=0.0)
    open = FloatField(default=0.0)
    close = FloatField(default=0.0)
    low = FloatField(default=0.0)
    high = FloatField(default=0.0)
    ts = IntegerField(default=0)

class DexV2Info(Model):
    __table__ = 'dexV2Info'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blockTimestamp = StringField(ddl='varchar(20)')
    dexFactory = StringField(ddl='varchar(60)')
    buyToken = StringField(ddl='varchar(60)')
    sellToken = StringField(ddl='varchar(60)')
    buyToken_amt = FloatField(default=0)
    sellToken_amt = FloatField(default=0)
    buyTokenDecimals = IntegerField(default=0)
    sellTokenDecimals = IntegerField(default=0)
    buyToken_price = FloatField(default=0)
    ts = StringField(ddl='varchar(20)')

#assistance con_tx
class Contx(Model):
    __table__ = 'con_tx'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blockNumber = StringField(ddl='varchar(20)')
    timeStamp = StringField(ddl='varchar(20)')
    hash = StringField(ddl='varchar(100)')
    nonce = StringField(ddl='varchar(10)')
    blockHash = StringField(ddl='varchar(100)')
    transactionIndex = StringField(ddl='varchar(10)')
    addrfrom = StringField(ddl='varchar(60)')
    addrto = StringField(ddl='varchar(60)')
    value = StringField(ddl='varchar(60)')
    gas = StringField(ddl='varchar(20)')
    gasPrice = StringField(ddl='varchar(20)')
    isError = StringField(ddl='varchar(2)')
    txreceipt_status = StringField(ddl='varchar(2)')
    contractAddress = StringField(ddl='varchar(60)')
    cumulativeGasUsed = StringField(ddl='varchar(20)')
    gasUsed = StringField(ddl='varchar(20)')
    confirmations = StringField(ddl='varchar(20)')
    mainnet = StringField(ddl='varchar(20)')
    address = StringField(ddl='varchar(60)')
    project = StringField(ddl='varchar(20)')
    input = TextField(default='')
    methodID = StringField(ddl='varchar(100)')
    arg1 = StringField(ddl='varchar(100)')
    arg2 = StringField(ddl='varchar(100)')
    arg3 = StringField(ddl='varchar(100)')
    arg4 = StringField(ddl='varchar(100)')

class SwapInfo(Model):
    __table__ = 'swapInfo'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch = StringField(ddl='varchar(50)')
    timestamp = StringField(ddl='varchar(20)')
    currency_pair = StringField(ddl='varchar(50)')
    token0_amt = FloatField(default=0)
    price = FloatField(default=0)
    token0 = StringField(ddl='varchar(60)')
    base = StringField(ddl='varchar(60)')
    base_amt = FloatField(default=0)
    ts = StringField(ddl='varchar(20)')

class TokenInfo(Model):
    __table__ = 'tokenInfo'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    source = StringField(ddl='varchar(50)')
    address = StringField(ddl='varchar(60)')
    chainId = IntegerField(default=0)
    decimals = IntegerField(default=0)
    name = StringField(ddl='varchar(200)')
    symbol = StringField(ddl='varchar(100)')
    ts = StringField(ddl='varchar(20)')    

class WsSpotTrade(Model):
    __table__ = 'wsSpotTrade'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch = StringField(ddl='varchar(50)')
    channel = StringField(ddl='varchar(20)')
    timestamp = StringField(ddl='varchar(20)')
    tx_id = StringField(ddl='varchar(20)')
    create_time = StringField(ddl='varchar(20)')
    side = StringField(ddl='varchar(10)')
    currency_pair = StringField(ddl='varchar(20)')
    amount = FloatField(default=0)
    price = FloatField(default=0)
    ts = StringField(ddl='varchar(20)')

class UniPairInfo(Model):
    __table__ = 'uniPairInfo'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    factory = StringField(ddl='varchar(60)')
    pair = StringField(ddl='varchar(60)')
    token0 = StringField(ddl='varchar(60)')
    symbol0 = StringField(ddl='varchar(100)')
    reserve0 = FloatField(default=0)
    token1 = StringField(ddl='varchar(60)')
    symbol1 = StringField(ddl='varchar(100)')
    reserve1 = FloatField(default=0)
    blockTimestampLast = StringField(ddl='varchar(20)')
    ts = StringField(ddl='varchar(20)')

class CexPair(Model):
    __table__ = 'cexPair'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch = StringField(ddl='exch(20)')
    ts = StringField(ddl='varchar(20)')
    base = StringField(ddl='varchar(100)')
    pair = StringField(ddl='varchar(200)')
    quote = StringField(ddl='varchar(60)')
    trade_status = StringField(ddl='varchar(20)')

class Tickers(Model):
    __table__ = 'tickers'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exchange = StringField(ddl='varchar(20)')
    symbol = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    amount = FloatField(default=0.0)
    count = FloatField(default=0.0)
    open = FloatField(default=0.0)
    close = FloatField(default=0.0)
    low = FloatField(default=0.0)
    high = FloatField(default=0.0)
    vol = FloatField(default=0.0)

class Currencys(Model):
    __table__ = 'currencys'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exchange = StringField(ddl='varchar(20)')
    currency = StringField(ddl='varchar(20)')

# table exchange_symbols
class ExchangeSymbols(Model):
    __table__ = 'exchange_symbols'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    b_curr = StringField(ddl='varchar(20)')
    q_curr = StringField(ddl='varchar(20)')
    p_prec = IntegerField(default=0)
    amt_prec = IntegerField(default=0)
    symb_part = StringField(ddl='varchar(20)')
    symbol = StringField(ddl='varchar(20)')
    state = StringField(ddl='varchar(20)')
    value_prec = IntegerField(default=0)
    min_ord_amt = FloatField(default=0.0)
    max_ord_amt = IntegerField(default=0)
    min_ord_valu = FloatField(default=0.0)
    exchange = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)

# table exchange_contracts
class ExchangeContracts(Model):
    __table__ = 'exchange_contracts'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    symbol = StringField(ddl='varchar(20)')
    contract_code = StringField(ddl='varchar(20)')
    contract_type = StringField(ddl='varchar(20)')
    contract_size = FloatField(default=0.0)
    price_tick = FloatField(default=0.0)
    delivery_date = StringField(ddl='varchar(10)')
    settlement_date = IntegerField(default=0)
    create_date = StringField(ddl='varchar(10)')
    contract_status = IntegerField(default=0)
    exchange = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)

# table mkt_trade
class MktTrade(Model):
    __table__ = 'mkt_trade'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch_id = StringField(ddl='varchar(50)')
    exch_nm = StringField(ddl='varchar(50)')
    symbol = StringField(ddl='varchar(50)')
    type = StringField(ddl='varchar(10)')
    side = StringField(ddl='varchar(10)')
    trd_id = StringField(ddl='varchar(50)')
    price = FloatField(default=0.0)
    qty = FloatField(default=0.0)
    trd_ts = IntegerField(default=0)
    ts = IntegerField(default=0)

# table mkt_kline
class MktKline(Model):
    __table__ = 'mkt_kline'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch_id = StringField(ddl='varchar(50)')
    exch_nm = StringField(ddl='varchar(50)')
    symbol = StringField(ddl='varchar(50)')
    period = StringField(ddl='varchar(10)')
    open = FloatField(default=0.0)
    close = FloatField(default=0.0)
    low = FloatField(default=0.0)
    high = FloatField(default=0.0)
    amount = FloatField(default=0.0)
    vol = FloatField(default=0.0)
    count = FloatField(default=0.0)
    kline_ts = IntegerField(default=0)
    ts = IntegerField(default=0)

# table mkt_depth
class MktDepth(Model):
    __table__ = 'mkt_depth'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exch_id = StringField(ddl='varchar(50)')
    exch_nm = StringField(ddl='varchar(50)')
    symbol = StringField(ddl='varchar(50)')
    a_b = StringField(ddl='varchar(10)')
    price = FloatField(default=0.0)
    amount = FloatField(default=0.0)
    liqu_qty = FloatField(default=0.0)
    qty = FloatField(default=0.0)
    trd_ts = IntegerField(default=0)
    ts = IntegerField(default=0)

# table ori_huobi_ord_spot_account
class OriHuobiAccountUpdate(Model):
    __table__ = 'ori_huobi_ord_spot_account'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    action = StringField(ddl='varchar(10)')
    ch = StringField(ddl='varchar(50)')
    data_currency = StringField(ddl='varchar(20)')
    data_accountId = StringField(ddl='varchar(20)')
    data_balance = FloatField(default=0.0)
    data_available = FloatField(default=0.0)
    data_changeType = StringField(ddl='varchar(20)')
    data_accountType = StringField(ddl='varchar(20)')
    changeTime = IntegerField(default=0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_spot_order
class OriHuobiOrderUpdate(Model):
    __table__ = 'ori_huobi_ord_spot_order'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    action = StringField(ddl='varchar(10)')
    ch = StringField(ddl='varchar(50)')
    data_remainAmt = FloatField(default=0.0)
    data_orderSize = FloatField(default=0.0)
    data_lastActTime = IntegerField(default=0)
    data_clientOrderId = StringField(ddl='varchar(20)')
    data_orderId = StringField(ddl='varchar(20)')
    data_orderStatus = StringField(ddl='varchar(20)')
    data_symbol = StringField(ddl='varchar(20)')
    data_eventType = StringField(ddl='varchar(20)')
    data_type = StringField(ddl='varchar(20)')
    data_tradePrice = FloatField(default=0.0)
    data_tradeVolume = FloatField(default=0.0)
    data_tradeId = StringField(ddl='varchar(50)')
    data_aggressor = StringField(ddl='varchar(10)')
    data_tradeTime = IntegerField(default=0)
    data_orderPrice = FloatField(default=0.0)
    data_orderCreateTime = IntegerField(default=0)
    data_orderValue = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_deli_accounts
class OriHuobiOrdConAccounts(Model):
    __table__ = 'ori_huobi_ord_deli_accounts'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    uid = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    event = StringField(ddl='varchar(50)')
    data_symbol = StringField(ddl='varchar(20)')
    data_margin_balance = FloatField(default=0.0)
    data_margin_static = FloatField(default=0.0)
    data_margin_position = FloatField(default=0.0)
    data_margin_frozen = FloatField(default=0.0)
    data_margin_available = FloatField(default=0.0)
    data_profit_real = FloatField(default=0.0)
    data_profit_unreal = FloatField(default=0.0)
    data_risk_rate = FloatField(default=0.0)
    data_liquidation_price = FloatField(default=0.0)
    data_withdraw_available = FloatField(default=0.0)
    data_lever_rate = FloatField(default=0.0)
    data_adjust_factor = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_deli_contractinfo
class OriHuobiOrdConContractinfo(Model):
    __table__ = 'ori_huobi_ord_deli_contractinfo'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    event = StringField(ddl='varchar(50)')
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_contract_type = StringField(ddl='varchar(20)')
    data_contract_size = FloatField(default=0.0)
    data_price_tick = FloatField(default=0.0)
    data_delivery_date = StringField(ddl='varchar(15)')
    data_create_date = StringField(ddl='varchar(15)')
    data_contract_status = IntegerField(default=0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_huobi_ord_deli_liquidation
class OriHuobiOrdConLiquidation(Model):
    __table__ = 'ori_huobi_ord_deli_liquidation'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_direction = StringField(ddl='varchar(10)')
    data_offset = StringField(ddl='varchar(10)')
    data_volume = FloatField(default=0.0)
    data_price = FloatField(default=0.0)
    data_created_at = IntegerField(default=0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_huobi_ord_deli_matchorders
class OriHuobiOrdConMatchorders(Model):
    __table__ = 'ori_huobi_ord_deli_matchorders'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    uid = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    symbol = StringField(ddl='varchar(20)')
    contract_type = StringField(ddl='varchar(10)')
    contract_code = StringField(ddl='varchar(20)')
    order_id = StringField(ddl='varchar(20)')
    order_id_str = StringField(ddl='varchar(20)')
    client_order_id = StringField(ddl='varchar(20)')
    order_type = IntegerField(default=0)
    trade_volume = FloatField(default=0.0)
    status = IntegerField(default=0)
    volume = FloatField(default=0.0)
    trade_role = StringField(ddl='varchar(10)')
    trade_created_at = IntegerField(default=0)
    trade_trade_turnover = FloatField(default=0.0)
    trade_trade_price = FloatField(default=0.0)
    trade_trade_volume = FloatField(default=0.0)
    trade_id = StringField(ddl='varchar(20)')
    trade_trade_id = StringField(ddl='varchar(20)')
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_deli_orders
class OriHuobiOrdConOrders(Model):
    __table__ = 'ori_huobi_ord_deli_orders'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    uid = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    symbol = StringField(ddl='varchar(20)')
    contract_type = StringField(ddl='varchar(10)')
    contract_code = StringField(ddl='varchar(20)')
    volume = FloatField(default=0.0)
    price = FloatField(default=0.0)
    order_price_type = StringField(ddl='varchar(20)')
    direction = StringField(ddl='varchar(10)')
    offset = StringField(ddl='varchar(10)')
    status = IntegerField(default=0)
    lever_rate = IntegerField(default=0)
    order_id = IntegerField(default=0)
    order_id_str = StringField(ddl='varchar(20)')
    client_order_id = StringField(ddl='varchar(20)')
    order_source = StringField(ddl='varchar(10)')
    order_type = IntegerField(default=0)
    created_at = IntegerField(default=0)
    canceled_at = IntegerField(default=0)
    trade_volume = FloatField(default=0.0)
    trade_trade_fee = FloatField(default=0.0)
    trade_turnover = FloatField(default=0.0)
    fee = FloatField(default=0.0)
    fee_asset = StringField(ddl='varchar(20)')
    trade_avg_price = FloatField(default=0.0)
    margin_frozen = FloatField(default=0.0)
    profit = FloatField(default=0.0)
    liquidation_type = StringField(ddl='varchar(10)')
    trade_id = StringField(ddl='varchar(50)')
    trade_trade_id = StringField(ddl='varchar(20)')
    trade_trade_price = FloatField(default=0.0)
    trade_trade_turnover = FloatField(default=0.0)

    trade_created_at = IntegerField(default=0)
    trade_trade_turnover = FloatField(default=0.0)
    trade_fee_asset = StringField(ddl='varchar(20)')
    trade_trade_volume = FloatField(default=0.0)
    trade_role = StringField(ddl='varchar(10)')
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_deli_positions
class OriHuobiOrdConPostions(Model):
    __table__ = 'ori_huobi_ord_deli_positions'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    uid = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    event = StringField(ddl='varchar(50)')
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_contract_type = StringField(ddl='varchar(10)')
    data_volume = FloatField(default=0.0)
    data_available = FloatField(default=0.0)
    data_frozen = FloatField(default=0.0)
    data_cost_open = FloatField(default=0.0)
    data_cost_hold = FloatField(default=0.0)
    data_profit_unreal = FloatField(default=0.0)
    data_profit_rate = FloatField(default=0.0)
    data_profit = FloatField(default=0.0)
    data_position_margin = FloatField(default=0.0)
    data_lever_rate = FloatField(default=0.0)
    data_direction = StringField(ddl='varchar(20)')
    data_last_price = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_account
class OriHuobiOrdPerpAccount(Model):
    __table__ = 'ori_huobi_ord_perp_account'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    ts = IntegerField(default=0)
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    uid = StringField(ddl='varchar(20)')
    event = StringField(ddl='varchar(50)')
    list_symbol = StringField(ddl='varchar(20)')
    list_contract_code = StringField(ddl='varchar(20)')
    list_margin_balance = FloatField(default=0.0)
    list_margin_static = FloatField(default=0.0)
    list_margin_position = FloatField(default=0.0)
    list_margin_frozen = FloatField(default=0.0)
    list_margin_available = FloatField(default=0.0)
    list_profit_real = FloatField(default=0.0)
    list_profit_unreal = FloatField(default=0.0)
    list_risk_rate = FloatField(default=0.0)
    list_liquidation_price = FloatField(default=0.0)
    list_withdraw_available = FloatField(default=0.0)
    list_lever_rate = IntegerField(default=0)
    list_adjust_factor = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_contractinfo
class OriHuobiOrdPerpContractinfo(Model):
    __table__ = 'ori_huobi_ord_perp_contractinfo'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    event = StringField(ddl='varchar(50)')
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_contract_size = FloatField(default=0.0)
    data_price_tick = FloatField(default=0.0)
    data_settlement_date = IntegerField(default=0)
    data_create_date = StringField(ddl='varchar(15)')
    data_contract_status = StringField(ddl='varchar(2)')
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_fundingrate
class OriHuobiOrdPerpFundingrate(Model):
    __table__ = 'ori_huobi_ord_perp_fundingrate'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(50)')
    ts = IntegerField(default=0)
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_fee_asset = StringField(ddl='varchar(20)')
    data_funding_time = IntegerField(default=0)
    data_funding_rate = FloatField(default=0.0)
    data_estimated_rate = FloatField(default=0.0)
    data_settlement_time = IntegerField(default=0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_liquidation
class OriHuobiOrdPerpLiquidation(Model):
    __table__ = 'ori_huobi_ord_perp_liquidation'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    data_symbol = StringField(ddl='varchar(20)')
    data_contract_code = StringField(ddl='varchar(20)')
    data_direction = StringField(ddl='varchar(10)')
    data_offset = StringField(ddl='varchar(10)')
    data_volume = FloatField(default=0.0)
    data_price = FloatField(default=0.0)
    data_created_at = IntegerField(default=0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_matchOrder
class OriHuobiOrdPerpMatchOrder(Model):
    __table__ = 'ori_huobi_ord_perp_matchOrder'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    uid = StringField(ddl='varchar(20)')
    symbol = StringField(ddl='varchar(20)')
    contract_code = StringField(ddl='varchar(20)')
    status = StringField(ddl='varchar(2)')
    order_id = StringField(ddl='varchar(20)')
    order_id_str = StringField(ddl='varchar(20)')
    client_order_id = StringField(ddl='varchar(20)')
    order_type = StringField(ddl='varchar(2)')
    trade_volume = FloatField(default=0.0)
    volume = FloatField(default=0.0)
    trade_id = StringField(ddl='varchar(20)')
    trade_trade_id = StringField(ddl='varchar(20)')
    trade_trade_price = FloatField(default=0.0)
    trade_trade_volume = FloatField(default=0.0)
    trade_trade_turnover = FloatField(default=0.0)
    trade_created_at = IntegerField(default=0)
    trade_role = StringField(ddl='varchar(20)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_order
class OriHuobiOrdPerpOrder(Model):
    __table__ = 'ori_huobi_ord_perp_order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    uid = StringField(ddl='varchar(20)')
    symbol = StringField(ddl='varchar(20)')
    contract_code = StringField(ddl='varchar(20)')
    volume = FloatField(default=0.0)
    price = FloatField(default=0.0)
    order_price_type = StringField(ddl='varchar(10)')
    direction = StringField(ddl='varchar(10)')
    offset = StringField(ddl='varchar(10)')
    status = StringField(ddl='varchar(2)')
    lever_rate = IntegerField(default=0)
    order_id = StringField(ddl='varchar(20)')
    order_id_str = StringField(ddl='varchar(20)')
    client_order_id = StringField(ddl='varchar(20)')
    order_source = StringField(ddl='varchar(20)')
    order_type = StringField(ddl='varchar(2)')
    created_at = IntegerField(default=0)
    trade_volume = FloatField(default=0.0)
    trade_turnover = FloatField(default=0.0)
    fee = FloatField(default=0.0)
    trade_avg_price = FloatField(default=0.0)
    margin_frozen = FloatField(default=0.0)
    profit = FloatField(default=0.0)
    liquidation_type = StringField(ddl='varchar(2)')
    canceled_at = IntegerField(default=0)
    fee_asset = StringField(ddl='varchar(20)')
    list_trade_id = StringField(ddl='varchar(20)')
    list_id = StringField(ddl='varchar(50)')
    list_trade_volume = FloatField(default=0.0)
    list_trade_price = FloatField(default=0.0)
    list_trade_fee = FloatField(default=0.0)
    list_fee_asset = StringField(ddl='varchar(20)')
    list_trade_turnover = FloatField(default=0.0)
    list_created_at = IntegerField(default=0)
    list_role = StringField(ddl='varchar(10)')
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_huobi_ord_perp_position
class OriHuobiOrdPerpPosition(Model):
    __table__ = 'ori_huobi_ord_perp_position'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    op = StringField(ddl='varchar(20)')
    topic = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)
    uid = StringField(ddl='varchar(20)')
    event = StringField(ddl='varchar(50)')
    list_symbol = StringField(ddl='varchar(20)')
    list_contract_code = StringField(ddl='varchar(20)')
    list_volume = FloatField(default=0.0)
    list_available = FloatField(default=0.0)
    list_frozen = FloatField(default=0.0)
    list_cost_open = FloatField(default=0.0)
    list_cost_hold = FloatField(default=0.0)
    list_profit_unreal = FloatField(default=0.0)
    list_profit_rate = FloatField(default=0.0)
    list_profit = FloatField(default=0.0)
    list_position_margin = FloatField(default=0.0)
    list_lever_rate = IntegerField(default=0)
    list_direction = StringField(ddl='varchar(10)')
    list_last_price = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_spot_account
class ori_bina_ord_spot_account(Model):
    __table__ = 'ori_bina_ord_spot_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    m_makerate = FloatField(default=0.0)
    t_takerate = FloatField(default=0.0)
    b_buyrate = FloatField(default=0.0)
    s_sellrate = FloatField(default=0.0)
    t_allowtrd = StringField(ddl='varchar(10)')
    w_allowWithdraw = StringField(ddl='varchar(10)')
    d_allowdeposit = StringField(ddl='varchar(10)')
    u_lastts = IntegerField(default=0)
    b_a_symbol = StringField(ddl='varchar(20)')
    b_f_bal = FloatField(default=0.0)
    b_l_frozen = FloatField(default=0.0)
    p_permission = StringField(ddl='varchar(10)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_bina_ord_spot_balanceupdate
class ori_bina_ord_spot_balanceupdate(Model):
    __table__ = 'ori_bina_ord_spot_balanceupdate'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    a_symbol = StringField(ddl='varchar(20)')
    d_baldelta = FloatField(default=0.0)
    t_clearts = IntegerField(default=0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_spot_executionreport
class ori_bina_ord_spot_executionreport(Model):
    __table__ = 'ori_bina_ord_spot_executionreport'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    s_symbol = StringField(ddl='varchar(20)')
    c_clientorderid = StringField(ddl='varchar(50)')
    s_direction = StringField(ddl='varchar(10)')
    o_type = StringField(ddl='varchar(10)')
    f_effect = StringField(ddl='varchar(10)')
    q_qty = FloatField(default=0.0)
    p_price = FloatField(default=0.0)
    p_limitprice = FloatField(default=0.0)
    f_iceprice = FloatField(default=0.0)
    g_ocoid = StringField(ddl='varchar(20)')
    c_oriordid = StringField(ddl='varchar(20)')
    x_exectype = StringField(ddl='varchar(10)')
    x_ordstatus = StringField(ddl='varchar(10)')
    r_ordrejectreason = StringField(ddl='varchar(20)')
    i_ordid = StringField(ddl='varchar(20)')
    l_orddoneqty = FloatField(default=0.0)
    z_ordaccqty = FloatField(default=0.0)
    l_ordlastprice = FloatField(default=0.0)
    n_fee = FloatField(default=0.0)
    n_feeasstype = StringField(ddl='varchar(10)')
    t_dealdonets = IntegerField(default=0)
    t_dealdoneid = StringField(ddl='varchar(20)')
    w_isordbook = StringField(ddl='varchar(10)')
    m_ismakedeal = StringField(ddl='varchar(10)')
    o_ordcreatets = IntegerField(default=0)
    z_accdoneamount = FloatField(default=0.0)
    y_lastdoneamount = FloatField(default=0.0)
    q_quoteordqty = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_bina_ord_spot_listStatus
class ori_bina_ord_spot_listStatus(Model):
    __table__ = 'ori_bina_ord_spot_listStatus'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    s_symbol = StringField(ddl='varchar(20)')
    g_ordlistid = StringField(ddl='varchar(20)')
    c_contingencytype = StringField(ddl='varchar(10)')
    l_liststatustype = StringField(ddl='varchar(10)')
    l_ordstatus = StringField(ddl='varchar(10)')
    r_rejectreason = StringField(ddl='varchar(10)')
    c_clientordid = StringField(ddl='varchar(20)')
    t_dealdonets = IntegerField(default=0)
    o_s_symbol = StringField(ddl='varchar(20)')
    o_i_ordid = StringField(ddl='varchar(20)')
    o_i_clientordid = StringField(ddl='varchar(20)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_bina_ord_deli_margincall
class ori_bina_ord_deli_margincall(Model):
    __table__ = 'ori_bina_ord_deli_margincall'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    i_accalia = StringField(ddl='varchar(20)')
    cw_balance = FloatField(default=0.0)
    p_s_symbol = StringField(ddl='varchar(20)')
    p_ps_direction = StringField(ddl='varchar(10)')
    p_pa_posi = FloatField(default=0.0)
    p_mt_marginmode = StringField(ddl='varchar(10)')
    p_iw_margin = FloatField(default=0.0)
    p_mp_price = FloatField(default=0.0)
    p_up_unrealpl = FloatField(default=0.0)
    p_mm_mainmargin = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_deli_ordertradeupdate
class ori_bina_ord_deli_ordertradeupdate(Model):
    __table__ = 'ori_bina_ord_deli_ordertradeupdate'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    t_matchts = IntegerField(default=0)
    i_accountalias = StringField(ddl='varchar(20)')
    o_s_symbol = StringField(ddl='varchar(20)')
    o_c_clientordid = StringField(ddl='varchar(50)')
    o_s_dire = StringField(ddl='varchar(10)')
    o_o_type = StringField(ddl='varchar(20)')
    o_f_effect = StringField(ddl='varchar(10)')
    o_q_qty = FloatField(default=0.0)
    o_p_oripirce = FloatField(default=0.0)
    o_ap_avgpirce = FloatField(default=0.0)
    o_sp_tripirce = FloatField(default=0.0)
    o_x_exectype = StringField(ddl='varchar(20)')
    o_x_status = StringField(ddl='varchar(10)')
    o_i_ordid = StringField(ddl='varchar(20)')
    o_l_lastqty = FloatField(default=0.0)
    o_z_accqty = FloatField(default=0.0)
    o_l_undoneprice = FloatField(default=0.0)
    o_ma_mainass = StringField(ddl='varchar(20)')
    o_n_feetype = StringField(ddl='varchar(20)')
    o_n_feeqty = FloatField(default=0.0)
    o_t_donets = IntegerField(default=0)
    o_t_doneid = StringField(ddl='varchar(20)')
    o_rp_realpl = FloatField(default=0.0)
    o_b_buyordnetworth = FloatField(default=0.0)
    o_a_sellordnetworth = FloatField(default=0.0)
    o_m_isdonebymake = StringField(ddl='varchar(10)')
    o_r_islight = StringField(ddl='varchar(10)')
    o_wt_tripricetype = StringField(ddl='varchar(20)')
    o_ot_oriordtype = StringField(ddl='varchar(20)')
    o_ps_posidire = StringField(ddl='varchar(10)')
    o_cp_istriord = StringField(ddl='varchar(10)')
    o_ap_tracstoplossprice = FloatField(default=0.0)
    o_cr_tracstoplossrate = FloatField(default=0.0)
    o_pp_isprotopen = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_bina_ord_deli_accountupdate
class ori_bina_ord_deli_accountupdate(Model):
    __table__ = 'ori_bina_ord_deli_accountupdate'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    t_matchts = IntegerField(default=0)
    i_accountalias = StringField(ddl='varchar(20)')

    a_b_a_ass = StringField(ddl='varchar(20)')
    a_b_wb_walletbal = FloatField(default=0.0)
    a_b_cw_marginwalletbal = FloatField(default=0.0)
    a_p_s_symbol = StringField(ddl='varchar(20)')
    a_p_pa_posi = FloatField(default=0.0)
    a_p_ep_price = FloatField(default=0.0)
    a_p_cr_accrealpl = FloatField(default=0.0)
    a_p_up_unrealpl = FloatField(default=0.0)
    a_p_mt_marginmode = StringField(ddl='varchar(10)')
    a_p_iw_margin = FloatField(default=0.0)
    a_p_ps_margindirection = StringField(ddl='varchar(10)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_perp_accountupdate
class ori_bina_ord_perp_accountupdate(Model):
    __table__ = 'ori_bina_ord_perp_accountupdate'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    t_matchts = IntegerField(default=0)
    a_m_eventreason = StringField(ddl='varchar(20)')
    a_b_a_ass = StringField(ddl='varchar(20)')
    a_b_wb_walletbal = FloatField(default=0.0)
    a_b_cw_marginwalletbal = FloatField(default=0.0)
    a_p_s_symbol = StringField(ddl='varchar(20)')
    a_p_pa_posi = FloatField(default=0.0)
    a_p_ep_price = FloatField(default=0.0)
    a_p_cr_accrealpl = FloatField(default=0.0)
    a_p_up_unrealpl = FloatField(default=0.0)
    a_p_mt_marginmode = StringField(ddl='varchar(10)')
    a_p_iw_margin = FloatField(default=0.0)
    a_p_ps_margindirection = StringField(ddl='varchar(10)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_perp_margincall
class ori_bina_ord_perp_margincall(Model):
    __table__ = 'ori_bina_ord_perp_margincall'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    cw_balance = FloatField(default=0.0)
    p_s_symbol = StringField(ddl='varchar(20)')
    p_ps_direction = StringField(ddl='varchar(10)')
    p_pa_posi = FloatField(default=0.0)
    p_mt_marginmode = StringField(ddl='varchar(10)')
    p_iw_margin = FloatField(default=0.0)
    p_mp_price = FloatField(default=0.0)
    p_up_unrealpl = FloatField(default=0.0)
    p_mm_mainmargin = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_bina_ord_perp_ordertradeupdate
class ori_bina_ord_perp_ordertradeupdate(Model):
    __table__ = 'ori_bina_ord_perp_ordertradeupdate'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    e_op = StringField(ddl='varchar(20)')
    e_ts = IntegerField(default=0)
    t_matchts = IntegerField(default=0)

    o_s_symbol = StringField(ddl='varchar(20)')
    o_c_clientordid = StringField(ddl='varchar(50)')
    o_s_dire = StringField(ddl='varchar(10)')
    o_o_type = StringField(ddl='varchar(20)')
    o_f_effect = StringField(ddl='varchar(10)')
    o_q_qty = FloatField(default=0.0)
    o_p_oripirce = FloatField(default=0.0)
    o_ap_avgpirce = FloatField(default=0.0)
    o_sp_tripirce = FloatField(default=0.0)
    o_x_exectype = StringField(ddl='varchar(20)')
    o_x_status = StringField(ddl='varchar(10)')
    o_i_ordid = StringField(ddl='varchar(20)')

    o_l_doneqty = FloatField(default=0.0)
    o_z_accqty = FloatField(default=0.0)
    o_l_undoneprice = FloatField(default=0.0)
    o_ma_marginass = StringField(ddl='varchar(20)')
    o_n_feetype = StringField(ddl='varchar(20)')
    o_n_feeqty = FloatField(default=0.0)
    o_t_donets = IntegerField(default=0)
    o_t_doneid = StringField(ddl='varchar(20)')

    o_b_buyordnetworth = FloatField(default=0.0)
    o_a_sellordnetworth = FloatField(default=0.0)
    o_m_isdonebymake = StringField(ddl='varchar(10)')
    o_r_islight = StringField(ddl='varchar(10)')
    o_wt_tripricetype = StringField(ddl='varchar(20)')
    o_ot_oriordtype = StringField(ddl='varchar(20)')
    o_ps_posidire = StringField(ddl='varchar(10)')
    o_cp_istriord = StringField(ddl='varchar(10)')
    o_ap_tracstoplossprice = FloatField(default=0.0)
    o_cr_tracstoplossrate = FloatField(default=0.0)
    o_rp_dealrealpl = FloatField(default=0.0)
    o_pp_isprotect = StringField(ddl='varchar(10)')


    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_deli_account
class ori_okex_ord_deli_account(Model):
    __table__ = 'ori_okex_ord_deli_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_currency = StringField(ddl='varchar(20)')
    data_margin_mode = StringField(ddl='varchar(10)')
    data_equity = FloatField(default=0.0)
    data_total_avail_balance = FloatField(default=0.0)
    data_margin = FloatField(default=0.0)
    data_realized_pnl = FloatField(default=0.0)
    data_unrealized_pnl = FloatField(default=0.0)
    data_margin_ratio = FloatField(default=0.0)
    data_margin_frozen = FloatField(default=0.0)
    data_margin_for_unfilled = FloatField(default=0.0)
    data_maint_margin_ratio = FloatField(default=0.0)
    data_liqui_mode = StringField(ddl='varchar(10)')
    data_available = FloatField(default=0.0)
    data_open_max = IntegerField(default=0)
    data_can_withdraw = FloatField(default=0.0)
    data_underlying = StringField(ddl='varchar(10)')

    data_timestamp = StringField(ddl='varchar(30)')
    
    data_contracts_available_qty = FloatField(default=0.0)
    data_contracts_fixed_balance = FloatField(default=0.0)
    data_contracts_instrument_id = StringField(ddl='varchar(20)')
    data_contracts_long_open_max = FloatField(default=0.0)
    data_contracts_margin_for_unfilled = FloatField(default=0.0)
    data_contracts_margin_frozen = FloatField(default=0.0)
    data_contracts_realized_pnl = FloatField(default=0.0)
    data_contracts_short_open_max = FloatField(default=0.0)
    data_contracts_timestamp = StringField(ddl='varchar(30)')
    data_contracts_unrealized_pnl = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_deli_order
class ori_okex_ord_deli_order(Model):
    __table__ = 'ori_okex_ord_deli_order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_instrument_id = StringField(ddl='varchar(50)')
    data_client_oid = StringField(ddl='varchar(50)')
    data_size = FloatField(default=0.0)
    data_timestamp = StringField(ddl='varchar(30)')
    data_filled_qty = FloatField(default=0.0)
    data_fee = FloatField(default=0.0)
    data_order_id = StringField(ddl='varchar(20)')
    data_price = FloatField(default=0.0)
    data_error_code = StringField(ddl='varchar(10)')
    data_pnl = FloatField(default=0.0)
    data_price_avg = FloatField(default=0.0)
    data_type = StringField(ddl='varchar(2)')
    data_contract_val = FloatField(default=0.0)
    data_leverage = StringField(ddl='varchar(10)')
    data_order_type = StringField(ddl='varchar(2)')
    data_last_fill_px = FloatField(default=0.0)
    data_last_fill_id = StringField(ddl='varchar(20)')
    data_last_fill_qty = FloatField(default=0.0)
    data_last_fill_time = StringField(ddl='varchar(30)')
    data_state = StringField(ddl='varchar(2)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_deli_orderalgo
class ori_okex_ord_deli_orderalgo(Model):
    __table__ = 'ori_okex_ord_deli_orderalgo'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_algo_id = StringField(ddl='varchar(20)')
    data_order_type = StringField(ddl='varchar(22)')
    data_leverage = StringField(ddl='varchar(10)')
    data_size = FloatField(default=0.0)
    data_instrument_id = StringField(ddl='varchar(50)')
    data_type = StringField(ddl='varchar(2)')
    data_timestamp = StringField(ddl='varchar(30)')
    data_status = StringField(ddl='varchar(2)')
    data_algo_price= FloatField(default=0.0)
    data_trigger_price= FloatField(default=0.0)
    data_real_amount= FloatField(default=0.0)
    data_algo_type= StringField(ddl='varchar(2)')
    data_callback_rate= FloatField(default=0.0)
    data_algo_variance= FloatField(default=0.0)
    data_avg_amount= FloatField(default=0.0)
    data_price_limit= FloatField(default=0.0)
    data_deal_value= FloatField(default=0.0)
    data_sweep_range= FloatField(default=0.0)
    data_sweep_ratio= FloatField(default=0.0)
    data_single_limit= FloatField(default=0.0)
    data_time_interval= FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_deli_position
class ori_okex_ord_deli_position(Model):
    __table__ = 'ori_okex_ord_deli_position'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_long_qty = FloatField(default=0.0)
    data_liquidation_price = FloatField(default=0.0)
    data_long_avail_qty = FloatField(default=0.0)
    data_long_margin = FloatField(default=0.0)
    data_long_liqui_price = FloatField(default=0.0)
    data_long_pnl_ratio = FloatField(default=0.0)
    data_long_avg_cost = FloatField(default=0.0)
    data_long_settlement_price = FloatField(default=0.0)
    data_realised_pnl = FloatField(default=0.0)
    data_short_qty = FloatField(default=0.0)
    data_short_avail_qty = FloatField(default=0.0)
    data_short_margin = FloatField(default=0.0)
    data_short_liqui_price = FloatField(default=0.0)
    data_short_pnl_ratio = FloatField(default=0.0)
    data_short_avg_cost = FloatField(default=0.0)
    data_short_settlement_price = FloatField(default=0.0)
    data_instrument_id = StringField(ddl='varchar(50)')
    data_long_leverage = IntegerField(default=0)
    data_short_leverage = IntegerField(default=0)
    data_created_at = StringField(ddl='varchar(30)')
    data_updated_at = StringField(ddl='varchar(30)')
    data_timestamp = StringField(ddl='varchar(30)')
    data_margin_mode = StringField(ddl='varchar(10)')
    data_short_margin_ratio = FloatField(default=0.0)
    data_short_maint_margin_ratio = FloatField(default=0.0)
    data_short_pnl = FloatField(default=0.0)
    data_short_unrealised_pnl = FloatField(default=0.0)
    data_long_margin_ratio = FloatField(default=0.0)
    data_long_maint_margin_ratio = FloatField(default=0.0)
    data_long_pnl = FloatField(default=0.0)
    data_long_unrealised_pnl = FloatField(default=0.0)
    data_long_open_outstanding = FloatField(default=0.0)
    data_short_open_outstanding = FloatField(default=0.0)
    data_long_settled_pnl = FloatField(default=0.0)
    data_short_settled_pnl = FloatField(default=0.0)
    data_last = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


# table ori_okex_ord_opt_account
class ori_okex_ord_opt_account(Model):
    __table__ = 'ori_okex_ord_opt_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_currency = StringField(ddl='varchar(20)')
    data_underlying = StringField(ddl='varchar(20)')
    data_equity = FloatField(default=0.0)
    data_total_avail_balance = FloatField(default=0.0)
    data_margin_balance = FloatField(default=0.0)
    data_margin_frozen = FloatField(default=0.0)
    data_avail_margin = FloatField(default=0.0)
    data_margin_for_unfilled = FloatField(default=0.0)
    data_maintenance_margin = FloatField(default=0.0)
    data_realized_pnl = FloatField(default=0.0)
    data_unrealized_pnl = FloatField(default=0.0)
    data_option_value = FloatField(default=0.0)
    data_delta = FloatField(default=0.0)
    data_vega = FloatField(default=0.0)
    data_gamma = FloatField(default=0.0)
    data_theta = FloatField(default=0.0)
    data_risk_factor = FloatField(default=0.0)
    data_margin_multiplier = FloatField(default=0.0)
    data_account_status = StringField(ddl='varchar(2)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_opt_order
class ori_okex_ord_opt_order(Model):
    __table__ = 'ori_okex_ord_opt_order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_order_id = StringField(ddl='varchar(20)')
    data_client_oid = StringField(ddl='varchar(50)')
    data_timestamp = StringField(ddl='varchar(30)')
    data_underlying = StringField(ddl='varchar(20)')
    data_instrument_id = StringField(ddl='varchar(50)')
    data_size = FloatField(default=0.0)
    data_price = FloatField(default=0.0)
    data_side = StringField(ddl='varchar(10)')
    data_filled_qty = FloatField(default=0.0)
    data_price_avg = FloatField(default=0.0)
    data_fee = FloatField(default=0.0)
    data_contract_val = FloatField(default=0.0)
    data_last_fill_px = FloatField(default=0.0)
    data_last_fill_qty = FloatField(default=0.0)
    data_last_fill_id = StringField(ddl='varchar(20)')
    data_order_type = StringField(ddl='varchar(2)')
    data_last_request_id = StringField(ddl='varchar(20)')
    data_last_amend_result = StringField(ddl='varchar(20)')
    data_state = StringField(ddl='varchar(2)')
    data_type = StringField(ddl='varchar(2)')
    data_event_code = StringField(ddl='varchar(10)')
    data_event_message = StringField(ddl='varchar(100)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_opt_position
class ori_okex_ord_opt_position(Model):
    __table__ = 'ori_okex_ord_opt_position'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_instrument_id = StringField(ddl='varchar(50)')
    data_position = FloatField(default=0.0)
    data_avg_cost = FloatField(default=0.0)
    data_avail_position = FloatField(default=0.0)
    data_settlement_price = FloatField(default=0.0)
    data_total_pnl = FloatField(default=0.0)
    data_pnl_ratio = FloatField(default=0.0)
    data_realized_pnl = FloatField(default=0.0)
    data_unrealized_pnl = FloatField(default=0.0)
    data_pos_margin = FloatField(default=0.0)
    data_option_value = FloatField(default=0.0)
    data_created_at = StringField(ddl='varchar(30)')
    data_updated_at = StringField(ddl='varchar(30)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_perp_account
class ori_okex_ord_perp_account(Model):
    __table__ = 'ori_okex_ord_perp_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_equity = FloatField(default=0.0)
    data_instrument_id = StringField(ddl='varchar(50)')
    data_margin = FloatField(default=0.0)
    data_margin_frozen = FloatField(default=0.0)
    data_margin_ratio = FloatField(default=0.0)
    data_realized_pnl = FloatField(default=0.0)
    data_timestamp = StringField(ddl='varchar(30)')
    data_total_avail_balance = FloatField(default=0.0)
    data_unrealized_pnl = FloatField(default=0.0)
    data_fixed_balance = FloatField(default=0.0)
    data_margin_mode = StringField(ddl='varchar(10)')
    data_maint_margin_ratio = FloatField(default=0.0)
    data_available_qty = FloatField(default=0.0)
    data_long_open_max = FloatField(default=0.0)
    data_short_open_max = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_perp_order
class ori_okex_ord_perp_order(Model):
    __table__ = 'ori_okex_ord_perp_order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_instrument_id = StringField(ddl='varchar(10)')
    data_size = FloatField(default=0.0)
    data_timestamp = StringField(ddl='varchar(30)')
    data_filled_qty = FloatField(default=0.0)
    data_fee = FloatField(default=0.0)
    data_error_code = StringField(ddl='varchar(10)')
    data_order_id = StringField(ddl='varchar(10)')
    data_client_oid = StringField(ddl='varchar(50)')
    data_price = FloatField(default=0.0)
    data_price_avg = FloatField(default=0.0)
    data_type = StringField(ddl='varchar(2)')
    data_contract_val = FloatField(default=0.0)
    data_order_type = StringField(ddl='varchar(2)')
    data_last_fill_px = FloatField(default=0.0)
    data_last_fill_qty = FloatField(default=0.0)
    data_last_fill_time = StringField(ddl='varchar(30)')
    data_last_fill_id = StringField(ddl='varchar(10)')
    data_state = StringField(ddl='varchar(2)')
    data_leverage = StringField(ddl='varchar(10)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_perp_orderalgo
class ori_okex_ord_perp_orderalgo(Model):
    __table__ = 'ori_okex_ord_perp_orderalgo'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')
    data_algo_id = StringField(ddl='varchar(20)')
    data_order_type = StringField(ddl='varchar(2)')
    data_leverage = StringField(ddl='varchar(10)')
    data_size = FloatField(default=0.0)
    data_instrument_id = StringField(ddl='varchar(50)')
    data_type = StringField(ddl='varchar(2)')
    data_timestamp = StringField(ddl='varchar(30)')
    data_status = StringField(ddl='varchar(2)')
    data_algo_price = FloatField(default=0.0)
    data_trigger_price = FloatField(default=0.0)
    data_algo_type = StringField(ddl='varchar(2)')
    data_callback_rate =FloatField(default=0.0)
    data_algo_variance = FloatField(default=0.0)
    data_avg_amount = FloatField(default=0.0)
    data_price_limit = FloatField(default=0.0)
    data_sweep_range = FloatField(default=0.0)
    data_sweep_ratio = FloatField(default=0.0)
    data_single_limit = FloatField(default=0.0)
    data_time_interval = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_perp_position
class ori_okex_ord_perp_position(Model):
    __table__ = 'ori_okex_ord_perp_position'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')

    data_instrument_id = StringField(ddl='varchar(50)')
    data_margin_mode = StringField(ddl='varchar(10)')
    data_timestamp = StringField(ddl='varchar(30)')
    data_holding_liquidation_price = FloatField(default=0.0)
    data_holding_position = FloatField(default=0.0)
    data_holding_avail_position = FloatField(default=0.0)
    data_holding_avg_cost = FloatField(default=0.0)
    data_holding_settlement_price = FloatField(default=0.0)
    data_holding_leverage = StringField(ddl='varchar(10)')
    data_holding_realized_pnl = FloatField(default=0.0)
    data_holding_side = StringField(ddl='varchar(10)')
    data_holding_timestamp = StringField(ddl='varchar(30)')
    data_holding_margin = FloatField(default=0.0)
    data_holding_settled_pnl = FloatField(default=0.0)
    data_holding_last = FloatField(default=0.0)
    data_holding_maint_margin_ratio = FloatField(default=0.0)
    data_holding_open_outstanding = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_spot_account
class ori_okex_ord_spot_account(Model):
    __table__ = 'ori_okex_ord_spot_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')

    data_balance = FloatField(default=0.0)
    data_available = FloatField(default=0.0)
    data_currency = StringField(ddl='varchar(20)')
    data_id = StringField(ddl='varchar(20)')
    data_hold = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_spot_marginaccount
class ori_okex_ord_spot_marginaccount(Model):
    __table__ = 'ori_okex_ord_spot_marginaccount'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')

    instrument_id = StringField(ddl='varchar(20)')
    maint_margin_ratio = FloatField(default=0.0)
    liquidation_price = FloatField(default=0.0)
    tiers = StringField(ddl='varchar(2)')
    quotecurr = StringField(ddl='varchar(20)')
    quotecurr_available = FloatField(default=0.0)
    quotecurr_balance = FloatField(default=0.0)
    quotecurr_borrowed = FloatField(default=0.0)
    quotecurr_hold = FloatField(default=0.0)
    quotecurr_lending_fee = FloatField(default=0.0)
    basecurr = StringField(ddl='varchar(20)')
    basecurr_available = FloatField(default=0.0)
    basecurr_balance = FloatField(default=0.0)
    basecurr_borrowed = FloatField(default=0.0)
    basecurr_hold = FloatField(default=0.0)
    basecurr_lending_fee = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_spot_order
class ori_okex_ord_spot_order(Model):
    __table__ = 'ori_okex_ord_spot_order'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')

    data_client_oid = StringField(ddl='varchar(50)')
    data_price = FloatField(default=0.0)
    data_size = FloatField(default=0.0)
    data_notional = FloatField(default=0.0)
    data_instrument_id = StringField(ddl='varchar(50)')
    data_side = StringField(ddl='varchar(10)')
    data_type = StringField(ddl='varchar(10)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_filled_size = FloatField(default=0.0)
    data_filled_notional = FloatField(default=0.0)
    data_margin_trading = StringField(ddl='varchar(2)')
    data_order_type = StringField(ddl='varchar(2)')
    data_last_fill_px = FloatField(default=0.0)
    data_last_fill_id = StringField(ddl='varchar(20)')
    data_last_fill_qty = FloatField(default=0.0)
    data_last_fill_time = StringField(ddl='varchar(50)')
    data_state = StringField(ddl='varchar(2)')
    data_created_at = StringField(ddl='varchar(30)')
    data_fee_currency = StringField(ddl='varchar(20)')
    data_fee = FloatField(default=0.0)
    data_rebate_currency = StringField(ddl='varchar(20)')
    data_rebate = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# table ori_okex_ord_spot_orderalgo
class ori_okex_ord_spot_orderalgo(Model):
    __table__ = 'ori_okex_ord_spot_orderalgo'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    table = StringField(ddl='varchar(20)')

    data_algo_id = StringField(ddl='varchar(20)')
    data_algo_price = FloatField(default=0.0)
    data_cancel_code = StringField(ddl='varchar(20)')
    data_created_at = StringField(ddl='varchar(30)')
    data_instrument_id = StringField(ddl='varchar(50)')
    data_mode = StringField(ddl='varchar(2)')
    data_order_id = StringField(ddl='varchar(20)')
    data_order_type = StringField(ddl='varchar(2)')
    data_side = StringField(ddl='varchar(10)')
    data_size = StringField(ddl='varchar(10)')
    data_status = StringField(ddl='varchar(10)')
    data_stop_type = StringField(ddl='varchar(10)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_trigger_price = FloatField(default=0.0)

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

# -----------public
class ori_huobi_mkt_spot_account(Model):
    __table__ = 'ori_huobi_mkt_spot_account'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    data_id = FloatField(default=0.0)
    data_type = StringField(ddl='varchar(50)')
    data_subtype = StringField(ddl='varchar(50)')
    data_state = StringField(ddl='varchar(50)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')



class ori_huobi_mkt_spot_commonsymbol(Model):
    __table__ = 'ori_huobi_mkt_spot_commonsymbol'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    status = StringField(ddl='varchar(10)')

    data_base_currency = StringField(ddl='varchar(20)')
    data_quote_currency = StringField(ddl='varchar(20)')
    data_price_precision = FloatField(default=0.0)
    data_amount_precision = IntegerField(default=0)
    data_symbol_partition = StringField(ddl='varchar(50)')
    data_symbol = StringField(ddl='varchar(20)')
    data_state = StringField(ddl='varchar(20)')
    data_value_precision = FloatField(default=0.0)
    data_min_order_amt = FloatField(default=0.0)
    data_max_order_amt = FloatField(default=0.0)
    data_min_order_value = FloatField(default=0.0)
    data_limit_order_min_order_amt = FloatField(default=0.0)
    data_limit_order_max_order_amt = FloatField(default=0.0)
    data_sell_market_min_order_amt = FloatField(default=0.0)
    data_sell_market_max_order_amt = FloatField(default=0.0)
    data_buy_market_max_order_value = FloatField(default=0.0)
    
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')


class ori_huobi_mkt_spot_historykline(Model):
    __table__ = 'ori_huobi_mkt_spot_historykline'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    ch = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(20)')
    ts = IntegerField(default=0)

    symbol = StringField(ddl='varchar(20)')
    period = StringField(ddl='varchar(20)')
    data_id = IntegerField(default=0)
    data_open = FloatField(default=0.0)
    data_close = FloatField(default=0.0)
    data_low = FloatField(default=0.0)
    data_high = FloatField(default=0.0)
    data_amount = FloatField(default=0.0)
    data_vol = FloatField(default=0.0)
    data_count = FloatField(default=0.0)
    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

class ori_okex_mkt_spottrade(Model):
    __table__ = 'ori_okex_mkt_spottrade'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    table = StringField(ddl='varchar(50)')
    data_trade_id = StringField(ddl='varchar(20)')
    data_price = FloatField(default=0.0)
    data_size = FloatField(default=0.0)
    data_side = StringField(ddl='varchar(20)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_instrument_id = StringField(ddl='varchar(50)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

class ori_okex_mkt_delitrade(Model):
    __table__ = 'ori_okex_mkt_delitrade'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    table = StringField(ddl='varchar(50)')
    data_trade_id = StringField(ddl='varchar(20)')
    data_price = FloatField(default=0.0)
    data_qty = FloatField(default=0.0)
    data_side = StringField(ddl='varchar(20)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_instrument_id = StringField(ddl='varchar(50)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

class ori_okex_mkt_perptrade(Model):
    __table__ = 'ori_okex_mkt_perptrade'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    table = StringField(ddl='varchar(50)')
    data_trade_id = StringField(ddl='varchar(20)')
    data_price = FloatField(default=0.0)
    data_size = FloatField(default=0.0)
    data_side = StringField(ddl='varchar(20)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_instrument_id = StringField(ddl='varchar(50)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

class ori_okex_mkt_opttrade(Model):
    __table__ = 'ori_okex_mkt_opttrade'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')

    table = StringField(ddl='varchar(50)')
    data_trade_id = StringField(ddl='varchar(20)')
    data_price = FloatField(default=0.0)
    data_qty = FloatField(default=0.0)
    data_side = StringField(ddl='varchar(20)')
    data_timestamp = StringField(ddl='varchar(50)')
    data_instrument_id = StringField(ddl='varchar(50)')

    create_ts = IntegerField(default=0)
    acc_key = StringField(ddl='varchar(100)')

class paraspace_generic_events(Model):
    __table__ = 'paraspace_generic_events'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    created_at = StringField(ddl='varchar(20)')
    updated_at = StringField(ddl='varchar(20)')
    from0x = StringField(ddl='varchar(50)')
    to0x = StringField(ddl='varchar(50)')
    tx_hash = StringField(ddl='varchar(80)')
    event_index = IntegerField(default=0)
    block_numbe = IntegerField(default=0)
    block_time = StringField(ddl='varchar(20)')
    event_type = StringField(ddl='varchar(50)')
    reserve = StringField(ddl='varchar(50)')
    user0x = StringField(ddl='varchar(50)')
    amount = StringField(ddl='varchar(254)')
    price = StringField(ddl='varchar(254)')
    usd_value = FloatField(default=0.0)
    event_body = StringField(ddl='varchar(254)')
