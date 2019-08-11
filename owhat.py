import urllib.request, urllib
import requests
import time
import string,json

raiseID = 67655

def getOwhatRankingList(raiseID,page):
    headers = {
        'host':'m.owhat.cn',
        'content-type':'application/x-www-form-urlencoded'
    }
    params = {
        'cmd_s': 'shop.goods',
        'cmd_m': 'findrankingbygoodsid',
        'v': '5.5.0',
        'client': '{"platform":"mobile", "version":"5.5.0", "deviceid":"xyz", "channel":"owhat"}',
        'data': '{ "goodsid":"'+ str(raiseID) +'", "pagenum":'+str(page)+', "pagesize":20 }'
    }

    url = "https://m.owhat.cn/api?requesttimestap=" + str(int(time.time()*1000))

    response = requests.post(url,params,json=True,headers=headers)

    print(url)

    resJsonData = response.json()
    rankingList = resJsonData['data']['rankinglist']
    resultList = []
    for thisItem in rankingList:
        resultList.append(rankingModel(thisItem['nickname'],thisItem['number'],thisItem['userid'],thisItem['amount']))
    
    return resultList

def getOwhatSales(raiseID):
    headers = {
        'host':'m.owhat.cn',
        'content-type':'application/x-www-form-urlencoded'
    }
    params = {
        'cmd_s': 'shop.price',
        'cmd_m': 'findPricesAndStock',
        'v': '5.5.0',
        'client': '{"platform":"mobile", "version":"5.5.0", "deviceid":"xyz", "channel":"owhat"}',
        'data': '{ "fk_goods_id":"'+str(raiseID)+'"}'
    }

    url = "https://m.owhat.cn/api?requesttimestap=" + str(int(time.time()*1000))

    response = requests.post(url,params,json=True,headers=headers)

    print(url)

    resJsonData = response.json()
    rankingList = resJsonData['data']['prices']
    resultList = []
    for thisItem in rankingList:
        resultList.append(rankingModel(thisItem['name'],thisItem['price'],thisItem['salestock'],thisItem['remainstock']))
    
    return resultList

class rankingModel(object):
    def __init__(self,nickname,rank,userid,amount):
        self.nickname = nickname
        self.rank = rank
        self.userid = userid
        self.amount = amount

class salesModel(object):
    def __init__(self,name,price,salestock,remainstock):
        self.name = name
        self.price = price
        self.salestock = salestock
        self.remainstock = remainstock
