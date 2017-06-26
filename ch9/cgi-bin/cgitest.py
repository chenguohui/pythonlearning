# encoding:utf-8 
# !/usr/bin/python

import cgi
# 显示为Html
print "Content-Type: text/html\n\n"
def generate_form():
    print "<HTML><HEAD><TITLE>Login</TITLE></HEAD><BODY >\n"
    print  ("<H3>input username and password </H3>\n")
    print "<FORM METHOD = post ACTION = \"cgitest.py\">\n"
    print " Username: <INPUT type = text     name = \"name\"> \n"
    print " Password: <INPUT type = text name =     \"pwd\"> \n"
    print "<INPUT TYPE = hidden NAME = \"action\" VALUE = \"display\">\n"
    print "<INPUT TYPE = submit VALUE = \"Enter\">\n"
    print "</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

def display_log(name, pwd):
    print "<HTML><HEAD><TITLE>User Info Form</TITLE></HEAD><BODY>\n"
    print "username:", name, "\n\n password :", pwd
    print "</BODY>\n"
    print "</HTML>\n"

if __name__=="__main__":
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("name")  and form.has_key("pwd")):
             if (form["action"].value == "display"):
                display_log(form["name"].value, form["pwd"].value)
    else:
             generate_form()
