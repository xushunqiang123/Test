#-*-coding:utf-8 -*-
from Txt_Xml import *

# with open("./static/Exam.txt","r",encoding="utf8") as f:
#     aa = f.read()
#     print(aa)
def makexml():
    from xml.dom.minidom import Document
    doc = Document()
    root = doc.createElement("root")
    doc.appendChild(root)

    lis = readtxt()
    for shili in lis:
        issue = doc.createElement("issue")
        issue.setAttribute('index',str(shili.isindex))
        issue.setAttribute('describe',str(shili.describe))
        print(str(shili.describe))
        issue.setAttribute('explain','道阻且长，吾将上下而求索')
        issue.setAttribute('img','')
        root.appendChild(issue)

        alternative = doc.createElement("alternative")
        alternative.setAttribute('index',str(shili.altindex1))
        alternative.setAttribute('describe',str(shili.altdescribe1))
        alternative.setAttribute('correct',str(shili.altcorrect1))
        issue.appendChild(alternative)

        alternative = doc.createElement("alternative")
        alternative.setAttribute('index',str(shili.altindex2))
        alternative.setAttribute('describe',str(shili.altdescribe2))
        alternative.setAttribute('correct',str(shili.altcorrect2))
        issue.appendChild(alternative)

        alternative = doc.createElement("alternative")
        alternative.setAttribute('index',str(shili.altindex3))
        alternative.setAttribute('describe',str(shili.altdescribe3))
        alternative.setAttribute('correct',str(shili.altcorrect3))
        issue.appendChild(alternative)

        alternative = doc.createElement("alternative")
        alternative.setAttribute('index',str(shili.altindex4))
        alternative.setAttribute('describe',str(shili.altdescribe4))
        alternative.setAttribute('correct',str(shili.altcorrect4))
        issue.appendChild(alternative)

    filename = "finally.xml"
    f = open(filename, "w",encoding="UTF-8")
    f.write(doc.toprettyxml(indent="  "))
    f.close()

if __name__ == '__main__':
    # chaiftxt()
    makexml()