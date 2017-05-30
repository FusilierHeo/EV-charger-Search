
#-*- coding: utf-8 -*-
import urllib.request

from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree


server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"


def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(600)+'&pageNo='+str(1) +'&addr='
    request=server+data

    print(request)
    return request


def LoadPoint(item):
    dic = {}
    dic["충전소 명"] = item.find("csNm").text
    dic["주소"]=item.find("addr").text
    dic["충전기 타입"]=item.find("chargeTp").text
    #dic["cpName"]=item.find("cpNm").text
    dic["현재 상태"]=item.find("cpStat").text
    #dic["type2"]=item.find("cpTp").text
    dic["위도"]=item.find("lat").text
    dic["경도"]=item.find("longi").text
    dic["시간"]=item.find("statUpdateDatetime").text
    return dic


class ChargingStation:
    def __init__(self, station):
        url = urlBuilder(server, serviceKey)
        data = urllib.request.urlopen(url).read()

        u=data.translate(None, b'\r\n')
        u=u.decode('utf-8')
        u=u.replace("10000","")
        u = u.replace("c55b", "")
        #print(u.len())
        '''
        .translate(None, b'ff16\r\n')
        \r\n10000\r\n
        \r\nc55b\r\n
        \r\n0\r\n\r\n
        '''
        tree = ElementTree.fromstring(u[4:-1])
        #print(data[6:32253])
        #tree = ElementTree.fromstring(data[6:32253])

       # tree=ElementTree.parse('tdata.xml')


        itemElement = list(tree.iter("item"))

        for item in itemElement:
            item.find("addr").text
            tmp = LoadPoint(item)
            station.append(tmp)


    def printList(self, station):
        for i in station:
            print(i)

    def searchList(self, station, add, list):
        list.clear()
        for i in station:
            if add in i["주소"]:
                list.append(i)
