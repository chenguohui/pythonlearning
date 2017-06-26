# encoding:utf-8 
# !/usr/bin/python
from lxml.html import parse
from urllib2 import urlopen
from lxml import etree
from StringIO import StringIO
#生成XML文件

def building_xml():
    root=etree.Element("root" )
    root.text=u"root 文本内容"
    root.set("rootattr1","123")
    root.set("rootattr2","456")
    print root.tag#输出元素标签
    print root.keys()#输出属性名
    print root.items()#输出属性
    print root.text#输出文本内容
    child1=etree.SubElement(root,"child1")
    child2=etree.SubElement(root,"child2")
    child1.text=u" hello child1 文本内容  "
    print etree.tostring(root,pretty_print=True)
    tree = etree.ElementTree(root)
    tree.write("XMLFile.xml", encoding='utf-8',method="xml",xml_declaration=True)
    return
building_xml()


#-读取所有的连接 ；
def parseXML(xmlFile):
    f = urlopen(xmlFile)
    xml = f.read()
    tree = etree.parse(StringIO(xml))
    context = etree.iterparse(StringIO(xml))
    for action, elem in context:
        if elem.tag=='link':
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print elem.tag + " => " + text
if __name__ == "__main__":
    parseXML("http://rss.sina.com.cn/news/marquee/ddt.xml")
    parseXML("http://www.people.com.cn/rss/politics.xml")
