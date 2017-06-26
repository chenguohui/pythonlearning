# encoding:utf-8 
# !/usr/bin/python
 
htmltext =u"""
<!DOCTYPE html>
<head>
    <title>网页</title>
</head>
<body>
    <ul >
    {% for item in items%}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>
    <h1>网页内容 </h1>
    {{ var|capitalize }}
    {# 注释  #}
</body>
</html>"""
import  jinja2  as  jj
template =jj.Template(htmltext)
class i:
    pass
items  =list()
items.append(i() )
items.append(i())
items[0].href='www.sina.com'
items[0].caption='sina'
items[1].href='www.yahoo.com'
items[1].caption='yahoo'
print template.render(var=u" hello",items=items)
