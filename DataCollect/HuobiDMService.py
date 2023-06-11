#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 20180917
# @Author  : zhaobo
# @github  : 

from DataCollect.HuobiDMUtil import http_tron_get_request, http_get_request, api_key_post,api_key_get, api_key_post_temp,api_key_get_yantoken
import DataCollect.DataMem
import configparser
import glob



class HuobiDM:

    def __init__(self,url,access_key,secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__dataMem = DataCollect.DataMem

    
    '''
    ======================
    Market data API
    ======================
    '''

    # 获取币本位永续合约信息 add by xuj
    def get_swap_contract_info(self, contract_code=''):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_contract_info'

        return http_get_request(url, params)

    # 获取合约信息
    def get_contract_info(self, symbol='', contract_type='', contract_code=''):
        """
        参数名称         参数类型  必填    描述
        symbol          string  false   "BTC","ETH"...
        contract_type   string  false   合约类型: this_week:当周 next_week:下周 quarter:季度
        contract_code   string  false   BTC181228
        备注：如果contract_code填了值，那就按照contract_code去查询，如果contract_code 没有填值，则按照symbol+contract_type去查询
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        if contract_type:
            params['contract_type'] = contract_type
        if contract_code:
            params['contract_code'] = contract_code
    
        url = self.__url + '/api/v1/contract_contract_info'
        return http_get_request(url, params)
    
    
    # 获取合约指数信息
    def get_contract_index(self, symbol=''):
        """
        :symbol    "BTC","ETH"...
        """
        params = {'symbol': symbol}
    
        url = self.__url + '/api/v1/contract_index'
        return http_get_request(url, params)
    
    
    # 获取合约最高限价和最低限价
    def get_contract_price_limit(self, symbol='', contract_type='', contract_code=''):
        """
        :symbol          "BTC","ETH"...
        :contract_type   合约类型: this_week:当周 next_week:下周 quarter:季度
        "contract_code   BTC180928
        备注：如果contract_code填了值，那就按照contract_code去查询，如果contract_code 没有填值，则按照symbol+contract_type去查询
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        if contract_type:
            params['contract_type'] = contract_type
        if contract_code:
            params['contract_code'] = contract_code
    
        url = self.__url + '/api/v1/contract_price_limit'
        return http_get_request(url, params)
    
    
    # 获取当前可用合约总持仓量
    def get_contract_open_interest(self, symbol='', contract_type='', contract_code=''):
        """
        :symbol          "BTC","ETH"...
        :contract_type   合约类型: this_week:当周 next_week:下周 quarter:季度
        "contract_code   BTC180928
        备注：如果contract_code填了值，那就按照contract_code去查询，如果contract_code 没有填值，则按照symbol+contract_type去查询
        """
        params = {'symbol': symbol,
                  'contract_type': contract_type,
                  'contract_code': contract_code}
    
        url = self.__url + '/api/v1/contract_open_interest'
        return http_get_request(url, params)   
        
    
    # 获取行情深度
    def get_contract_depth(self, symbol, type):
        """
        :param symbol:   BTC_CW, BTC_NW, BTC_CQ , ...
        :param type: 可选值：{ step0, step1, step2, step3, step4, step5 （合并深度0-5）；step0时，不合并深度 }
        :return:
        """
        params = {'symbol': symbol,
                  'type': type}
    
        url = self.__url + '/market/depth'
        return http_get_request(url, params)
    
    # 获取行情深度 add by xuj
    def get_depth(self, symbol, type):
        """
        :param symbol:   btcusdt, bchbtc, rcneth ...
        :param type: 可选值：{ step0, step1, step2, step3, step4, step5 （合并深度0-5）；step0时，不合并深度 }
        :return:
        """
        params = {'symbol': symbol,
                  'type': type}
    
        url = self.__url + '/market/depth'
        if type=='step0':
            self.__dataMem.setDepth_step0(http_get_request(url, params))
            return self.__dataMem.getDepth_step0()
        else:
            return self.__dataMem.getDepth_step0()
    
    # 获取KLine
    def get_contract_kline(self, symbol, period, size=150):
        """
        :param symbol  BTC_CW, BTC_NW, BTC_CQ , ...
        :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1week, 1mon }
        :param size: [1,2000]
        :return:
        """
        params = {'symbol': symbol,
                  'period': period}
        if size:
            params['size'] = size
    
        url = self.__url + '/market/history/kline'
        return http_get_request(url, params)

    # 获取KLine add by xuj
    def get_kline(self, symbol, period, size=1000):
        """
        :param symbol  btcusdt, bchbtc, rcneth , ...
        :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
        :param size: [1,2000]
        :return:
        :status {"ok" , "error"}
        :ts 响应生成时间点，单位：毫秒
        :tick  KLine 数据
        :ch 数据所属的 channel，格式： market.$symbol.kline.$period
        """
        params = {'symbol': symbol,
                  'period': period}
        if size:
            params['size'] = size

        url = self.__url + '/market/history/kline'
        reqObj=http_get_request(url, params)
        # the history problem default symbol = btc, period = 15m or 1d
        if period==period1m and symbol=="btcusdt":
            self.__dataMem.setKline_1m(reqObj)
            return self.__dataMem.getKline_1m()
        elif period==period1d and symbol=="btcusdt":
            self.__dataMem.setKline1day(reqObj)
            return self.__dataMem.getKline1day()
        # save the diff kline by symbol and period
        strKey="huob_data_kline_"+symbol+period
        self.__dataMem.setTmp(strKey,reqObj)
        return self.__dataMem.getTmp(strKey)

    # 获取 c2c market orderbook
    def get_c2cOrderBook(self, symbol):
        url = self.__url + symbol
        params = {}
        reqObj=http_get_request(url, params)

        strKey='get_c2cOrderBook'
        if "result" in reqObj and "asks" in reqObj and "bids" in reqObj:
            self.__dataMem.setTmp(strKey, reqObj)
            return self.__dataMem.getTmp(strKey)
        else:
            return "there are not the key"


    # 获取 currencys add by xuj
    def get_currencys(self):
        params = {'symbol': ''}
        url = self.__url + '/v1/common/symbols'
        self.__dataMem.setCurrencys(http_get_request(url,params))
        return self.__dataMem.getCurrencys()

    def get_exchangeInfo(self):
        params = {'symbol': ''}
        url= 'https://api.binance.com/api/v1/exchangeInfo'
        return http_get_request(url,params)

    # 获取 tickers add by xuj
    def get_tickers(self):
        params = {'symbol': ''}
        url = self.__url + '/market/tickers'
        self.__dataMem.setTickers(http_get_request(url,params))
        return self.__dataMem.getTickers()

    # 获取 tickers add by xuj
    def get_tmp(self,urlIn=''):
        url = urlIn
        return http_get_request(url,None)

    def http_tron_get_request(self, _url='', _apikey="", params=None):
        return http_tron_get_request(url=_url, params=params, add_to_headers=None, _apikey=_apikey)

    # 获取聚合行情
    def get_contract_market_merged(self, symbol):
        """
        :symbol	    "BTC_CW","BTC_NW", "BTC_CQ" ...
        """
        params = {'symbol': symbol}
    
        url = self.__url + '/market/detail/merged'
        return http_get_request(url, params)
    
    
    # 获取市场最近成交记录
    # 好像size不起作用？只能取到最近一条成交记录？
    def get_contract_trade(self, symbol, size=1):
        """
        :param symbol: 可选值：{ BTC_CW, BTC_NW, BTC_CQ, etc. }
        :return:
        """
        params = {'symbol': symbol,
                  'size' : size}
    
        url = self.__url + '/market/trade'
        return http_get_request(url, params)
    
    
    # 批量获取最近的交易记录
    def get_contract_batch_trade(self, symbol, size=1):
        """
        :param symbol: 可选值：{ BTC_CW, BTC_NW, BTC_CQ, etc. }, size: int
        :return:
        """
        params = {'symbol': symbol,
                  'size' : size}
    
        url = self.__url + '/market/history/trade'
        return http_get_request(url, params)
    
    
    
    
    
    
    '''
    ======================
    Trade/Account API
    ======================
    '''
    
    # 获取用户账户信息
    def get_contract_account_info(self, symbol=''):
        """
        :param symbol: "BTC","ETH"...如果缺省，默认返回所有品种
        :return:
        """
        
        params = {}
        if symbol:
            params["symbol"] = symbol
    
        request_path = '/api/v1/contract_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # 获取用户持仓信息
    def get_contract_position_info(self, symbol=''):
        """
        :param symbol: "BTC","ETH"...如果缺省，默认返回所有品种
        :return:
        """
        
        params = {}
        if symbol:
            params["symbol"] = symbol
    
        request_path = '/api/v1/contract_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # get fee rate spot add by xuj
    def get_spot_fee(self, symbols=''):
        params = {}
        if symbols:
            params["symbols"] = symbols

        request_path = '/v2/reference/transact-fee-rate'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # get loan info spot add by xuj
    def get_loan_info(self):
        params = {}
        request_path = '/v1/margin/loan-info'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # get loan info spot add by xuj
    def get_loan_account(self):
        params = {}
        request_path = '/v1/margin/accounts/balance'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # get lev rate contract add by xuj
    def get_contract_lev(self):
        params = {}
        request_path = '/api/v1/contract_available_level_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # get fee rate contract add by xuj
    def get_contract_fee(self):
        params = {}
        request_path = '/api/v1/contract_fee'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户持仓信息 add by xuj
    def get_account(self, symbol=''):
        """
        :param symbol: "BTC","ETH"...如果缺省，默认返回所有品种
        :return:
        """

        params = {}
        if symbol:
            params["symbol"] = symbol

        request_path = '/v1/account/accounts'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # 获取用户持仓信息 add by xuj
    def get_perpetual_account(self):
        params = {}
        request_path = '/swap-api/v1/swap_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户持仓信息 add by xuj
    def post_contract_sub_account_list(self):
        params = {}
        request_path = '/api/v1/contract_sub_account_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # get the ETF info
    def get_ETF(self):
        params = {}
        request_path = '/etf/swap/config'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    def get_c2c_offers(self,offerStatus=''):
        params = {}
        params["offerStatus"] = offerStatus
        request_path = '/v2/c2c/offers'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # balance add by xuj
    def get_balance(self, account_id=''):
        """
        :param symbol: "account-id"
        :return:
        """

        params = {}
        if account_id:
            params["account-id"] = account_id

        #request_path = '/v1/account/accounts/{account-id}/balance'
        request_path = "/v1/account/accounts/{0}/balance".format(account_id)
        self.__dataMem.setBalance(api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key))
        return self.__dataMem.getBalance()

    # account his add by xuj
    def get_account_his(self, account_id=''):
        params = {}
        if account_id:
            params["account-id"] = account_id
        request_path = "/v1/account/history"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # ledger add by xuj
    def get_ledger_his(self, account_id=''):
        params = {}
        if account_id:
            params["accountId"] = account_id
        request_path = "/v2/account/ledger"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # deposit and withdraw his add by xuj
    def get_dep_withd_his(self, type='' ):
        params = {}
        if type:
            params["type"] = type
        request_path = "/v1/query/deposit-withdraw"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # query the sub user add by xuj
    def get_subUser_his(self):
        params = {}
        request_path = "/v2/sub-user/user-list"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    def get_c2c_account(self,accID):
        params = {}
        if accID:
            params["accountId"] = accID
        request_path = "/v2/c2c/account"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    def get_stablecoin_quote(self,currency,amount,type):
        params = {}
        if currency:
            params["currency"] = currency
            params["amount"] = amount
            params["type"] = type
        request_path = "/v1/stable-coin/quote"
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # 合约下单
    def send_contract_order(self, symbol, contract_type, contract_code, 
                            client_order_id, price,volume,direction,offset,
                            lever_rate,order_price_type):
        """
        :symbol: "BTC","ETH"..
        :contract_type: "this_week", "next_week", "quarter"
        :contract_code: "BTC181228"
        :client_order_id: 客户自己填写和维护，这次一定要大于上一次
        :price             必填   价格
        :volume            必填  委托数量（张）
        :direction         必填  "buy" "sell"
        :offset            必填   "open", "close"
        :lever_rate        必填  杠杆倍数
        :order_price_type  必填   "limit"限价， "opponent" 对手价
        备注：如果contract_code填了值，那就按照contract_code去下单，如果contract_code没有填值，则按照symbol+contract_type去下单。
        :
        """
        
        params = {"price": price,
                  "volume": volume,
                  "direction": direction,
                  "offset": offset,
                  "lever_rate": lever_rate,
                  "order_price_type": order_price_type}
        if symbol:
            params["symbol"] = symbol
        if contract_type:
            params['contract_type'] = contract_type
        if contract_code:
            params['contract_code'] = contract_code
        if client_order_id:
            params['client_order_id'] = client_order_id
    
        request_path = '/api/v1/contract_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # add by xuj for perp order
    def send_perp_order(self,contract_code,client_order_id,price,volume,direction,offset,lever_rate,order_price_type):
        params = {"contract_code": contract_code,
                  "client_order_id": client_order_id,
                  "price": price,
                  "volume": volume,
                  "direction": direction,
                  "offset": offset,
                  "lever_rate": lever_rate,
                  "order_price_type": order_price_type}
        request_path = '/swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # 下单 add by xuj
    def send_order(self, account_id, amount,price,source='',symbol='',type='',client_order_id=''):
        """
        account-id,
        amount, btc/usdt amount=amount of btc
        price,source,symbol,type

        """

        params = {"account-id": account_id,"amount": amount,
                  "price": price,"source": source, "symbol": symbol,"type": type}
        if account_id:
            params["account-id"] = account_id
        if amount:
            params['amount'] = amount
        if price:
            params['price'] = price
        if source:
            params['source'] = source
        if symbol:
            params['symbol'] = symbol
        if type:
            params['type'] = type
        if client_order_id:
            params['client-order-id'] = client_order_id

        request_path = '/v1/order/orders/place'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 合约批量下单
    def send_contract_batchorder(self, orders_data):
        """
        orders_data: example:
        orders_data = {'orders_data': [
               {'symbol': 'BTC', 'contract_type': 'quarter',  
                'contract_code':'BTC181228',  'client_order_id':'', 
                'price':1, 'volume':1, 'direction':'buy', 'offset':'open', 
                'leverRate':20, 'orderPriceType':'limit'},
               {'symbol': 'BTC','contract_type': 'quarter', 
                'contract_code':'BTC181228', 'client_order_id':'', 
                'price':2, 'volume':2, 'direction':'buy', 'offset':'open', 
                'leverRate':20, 'orderPriceType':'limit'}]}    
            
        Parameters of each order: refer to send_contract_order
        """
        
        params = orders_data
        request_path = '/api/v1/contract_batchorder'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 撤销订单
    def cancel_contract_order(self, symbol, order_id='', client_order_id=''):
        """
        参数名称          是否必须 类型     描述
        symbol           true   string  BTC, ETH, ...
        order_id	         false  string  订单ID（ 多个订单ID中间以","分隔,一次最多允许撤消50个订单 ）
        client_order_id  false  string  客户订单ID(多个订单ID中间以","分隔,一次最多允许撤消50个订单)
        备注： order_id 和 client_order_id都可以用来撤单，同时只可以设置其中一种，如果设置了两种，默认以order_id来撤单。
        """
        
        params = {"symbol": symbol}
        if order_id:
            params["order_id"] = order_id
        if client_order_id:
            params["client_order_id"] = client_order_id  
    
        request_path = '/api/v1/contract_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 全部撤单
    def cancel_all_contract_order(self, symbol):
        """
        symbol: BTC, ETH, ...
        """
        
        params = {"symbol": symbol}
    
        request_path = '/api/v1/contract_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取合约订单信息
    def get_contract_order_info(self, symbol, order_id='', client_order_id=''):
        """
        参数名称	        是否必须	类型	    描述
        symbol          true    string  BTC, ETH, ...
        order_id	        false	string	订单ID（ 多个订单ID中间以","分隔,一次最多允许查询20个订单 ）
        client_order_id	false	string	客户订单ID(多个订单ID中间以","分隔,一次最多允许查询20个订单)
        备注：order_id和client_order_id都可以用来查询，同时只可以设置其中一种，如果设置了两种，默认以order_id来查询。
        """
        
        params = {"symbol": symbol}
        if order_id:
            params["order_id"] = order_id
        if client_order_id:
            params["client_order_id"] = client_order_id  
    
        request_path = '/api/v1/contract_order_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户合约账户财务记录
    def get_financial_his(self, symbol=''):
        params = {}
        if symbol:
            params["symbol"] = symbol
        request_path = '/api/v1/contract_financial_record'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取合约订单信息 add by xuj
    def get_order_info(self, symbol, types='', start_date='',end_date='',states='',from1='',direct='',size=5):
        """
        symbol: btcusdt
        types: buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖, buy-ioc：IOC买单, sell-ioc：IOC卖单
        start-date
        end-date
        states
        from
        """

        params = {"symbol": symbol,
                  "types":types,
                  "start-date": start_date,
                  "end-date": end_date,
                  "states": states,
                  "from": from1,
                  "direct": direct,
                  "size": size
                  }
        if symbol:
            params["symbol"] = symbol
        if types:
            params["types"] = types
        if start_date:
            params["start-date"] = start_date
        if end_date:
            params["end-date"] = end_date
        if states:
            params["states"] = states
        if from1:
            params["from"] = from1
        if direct:
            params["direct"] = direct
        if size:
            params["size"] = size

        request_path = '/v1/order/orders'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # cancel order by id  add by xuj
    def post_cancel_order(self, order_id=''):
        """
        order-id
        """

        params = {"order-id": order_id,
                  }
        if order_id:
            params["order-id"] = order_id

        #request_path = '/v1/order/orders/{order-id}/submitcancel'
        request_path = '/v1/order/orders/{0}/submitcancel'.format(order_id)
        #request_path = "/v1/account/accounts/{0}/balance".format(order_id)
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    # 获取合约订单明细信息
        
    def get_contract_order_detail(self, symbol, order_id, page_index=None, page_size=None):
        """
        参数名称     是否必须  类型    描述
        symbol      true	    string "BTC","ETH"...
        order_id    true	    long	   订单id
        page_index  false   int    第几页,不填第一页
        page_size   false   int    不填默认20，不得多于50
        """
        
        params = {"symbol": symbol,
                  "order_id": order_id}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/api/v1/contract_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取合约当前未成交委托
    def get_contract_open_orders(self, symbol=None, page_index=None, page_size=None):
        """
        参数名称     是否必须  类型   描述
        symbol      false   string "BTC","ETH"...
        page_index  false   int    第几页,不填第一页
        page_size   false   int    不填默认20，不得多于50
        """
        
        params = {}
        if symbol:
            params["symbol"] = symbol
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/api/v1/contract_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)
    
    
    # 获取合约历史委托
    def get_contract_history_orders(self, symbol, trade_type, type, status, create_date,
                                    page_index=None, page_size=None):
        """
        参数名称     是否必须  类型     描述	    取值范围
        symbol      true	    string  品种代码  "BTC","ETH"...
        trade_type  true	    int     交易类型  0:全部,1:买入开多,2: 卖出开空,3: 买入平空,4: 卖出平多,5: 卖出强平,6: 买入强平,7:交割平多,8: 交割平空
        type        true	    int     类型     1:所有订单、2：结束汏订单
        status      true	    int     订单状态  0:全部,3:未成交, 4: 部分成交,5: 部分成交已撤单,6: 全部成交,7:已撤单
        create_date true	    int     日期     7，90（7天或者90天）
        page_index  false   int     页码，不填默认第1页		
        page_size   false   int     不填默认20，不得多于50
        """
        
        params = {"symbol": symbol,
                  "trade_type": trade_type,
                  "type": type,
                  "status": status,
                  "create_date": create_date}
        if page_index:
            params["page_index"] = page_index
        if page_size:
            params["page_size"] = page_size  
    
        request_path = '/api/v1/contract_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # add by xuj for temp https://api.yantoken.io
    def get_temp(self, symbol):
        params = {"symbol": symbol,
                  "limit": 10}

        params_temp = {}

        request_path = '/openapi/option/v1/myTrades'
        return api_key_post_temp(self.__url, request_path, params_temp, self.__access_key, self.__secret_key)


    # add by xuj for temp https://api.yantoken.io
    # 获取用户账户信息 add by xuj
    def get_account_yantoken(self):
        params = {}
        request_path = '/openapi/contract/v1/account'
        return api_key_get_yantoken(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # add by xuj for temp https://api.yantoken.io
    # 获取用户持仓信息 add by xuj
    def get_positions_yantoken(self,symbol=None,side=None):
        params = {}
        if symbol:
            params["symbol"] = symbol
        if side:
            params["side"] = side
        request_path = '/openapi/contract/v1/positions'
        return api_key_get_yantoken(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # add by xuj for temp https://api.yantoken.io
    # 获取标的指数价格信息 add by xuj
    def get_index_yantoken(self,symbol=None):
        params = {}
        if symbol:
            params["symbol"] = symbol
        request_path = '/openapi/quote/v1/contract/index'
        return api_key_get_yantoken(self.__url, request_path, params, self.__access_key, self.__secret_key)
