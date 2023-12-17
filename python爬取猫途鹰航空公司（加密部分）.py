import requests
import csv
import re
import bs4
import time
from lxml import html
from lxml import etree
#from lxml import etree
#etree=html.etree
import json
texts_list=[]
data = []
Comment = []
User = []
Point = []

# urls = ['https://cn.tripadvisor.com/OverlayWidgetAjax?Mode=EXPANDED_HOTEL_REVIEWS&metaReferer=ShowUserReviews',-中国国际航空
#         'https://cn.tripadvisor.com/OverlayWidgetAjax?Mode=EXPANDED_HOTEL_REVIEWS&metaReferer=ShowUserReviews',-中国东方航空
#         '']
url = 'https://cn.tripadvisor.com/OverlayWidgetAjax?Mode=EXPANDED_HOTEL_REVIEWS&metaReferer=ShowUserReviews'

Reviews=[
        '757582248','716685262','694952005','694379453','714747571','676786134',
        '669158895','666669687','677250852','660122615','659878084','657781687',
        '665019994','649656398','653892056','639721278','637606448','645128324',
        '634622064','616918450','616670691','616209687','618406613','606691959',
        '604280177','603289637','602060319','598822074','593221675','583624068',
        '582178456','579014971','569257921','581951032','567651378','568843367',
        '562903715','561688451','544206009','543143080','537602243','534291649',
        '515902234','515519184','517087718','513659670','502442429','496494855',
        '497417221','490968262','482871653','482871653','474050503','470488417',
        '470477294','467194272','464993075','469070970','460620100','458862468',
        '458645990','458040687','457819219','457314824','458455975','454221838',
        '449135218','447967542','454932478','447083792','441504547','440834336',
        '440080658','436088187','434760478','440834955','432612850','429130756',
        '426897380','424952924','424952815','426076183','423082333','422748849',
        '421997796','423450535','418759136','418759083','416733970','421997409',
        '415546391','415632171','415320722','415179506','415633333','413824888',
        '412203829','407393092','413824889','399122173','407393044','385501139',
        '385215142','383909792','381825587','385501832','376882106','376878522',
        '381074928','373632439','373311701','373023477','372310529','376875496',
        '371115919','371115866','370868416','370066983','368672110','368404930',
        '368403980','367151585','368672123','366806384'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Referer':'https://cn.tripadvisor.com/ShowUserReviews-g1-d8729000-r804465644-Air_China-World.html',
    'Cookie':'TASameSite=1; TAUnique=%1%enc%3AjYF91P0b3tpHAsDhghvm73quG5OSFSRMrBKphU8KzJ4IFRzS%2B6QwHUJAswmwMYgfNox8JbUSTxk%3D; TASSK=enc%3AAAfbh%2FgFEeLvpTf2p7Mlgy1xUfavdwJVXugyNjt1LVJz2p27lmWU1x2EpQjtQjqGuIRVvCkc%2FIsCl97GWZV9%2FfiR1GQslqAb4FPUPaUQ%2FehQyWuSS1OVqPqEHltcl8fO%2Bw%3D%3D; TART=%1%enc%3ALIlNnjMq3x9GPrk38Yt3CmYafRkYCb9CaffJ7Btcn0coScy85kXUfTlElFh4k3ttmEKXuc1TgSo%3D; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; _ga=GA1.1.1385501347.1702261526; pbjs_sharedId=19bfacdd-b943-47db-8bcf-fd55c33e9e3c; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; _lc2_fpi=b140173de591--01hhbb3883xmythh3efx6r6xj1; _lc2_fpi_meta=%7B%22w%22%3A1702261530883%7D; _lr_env_src_ats=false; pbjs_unifiedID=%7B%22TDID%22%3A%2221cadc02-4c5f-40bc-ab00-1a7fce1ec976%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-11T02%3A25%3A39%22%7D; pbjs_unifiedID_cst=zix7LPQsHA%3D%3D; TATravelInfo=V2*AY.2023*AM.12*AD.24*DY.2023*DM.12*DD.25*A.2*MG.-1*HP.2*FL.3*DSM.1702267617872*RS.1; TALanguage=zhCN; VRMCID=%1%V1*id.10570*llp.%2FAirline_Review-d8729050-Reviews-China-Eastern-Airlines*e.1702977772414; TADCID=LMk2uZG0BBT1l926ABQCCKy0j55CTpGVsECjuwJMq3o1EQj9ai3WnZmNKx6tleGxwKC1s6EiTpfy5DnNctx2_ry6M_7VuuBGytY; PAC=AEImXkdTff9gXe8V_YqcyNkyHmNAJoV7jHTeYzFbaEDwiif6tCbNJVZoKMYMyFrzDvNVssGQptncNHq1M-FpaLpZ7yftNJPoKz5238izDPBdetMkdgOImRYaD3UB2_8zTSWlmJbWfyGQMsHVf9L4JFxtOr2whWQmTrx4mqIANb9RE6t49YYom2zZqt_ey0fQYw%3D%3D; ServerPool=X; PMC=V2*MS.88*MD.20231210*LD.20231214; _abck=103E54A598E4912FA9A5E60D051A7CDD~-1~YAAQhb8mF12q8mOMAQAAcvwKaAs5LI+0BVP9Pm4b+OVgiqle9H+9IsZ308GOzd0hI4E5PZyzmgb1F5CE6GOINZS9uOWptm2U9w3QX3ftBt3CG1uvjy2gpJy+tkuHTvc3SofSzjUfPjJcyTcvpWHOSM9s9H0ajFSaPN/fUv1T/l7hIRasFCvvQvyUzioF2J1SNYvjVkj6O8CcRwPozrDkalptoRUhq74LLM6jB6iU5LKQTVbRZD6Cy40Z7ySSyAVzD9sIVrsfA51WyL66iqUyAD3zwZQKf5hycztvZx8FdTZFURaR26judNreX8JAzosGNc8OkyuioNPIjNyXkDKumBhdHz4ZfNFOI0gVS8ct+plBMrjTofu77qVSay4ZxJVSaHtLT+TteNWQZhrT9uZnJA==~-1~-1~-1; bm_sz=6BA49A78F535042224FFE8B544DC17C5~YAAQhb8mF16q8mOMAQAAcvwKaBYSIZNhWwq5EyOHJDPRtBTWP6hhkhJgE3iUzfT1r5OvWyky0rVYzrORe4htQK1xmY1AAa0Mcr/CojNoCsKiR3A3Q9+cM64aOrm/MPfJ+fxMSx3XHCFd24p9loOg9dIpSIndcel86nBlP/XlYqqVnzxu0WLnMs3i46qI65kYkCSoJ3oP6sSGecSZQLveqcWdZfN/r/QpN/uHoWaZBADqG/wPFAbZyq0k6VLK+J4b7VlNooScmc0BYWRmhkuSavaTSbQkag/80ulC4/8rdTnmMc+jOw4cFA==~4408887~3555896; _li_dcdm_c=.tripadvisor.com; _lr_sampling_rate=100; __li_idex_cache2_InByZWJpZC82NDQzOT9kdWlkPWIxNDAxNzNkZTU5MS0tMDFoaGJiMzg4M3hteXRoaDNlZng2cjZ4ajEmcmVzb2x2ZT1ub25JZCZyZXNvbHZlPW1hZ25pdGUi=%7B%7D; __li_idex_cache2_InByZWJpZC82NDQzOT9kdWlkPWIxNDAxNzNkZTU5MS0tMDFoaGJiMzg4M3hteXRoaDNlZng2cjZ4ajEmcmVzb2x2ZT1ub25JZCZyZXNvbHZlPW1hZ25pdGUi_meta=%7B%22w%22%3A1702552619384%2C%22e%22%3A1702556219000%7D; pbjs_li_nonid=%7B%7D; pbjs_li_nonid_cst=zix7LPQsHA%3D%3D; G_AUTH2_MIGRATION=informational; TAReturnTo=%1%%2FShowUserReviews-g1-d8729000-r804465644-Air_China-World.html; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+14+2023+19%3A24%3A17+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=7fb30751-d27c-4be4-b4a2-d3286dde6bf1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga_QX0Q50ZC9P=GS1.1.1702552610.12.1.1702553057.60.0.0; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22bedf6862-8384-695f-61b3-0ab92f22c19a%22%2C%22c%22%3A1702267517788%2C%22l%22%3A1702553058602%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%225568372c-1f96-e507-9641-b5b94eefbf8e%22%2C%22e%22%3A1702553118612%2C%22c%22%3A1702553058601%2C%22l%22%3A1702553058612%7D; __gads=ID=4c5ed3959617812a:T=1702261534:RT=1702556010:S=ALNI_MYDS-TCiF1YFyS3-R-Etl2apqEAxQ; __gpi=UID=00000ca93626e234:T=1702261534:RT=1702556010:S=ALNI_MYvLE68S9zTYAJ_a6h4QT_NlEjmIg; SRT=TART_SYNC; TASID=9A8CBAB7238541EFB728B2D2686823D3; TASession=V2ID.9A8CBAB7238541EFB728B2D2686823D3*SQ.16*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.8729000*EAU._; TAUD=LA-1702261304798-1*RDD-1-2023_12_10*ARDD-6313422-2023_12_24.2023_12_25*HDD-291747903-2023_12_24.2023_12_25*LG-294712289-2.1.F.*LD-294712290-.....; datadome=hanm5UoQplEg4yCOEfFfcFHg63c8tCJSaGCjP9glAdSETbZ0WJbHLiwsVJ1WLolV89gaceahiDQ~Y~C_NtJORmbiWYCEbo5LSDVJrFmQ9YViVyqQ_C~QYiAA27bwFLTN; __vt=lfYMWy6BmoJxacUkABQCCQPEFUluRFmojcP0P3EgGioS9WDkUayfU_pxWqcfZM-tcE0UfOIL2F6B9pNlHGIGGlF-YbfD-X9SH7qSZu-MNpZQHO0CHBkRczFgF9fc9R8z4BKWzZvua9PepIKYoxj_toTcEQ'
}
for i in range(0,len(Reviews)):
    data={
        'reviews': Reviews[i],
        'idxMtReviews':'',
        'contextChoice': 'SUR',
        'widgetChoice': 'EXPANDED_HOTEL_REVIEW_HSX',
        'haveJses': 'global_error, amdearly, jquery, mootools, ta - sur - hotel, attraction - detail - 2col, desktop - calendar - templates - dust - zh, 5xz, bt3, mqw, 988, qlc, 6nm, 52f, xg7, yau, al4, gug, p5p, 7th, nnp, ys6, eqo, 9b9, ltl, xo1, 4x6, dyf, qnd, fkj, jpp, qrk, q21, m49, u9j, gjt, 0b0, 90b, evv, gw8, 2r4, mb2, frf, kq4, zq9, ess, lr6, 904, b5n, eta, bxk, gbn, ltf, btb, nex, tm6, 5gp, 98i, 8py, qjo, uvk, 4eu, nnm, 1ol, bvz, vjl, rdy, z2l, hxl, l9q, 7u7, q13, uzm, qkj, gtt, 65r, d8o, iog, eww, tp1, tbk, lch, xj2, 3dy, vum, gyz, dsb, c3x, u5g, t9n, vbk, g05, vpo, s6q, ahl, fbu, 3co, fgw, j8l, ule, mtb, 32p, pro, q7w, 45d, bqg, txq, fzz, bvv, 4ax, 3bt, w0d, w1v, qbn, ued, f7m, laj, 7v9, 0of, 4q9, x9d, 79a, jbz, ja5, d6v, ybx, tr3, sdp, skj, 83p, 973, 6z5, t05, 2mj, wr5, vop, o4y, teh, ifb, 21h, l2u, 8cr, 5hc, ku7, ex1, qhd, k64, n6i, 7g0, g6k, i9i, kkq, 1ya, grn, siv, i3s, 7nq, xm2, con, an5, u59, rbx, p33, os3, yc7, r73, cov, lt9, 94v, ar9, u3a, qx8, 4il, i0z, my7, a6i, dvc, tj4, 0sj, lyy, ntn, b1c, bp9, af7, 43e, l47, 4tv, 24j, a2q, f2f, zuq, vfy, 7ya, 6qm, wrg, pg8, 34b, fa3, bke, 360, 2w7, sw5, w5k, j8m, 9m9, a3v, uby, oz3, eoz, 714, iah, 32k, 7gm, gpp, qhn, 7l5, flc, hwd, w1y, j1i, o3m, c5q, s1y, uc4, dlu, 27f, v5c, gcj, 60m, xtz, v1d, klb, 92w, t0p, 23p, y0u, kcv, abx, u16, gmr, mxu, 2wl, 4nz, 80h, z6c, y52, hv3, pn8, gnz, yw8, 00m, 8ec, 7a7, aqc, e32, 8m6, 4t9, afp, uov, dl4, 76j, j56, iro, 68a, ipq, owx, xvc, u47, rvd, hjf, wt5, it9, xlp, 89z, b42, 4z4, ezm, yc8, bxt, epp, bck, jk7, 1b5, l75, zb2, nc3, 0ad, nc6, m7w, 633, h9i, tty, l71, 2he, iwu, cb7, yug, cyr, cje, wsk, 1ua, tf8, xnj, gbs, jnx, 9yg, p4a, b1q, c5k, 2l7, do5, kqf, 0hk, 5c8, los, igy, y59, 7ov, b3v, sbz, m5f, 2mx, blj, d4c, aa8, a55, q6p, 5zx, nm5, 079, fug, u9y, mim, vws, lzo, l6h, qko, 6g4, 7s4, mat, xzn, d3i, 55g, 5h0, mc5, x0l, d5r, 74j, 7bj, s2g, mvp, wgu, nut, 9l2, ec9, b49, vtj, o5y, 330, 3ai, p3y, o80, bug, z2n, j2l, 8fu, lji, 35m, iun, w9f, ewp, q78, toc, vnf, vm2, rz5, 9so, wzt, wiw, t5u, nnv, arw, wud, q1i, apa, 1k8, r67, c38, yy6, l8y, rnf, 11l, q32, cgy, u6r, 7dk, moe, wxj, 9d7, ecg, zth, 3r7, df0, 508, yr8, n7m, kto, chl, bht, eun, b6u, 9qb, us7, cmu, i2c, 70j, 55n, obr, ag9, ns8, v1g, 2rn, yk7, p9u, joj, 6m9, r6a, 6ri, qk2, uw9, iyq, aj7, a85, 9rb, 665, tm4, qhc, 050, 2ws, irf, k7d, 227, c44, he3, 8ny, ams, 4sf, kxi, ckg, mjd, 25h, zto, 56m, gtc, y5k, 40q, w21, h9r, zsa, hu8, cjy, ymm, da2, 77i, 8sl, 1u1, kgl, 6zt, 52b, ifp, all, nyl, 7wb, 06g, hdc, 1f4, axz, 2hd, eki, 6q5, 92b, ztz, w43, n4z, weh, nnt, 9w3, ahn, nds, amw, sa2, avg, jud, ibe, 9d1, n48, 9ir, kgv, 2xm, vby, gag, nj1, 7oy, 2j5, g6h, jkv, ql7, 96e, lya, q6i, fm6, us1, 5xq, frb, 57e, 6mu, ifc, bhr, jgm, 5wi, xv8, 2t8, iwv, 141, cby, dk1, 0c1, z9k, wp1, rmu, 2mm, ghg, q76, 2jo, 49c, acx, ljq, ay1, gud, x55, zj3, iwb, dpz, 96t, rfo, deg, asj, dpm, 1gw, 4wi, lsg, gx3, x4s, wxz, a79, cdp, 8gg, o8g, fmn, 2ve, 9bt, kgn, j8u, bov, lq6, 68f, 6hf, n1m, c96, bj0, z2i, 468, 5hn, 2qd, ego, 8cp, z72, a7a, 0cw, dvd, cbd, kqy, yer, a34, 75v, q18, 556, 5az, it6, ue3, 008, 0v7, ofj, cvh, w2p, gu0',
        'haveCsses': 'long_lived_global_legacy, airline_sur, sur_reviews',
        'Action': 'install'
        }

    page_text =requests.post(url=url, headers=headers, data=data).text
    bes = bs4.BeautifulSoup(page_text,'lxml')
    texts = bes.find('div', id="", class_="entry")
    texts_list= texts_list+texts.text.split("\xa0"*4)
    print(texts.text.split("\xa0"*4))

    ex2 = '<div class="username mo">.*?>(.*?)<.*?</div>'
    user_name_list = re.findall(ex2, page_text, re.S)
    User = User + user_name_list
    print(user_name_list)

    ex3 = '<span class="ui_bubble_rating bubble_(.*?)0">.*?</span>'
    point_list = re.findall(ex3, page_text)
    Point = Point + point_list
    print(point_list)

f = open("中国南方航空2.csv", "w", encoding="utf-8-sig", newline="")
csvwritter = csv.writer(f)

for i in range(len(texts_list)):
    database = [User[i]] + [Point[i]] + [texts_list[i]]
    csvwritter.writerow(database)

print("Over")
'''
Reviews=
['732027085','768679675','694376423','689777430','694952521','688407554','663956812','649656405','625344565','359996690','929225828','360312517',
 '624692513','619442540','618172031','602060311','590865013','579247522','584529382','572888483','558063453','557304391','556644063',
 '552926546','552925157','551132634','550855033','550854953','543796976','543142536','540895535','540169499','533822958','522824837',
 '519379437','517656229','515902125','509306561','488398166','487724111','479433545','475766475','467769724','466012943','463670060',
 '458646009','457818515','457094159','455589307','454221840','451425431','449135358','447998973','447832990','447783647','447633447',
 '447083033','447831932','440080433','439888128','439450834','438253307','437738418','435557133','434760293','438474224','433903054',
 '431740871','427543948','431450416','426318402','424644713','423450530','421997479','421116163','417405085','420779077','409937336',
 '409256208','407394748','393473939','382117563','381825574','387741039','378212458','377268180','376882061','376874950','378548370',
 '373311705','371402589','371115901','373632075','370368454','370066974','369479751','371115852','368404956','364553231','360596313']-中国国际航空Reviews参数
'''
'''
Reviews=
['728555378','699212117','687794173','688674966','682640230','678513461','676091154','678820521','669158833','659256192','663956963',
'658438733','656981427','655391960','655179956','654104480','652332495','649656393','649115070','641762529','637606441','637212971',
'636668165','638312588','632795063','616673705','606338965','604632492','604281365','602060314','594859187','597578421','586378947',
'575850179','571874643','566435301','567189222','559183429','557304384','554168776','550855029','550854944','545751802','545249301',
'546984546','542416997','540895524','536587359','533818668','522824841','519858909','515902240','506732248','502443755','498183761',
'497417319','498804645','490660597','488194533','490660593','481585988','485328730','478794192','477957472','477955607','463670057',
'463669630','470477286','462207200','460334549','458261140','457313559','451647020','450106494','454932488','447967544','447882217',
'449135365','447072356','441892863','441505115','447645811','432612862','437738756','430826849','427830089','431741418','424952922',
'421115476','417405063','413824898','421116469','410946265','406978031','413452239','388983637','386960506','381824660','381334219',
'378211710','377873472','376881935','376880154','373311714','373023463','377268177','371719636','372784349','371115873','370066849',
'368405843','371116261','360311985','929362992','929232229','365344091']-中国东方航空公司Reviews参数
'''

'''
Reviews=[
'757582248','716685262','694952005','694379453','714747571','676786134',
'669158895','666669687','677250852','660122615','659878084','657781687',
'665019994','649656398','653892056','639721278','637606448','645128324',
'634622064','616918450','616670691','616209687','618406613','606691959',
'604280177','603289637','602060319','598822074','593221675','583624068',
'582178456','579014971','569257921','581951032','567651378','568843367',
'562903715','561688451','544206009','543143080','537602243','534291649',
'515902234','515519184','517087718','513659670','502442429','496494855',
'497417221','490968262','482871653','482871653','474050503','470488417',
'470477294','467194272','464993075','469070970','460620100','458862468',
'458645990','458040687','457819219','457314824','458455975','454221838',
'449135218','447967542','454932478','447083792','441504547','440834336',
'440080658','436088187','434760478','440834955','432612850','429130756',
'426897380','424952924','424952815','426076183','423082333','422748849',
'421997796','423450535','418759136','418759083','416733970','421997409',
'415546391','415632171','415320722','415179506','415633333','413824888',
'412203829','407393092','413824889','399122173','407393044','385501139',
'385215142','383909792','381825587','385501832','376882106','376878522',
'381074928','373632439','373311701','373023477','372310529','376875496',
'371115919','371115866','370868416','370066983','368672110','368404930',
'368403980','367151585','368672123','366806384'
]中国南方航空公司Reviews参数
'''