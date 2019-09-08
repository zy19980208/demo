'''
正则表达式：是一种字符串的处理方式，用于字符串的匹配
字符串的匹配有两种：
    内容匹配   python re
        通过描述要匹配的内容的类型和数量来实现匹配
    结构匹配  xpath
        通过描述要匹配的内容在整体中的结构来实现匹配
'''
import re

string = 'hello \n  \t  world 12h3 _ _'
# 类型匹配
# 原样匹配
# res = re.findall('正则表达式','字符串')
res = re.findall('hello',string)
print(res)
# .  除了 \n 之外的所有内容
res = re.findall('.', string)
print(res)
# \d 匹配的是数字
res = re.findall('\d', string)
print(res)
# \D 匹配的是除了数字之外的
res = re.findall('\D', string)
print(res)
# \w 匹配的是数字、字母、下划线
res = re.findall('\w', string)
print(res)
# \W 匹配的是除了数字、字母、下划线之外的
res = re.findall('\W', string)
print(res)
# [] 返回中括号中的任意一个字符
res = re.findall('[a-zA-Z0-9]', string)
print(res)
# 取反
res = re.findall('[^a-zA-Z0-9]', string)
print(res)
# | 匹配任意一边的字符
res = re.findall('hello|world', string)
print(res)
# () 组匹配，将括号后面的作为条件
# 匹配一个后面为数字的数字
res = re.findall('(\d)h', string)
print(res)
# 分组 起一个组名  组名叫id
# id = \d
res = re.findall('(?P<id>\d)', string)
print(res)

# (?P=id) 对前面的组名 id 的引用
# (?P<id>\d)h



# 长度匹配  * + ? {}
# 特殊匹配  ^ $