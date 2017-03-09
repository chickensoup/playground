# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
from urllib import *
import pdb, time
reload(sys)
sys.setdefaultencoding('utf8')

fproj = open('project_code_list.txt', 'r')
lines = fproj.read().splitlines()
lines.pop()

start = 0
if len(sys.argv) > 1:
    start = int(sys.argv[1])

if len(sys.argv) > 2:
    end = int(sys.argv[2])
else:
    end = start + 50


def process_room(room):
    room_url_prefix = 'http://fsfc.fsjw.gov.cn:8050/Templets/foshan/aspx/hpms/'
    room_url = room_url_prefix + room
    room_url = room_url.replace('&amp;', '&')
    re = requests.get(room_url).text
    room_soup = BeautifulSoup(re, "html.parser")
    room_info = "门牌号:" + room_soup.body.find(id='ROOM_ROOMNO').text + ";" + "所属单元:" + room_soup.body.find(id='ROOM_UNITNAME').text + ";" + "户型:" + room_soup.body.find(id='ROOM_FWHX').text + ";" + "房屋类型:" + room_soup.body.find(id='ROOM_FWLX').text + ";" + "房屋性质:" + room_soup.body.find(id='ROOM_FWXZ').text + ";" + "规划用途:" + room_soup.body.find(id='ROOM_GHYT').text + ";" + "权属状态:" + room_soup.body.find(id='ss').text + ";" + "阳台类型:" + room_soup.body.find(id='ROOM_YTLX').text + ";" + "预测建筑面积:" + room_soup.body.find(id='ROOM_YCJZMJ').text + ";" + "实测建筑面积:" + room_soup.body.find(id='ROOM_SCJZMJ').text + ";" + "预测套内面积:" + room_soup.body.find(id='ROOM_YCTNMJ').text + ";" + "实测套内面积:" + room_soup.body.find(id='ROOM_SCTNMJ').text + ";" + "预测分摊面积:" + room_soup.body.find(id='ROOM_YCFTMJ').text + ";" + "实测分摊面积:" + room_soup.body.find(id='ROOM_SCFTMJ').text + ";" + "装饰标准:" + room_soup.body.find(id='ROOM_ZSBZ').text + ";" + "设备标准:" + room_soup.body.find(id='ROOM_SBBZ').text + ";" + "户室配套:" + room_soup.body.find(id='ROOM_HSPT').text + ";" + "是否抵押:" + room_soup.body.find(id='SFDY').text + ";" + "是否查封:" + room_soup.body.find(id='SFCF').text + ";" + "销售状态:" + room_soup.body.find(id='XSZT').text + ";" + "单价（元）:" + room_soup.body.find(id='ROOM_PRICE').text + ";" + "总价（元）:" + room_soup.body.find(id='ROOM_ZJ').text + ";" + "房屋坐落:" + room_soup.body.find(id='ROOM_FWZL').text
    return room_info + "\r\n"


def process_proj(pj, line):
    outfile = 'proj_' + str(pj) + '.txt'
    f = open(outfile, 'w')

    pline = line.strip().split('&')
    pcode = pline[0]
    pdblx = pline[1]
    projurl = 'http://fsfc.fsjw.gov.cn:8050/Templets/foshan/aspx/hpms/ProjectDetailsInfo.aspx?' + str(line.strip())
    r1 = requests.get(projurl)
    soup = BeautifulSoup(r1.text, "html.parser")
    
    print 'Processing project ' + str(pj)
    f.write("项目链接:" + projurl + "\r\n")
    projdetail = "项目名称:" + soup.body.find(id='Project_XMMC').text + ";项目地址:" + soup.body.find(id='Project_XMDZ').text + ";开发商:" + soup.body.find(id='Project_KFQY_NAME').text + ";行政区划:" + soup.body.find(id='lblSZQY').text + ";总建筑面积:" + soup.body.find(id='Project_GHZJZMJ').text + ";容积率:" + soup.body.find(id='Project_RJL').text + ";资质证书编号:" + soup.body.find(id='lblZZZS').text + ";资质等级:" + soup.body.find(id='lblZZDJ').text + ";楼盘销售部地址:" + soup.body.find(id='Project_SLCDH').text
    projzz = "住宅:" + soup.body.find(id='lblZZYSZTS').text + ";" + soup.body.find(id='lblZZYSZMJ').text + ";" + soup.body.find(id='lblZZYSJJ').text + ";" + soup.body.find(id='lblZZWSTS').text + ";" + soup.body.find(id='lblZZWSMJ').text
    projsy = "商业:" + soup.body.find(id='lblSYYSZTS').text + ";" + soup.body.find(id='lblSYYSZMJ').text + ";" + soup.body.find(id='lblSYYSJJ').text + ";" + soup.body.find(id='lblSYWSTS').text + ";" + soup.body.find(id='lblSYWSMJ').text
    projqt = "其他:" + soup.body.find(id='lblQTYSZTS').text + ";" + soup.body.find(id='lblQTYSZMJ').text + ";" + soup.body.find(id='lblQTYSJJ').text + ";" + soup.body.find(id='lblQTWSTS').text + ";" + soup.body.find(id='lblQTWSMJ').text
    f.write(projdetail + "\r\n")
    f.write(projzz + "\r\n")
    f.write(projsy + "\r\n")
    f.write(projqt + "\r\n")
    f.flush()

    proj_presell = 'http://fsfc.fsjw.gov.cn:8050/Templets/FoShan/aspx/HPMS/GetQueryResult.ashx?type=0&P' + pcode + "&" + pdblx
    r2 = requests.get(proj_presell)
    soup2 = BeautifulSoup(r2.text, "html.parser")
    presell_count = str(soup2).count("BuildChange(")
    f.write("总栋数:" + str(presell_count) + "\r\n")
    print str(presell_count) + " buildings"
    presell_yushou = str(soup2).strip().split("BuildChange(")
    presell_dong = str(soup2).strip().split("id=\"build")
    for i in range(1, presell_count + 1):
        presell_yushouid = (presell_yushou[i].split(","))[0].rstrip("\'")
        presell_dongid = (presell_dong[i].split("\""))[0].rstrip("\'")
        #f.write(presell_yushouid + ";" + presell_dongid + "\r\n")
        presell_url = "http://fsfc.fsjw.gov.cn:8050/Templets/foshan/aspx/hpms/presellCertInfo.aspx?" + pdblx + "&code=" + presell_yushouid
        f.write("预售许可证:" + presell_url + ";")
        presell_r = ""
        while 1:
            try:
                presell_r = requests.get(presell_url)
                break
            except Exception, e:
                print "retry get presell response"
        presell_soup = BeautifulSoup(presell_r.text, "html.parser")
        presell_info = "发证日期:" + presell_soup.body.find(id='YSXKZ_FZRQ').text + ";" + "有效期自:" + presell_soup.body.find(id='YSXKZ_YXQX1').text + ";" + "有效期至:" + presell_soup.body.find(id='YSXKZ_YXQX2').text + ";" + "预售幢名称:" + presell_soup.body.find(id='YSZMC').text
        f.write(presell_info + "\r\n")
        #presell_useage1 = "套数:" + presell_soup.body.find(id='lblZZTS').text + ";" + presell_soup.body.find(id='lblSYTS').text + ";" + presell_soup.body.find(id='lblQTTS').text
        #presell_useage2 = "面积:" + presell_soup.body.find(id='lblZZMJ').text + ";" + presell_soup.body.find(id='lblSYMJ').text + ";" + presell_soup.body.find(id='lblQTMJ').text
        #f.write(presell_useage1 + "\r\n")
        #f.write(presell_useage2 + "\r\n")
        exe_url = 'http://fsfc.fsjw.gov.cn:8050/Common/Agents/ExeFunCommon.aspx'
        exe_validation_data = '%3C?xml%20version=%221.0%22%20encoding=%22utf-8%22%20standalone=%22yes%22?%3E%0A%3Cparam%20funname=%22SouthDigital.CMS.PubHelper.GetRoomWhere%22%3E%0A%3Citem%3Ecode=' + presell_dongid + '&amp;rsr=1001&amp;rse=0&amp;rhx=3001&amp;jzmj=&amp;tnmj=%3C/item%3E%0A%3C/param%3E%0A'
        response_validation = ""
        while 1:
            try:
                response_validation = requests.post(exe_url, exe_validation_data).text
                break
            except Exception, e:
                print "retry response validation"
        exe_dong_data1 = '%3C?xml%20version=%221.0%22%20encoding=%22utf-8%22%20standalone=%22yes%22?%3E%0A%3Cparam%20funname=%22SouthDigital.CMS.CBuildTableEx_FS.GetPublicHTML%22%3E%0A%3Citem%3E' + presell_dongid + '%3C/item%3E%0A%3Citem%3E%20' + response_validation.strip() + '%3C/item%3E%0A%3Citem%3E%3C/item%3E%0A%3Citem%3E%3C/item%3E%0A%3Citem%3E1%3C/item%3E%0A%3C/param%3E%0A'
        exe_dong_data2 = '%3C?xml%20version=%221.0%22%20encoding=%22utf-8%22%20standalone=%22yes%22?%3E%0A%3Cparam%20funname=%22SouthDigital.CMS.CBuildTableEx_FS.GetPublicHTML%22%3E%0A%3Citem%3E' + presell_dongid + '%3C/item%3E%0A%3Citem%3E%20' + response_validation.strip() + '%3C/item%3E%0A%3Citem%3E%3C/item%3E%0A%3Citem%3E%3C/item%3E%0A%3Citem%3E2%3C/item%3E%0A%3C/param%3E%0A'
        
        
        if pdblx == 'dblx=1':
            exe_dong_data = exe_dong_data1
        elif pdblx == 'dblx=2':
            exe_dong_data = exe_dong_data2
        
        dong_soup = BeautifulSoup(requests.post(exe_url, exe_dong_data).text, "html.parser")
        rooms = str(dong_soup).split("href=\"")

        if (len(rooms) > 1):
            rooms.pop(0)
            rooms_set = set()
            for room in rooms:
                room_url_app = room.split("\"")[0]
                rooms_set.add(room_url_app)

            print "  " + str(len(rooms_set)) + " rooms"
            t3 = time.time()
            rooms_set_list = list(rooms_set)
            j = 0
            room_list = [""] * len(rooms_set_list)
            sys.stdout.write("    ")
            while j < len(rooms_set_list):
                j = j + 1
                room = rooms_set_list[j-1]
                try:
                    room_list[j-1] = process_room(room)
                    sys.stdout.write("+")
                    sys.stdout.flush()
                except Exception, e:
                    print "find exception, retry"
                    j = j - 1

            room_infos = "".join(room_list)
            f.write(room_infos)
            f.flush()
            t4 = time.time()
            print " No." + str(i) + "/" + str(presell_count) + ": "+ str(t4-t3) + " secondes."

    f.write("\r\n")
    f.flush()
    f.close()

for i in range(start, end):
    t1 = time.time()
    process_proj(i, lines[i])
    t2 = time.time()
    print "Process " + str(i) + " finished in " + str(t2-t1) + " seconds."