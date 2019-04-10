#-*-coding:utf-8 -*-
from YIEDD import makexml
import re


class readdata():
    isindex = ""
    describe = ""
    correct = ""

    altindex1 = "A"
    altdescribe1 = ""
    altcorrect1 = False


    altindex2 = "B"
    altdescribe2 = ""
    altcorrect2 = False


    altindex3 = "C"
    altdescribe3 = ""
    altcorrect3 = False

    altindex4 = "D"
    altdescribe4 = ""
    altcorrect4 = False



def chaiftxt():
    with open("./static/光热选择题.txt","r",encoding="utf8") as f:
        while True:
            altindex = f.readline()
            num = altindex.split(".")[0]
            b = f.readline()
            with open("./static/alltxt/{0}.txt".format(num),"w",encoding="utf8") as tt:
                tt.write(altindex)
                tt.write(b)
            if num =="51":
                break
            continue
def readtxt():
    lis = ["A","B","C","D"]
    lisduixiang = []
    for num in range(1,52):
        with open("./static/alltxt/{0}.txt".format(num),"r",encoding="utf8")as xx:
            #第一行内容
            firstline = xx.readline()
            p1 = re.compile(r'[（](.*?)[）]', re.S)  # 最小匹配
            ss = re.findall(p1,firstline)[0].strip()
            # print(ss)
# （）
            global  correct ,timu
            kuohou = firstline.split("（")[1]
            for i in kuohou:
                if i in lis:
                    a = firstline.replace(ss,"")
                    correct = ss
                    # print(i)
                    try:
                        timu = a.split("{0}.".format(num))[1]
                    except:
                        timu =a.split(".")[1]
                    # print(firstline)
                    # print(correct)
                    # print(timu)
                    # print("*"*10)
            #第二行内容
            sencondline = xx.readline()
            # print(sencondline)

            aconten = sencondline.split("B")[0].split(".")[1].strip()
            bconten = sencondline.split(".")[2].replace("C", "").strip()
            cconten = sencondline.split(".")[3].replace("D", "").strip()
            dconten = sencondline.split("D")[1].split(".")[1].strip()
            # print(aconten)
            # print(bconten)
            # print(cconten)
            # print(dconten)
            # print(num,"*" * 10)


            shili = readdata()
            shili.isindex = num
            shili.describe = timu
            shili.correct = correct
            if correct =="A":
                shili.altcorrect1 = True
                shili.altcorrect2 = False
                shili.altcorrect3 = False
                shili.altcorrect4 = False
            elif correct =="B":
                shili.altcorrect1 = False
                shili.altcorrect2 = True
                shili.altcorrect3 = False
                shili.altcorrect4 = False
            elif correct =="C":
                shili.altcorrect1 = False
                shili.altcorrect2 = False
                shili.altcorrect3 = True
                shili.altcorrect4 = False
            elif correct =="D":
                shili.altcorrect1 = False
                shili.altcorrect2 = False
                shili.altcorrect3 = False
                shili.altcorrect4 = True



            #第二行的
            shili.altindex1 = "A"
            shili.altdescribe1 = aconten

            shili.altindex2 = "B"
            shili.altdescribe2 = bconten

            shili.altindex3 = "C"
            shili.altdescribe3 = cconten

            shili.altindex4 = "D"
            shili.altdescribe4 = dconten

            lisduixiang.append(shili)
    return lisduixiang
            # break



