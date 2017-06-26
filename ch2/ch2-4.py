#tel book example
telbook={'mike': '1238569', 'john': '1534755', 'mary': '1235345', 'henry': '1452568'}
name=raw_input('whose number do you want to get:')
num=telbook.get(name)
print name,"'s number is", num
