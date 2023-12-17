import urllib.request
import useragent
import random
import urllib3
from random import *
import requests
import csv
import re
import time
import lxml
from lxml import etree
import json


if __name__ == '__main__':
    data = []
    Comment = []
    User = []
    Point = []
    urls = [
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r925876856-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r757296659-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r739402703-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r720611707-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r714747571-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r677250852-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r665019994-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r653892056-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r645128324-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r634622064-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r618406613-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r606596601-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r599775803-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r592906579-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r589458903-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r589279422-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r582127592-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r581951032-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r568843367-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r563302925-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r555761950-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r545402297-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r538197567-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r534291649-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r520377686-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r517087718-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r515739678-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r502442429-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r497417221-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r496721120-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r488194618-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r474375776-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r469070970-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r463099489-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r458455975-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r454932478-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r443216474-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r440834955-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r433860906-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r429027982-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r426076183-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r423450535-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r421997409-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r415633333-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r413824889-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r407393044-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r385501832-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r381074928-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r376875496-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r373247424-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r368672123-China_Southern_Airlines-World.html",
        "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r366806384-China_Southern_Airlines-World.html"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        "Referer": 'https://cn.tripadvisor.com/'
    }

    for url in urls:
        user_name_list = []
        comment_list = []
        point_list = []
        print(url)
        response = requests.get(url=url, headers=headers)
        print(response.status_code)
        while len(user_name_list) == 0:
            page_text = requests.get(url=url, headers=headers).text
            # <p class ="partial_entry" > </p>
            ex2 = '<div class="username mo">.*?>(.*?)<.*?</div>'
            user_name_list = re.findall(ex2, page_text, re.S)
            print(user_name_list)

            ex1 = '<div class="entry"><p class="partial_entry">(.*?)</p></div>'
            comment_list = re.findall(ex1, page_text, re.S)  # re.S单行匹配，re.M多行匹配
            print(comment_list)

            ex3 = '<span class="ui_bubble_rating bubble_(.*?)0">.*?</span>'
            point_list = re.findall(ex3, page_text)
            print(point_list)
            time.sleep(10)

        Point = Point + point_list
        User = User + user_name_list
        Comment = Comment + comment_list

    f = open("中国南方航空1.csv", "w", encoding="utf-8-sig", newline="")
    csvwritter = csv.writer(f)

    for i in range(len(Comment)):
        data = [User[i]] + [Point[i]] + [Comment[i]]
        csvwritter.writerow(data)
    # with open('./pinglun.html','wb',encoding='utf') as fp:
    #    fp.write(page_text)
    print('over')
'''
urls = ["https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r804465644-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r752355879-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r737740387-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r713797386-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r694952521-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r688847280-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r687379973-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r678441865-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r666681432-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r658688935-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r652860536-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r645665547-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r626322646-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r621607653-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r617856065-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r608716917-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r600276910-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r595149023-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r584529382-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r578713306-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r573634740-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r567785070-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r563120260-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r558750408-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r557664387-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r554120054-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r552626367-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r551910518-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r549226481-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r546743130-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r544713918-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r541495621-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r538923195-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r531259639-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r519722941-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r518208338-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r515902125-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r515744979-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r500582495-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r497044242-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r495287011-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r488839117-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r480778944-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r473728397-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r467112233-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r458814401-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r456826571-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r453249207-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r447831932-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r442297927-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r438474224-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r434715815-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r431450416-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r427124451-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r423837075-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r424889553-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r424889183-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r420779077-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r416334088-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r407394748-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r393473939-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r387741039-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r378548370-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r373632075-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r371115852-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r369133166-Air_China-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r360312517-Air_China-World.html"]  中国国际航空urls
'''

'''
    urls = ["https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r913438413-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r733683100-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r719785838-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r711259778-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r700149959-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r688674966-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r683079844-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r678820521-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r669549329-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r663956963-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r658362401-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r655124202-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r652458941-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r643914278-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r641762529-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r638312588-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r633718182-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r625242901-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r617560374-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r614006356-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r603953782-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r597578421-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r589897518-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r584041211-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r580546430-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r575338609-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r567189222-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r563517592-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r557304384-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r555072849-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r551663617-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r547819985-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r546984546-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r544533968-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r539285740-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r533818668-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r523086084-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r519702866-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r519721015-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r516130223-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r515902240-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r515740340-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r514599207-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r505671772-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r498804645-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r497042603-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r490660593-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r485328730-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r479641695-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r476658532-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r474859815-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r470477286-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r463374970-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r460272098-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r454932488-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r449135365-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r447645811-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r441463417-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r437738756-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r431741418-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r427479904-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r424952922-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r423000453-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r421116469-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r413452239-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r406422768-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r401556396-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r387289696-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r381284218-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r377268177-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r372784349-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r371116261-China_Eastern_Airlines-World.html",
            "https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r365344091-China_Eastern_Airlines-World.html","https://cn.tripadvisor.com/ShowUserReviews-g1-d8729050-r928765590-China_Eastern_Airlines-World.html"]
            中国东方航空urls
'''

'''
urls =[
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r925876856-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r757296659-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r739402703-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r720611707-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r714747571-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r677250852-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r665019994-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r653892056-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r645128324-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r634622064-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r618406613-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r606596601-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r599775803-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r592906579-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r589458903-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r589279422-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r582127592-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r581951032-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r568843367-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r563302925-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r555761950-China_Southern_Airlines-World.html"，
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r545402297-China_Southern_Airlines-World.html"，
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r538197567-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r534291649-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r520377686-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r517087718-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r515739678-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r502442429-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r497417221-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r496721120-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r488194618-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r474375776-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r469070970-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r463099489-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r458455975-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r454932478-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r443216474-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r440834955-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r433860906-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r429027982-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r426076183-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r423450535-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r421997409-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r415633333-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r413824889-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r407393044-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r385501832-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r381074928-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r376875496-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r373247424-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r368672123-China_Southern_Airlines-World.html",
"https://cn.tripadvisor.com/ShowUserReviews-g1-d8729051-r366806384-China_Southern_Airlines-World.html",

]-中国南方航空公司url
'''
# UA_list = [
#     "Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36",
#     "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M351 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/31.0.1650.18 Mobile/11B554a Safari/8536.25",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"]

