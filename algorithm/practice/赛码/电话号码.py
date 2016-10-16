# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3310&konwledgeId=134
>题目描述				
	电话机按键中英文字母（除Q和Z外）和电话号码之间存在如下对应关系：
	A,B,C -> 2
	D,E,F -> 3
	G,H,I -> 4
	J,K,L -> 5
	M,N,O -> 6
	P,R,S -> 7
	T,U,V -> 8
	W,X,Y -> 9
	美国标准的电话号码格式为xxx-xxxx，其中x表示0-9中的一个数字。有时为方便记忆，会将电话号码中的数字转变为英文字母，如263-7422为America。有时还会加上“-”作为分隔符，如449-6753记成Hi-World。当然，没有必要将所有的数字都转变为字母，所以474-6635可以记作iPhone-5。
	总之，一个方便记忆的电话号码由数字和除Q、Z外的英文字母组成，并且可以在任意位置插入任意多的“-”符号。
	现在有一个电话号码列表，记录着许多方便记忆的电话号码。不同的方便记忆的电话号码可能对应相同的标准号码，你能找出它们吗?
								
>输入
	第一行是一个正整数n（n <= 100000），表示号码列表中的电话号码数。
	其后的n行中，每行是一个方便记忆的电话号码，由数字和除Q、Z外的英文字母、“-”符号组成，其中数字和字母的总数一定为7，字符串总长度不超过200。
>输出
	输出包括若干行，每行包括一个标准电话号码（xxx-xxxx）以及它重复出现的次数k（k >= 2），中间用空格分隔。输出的标准电话号码需按照升序排序。
	如果没有重复出现的标准电话号码，则输出一行“No duplicates.”。
>样例输入
	12
	4873279
	ITS-EASY
	888-4567
	3-10-10-10
	888-GLOP
	TUT-GLOP
	967-11-11
	310-GINO
	F101010
	888-1200
	-4-8-7-3-2-7-9-
	487-3279
>样例输出
	310-1010 2
	487-3279 4
	888-4567 3
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
dic = {
	'0':0, '1':1,
	'A':2, 'B':2, 'C':2, '2':2,
	'D':3, 'E':3, 'F':3, '3':3,
	'G':4, 'H':4, 'I':4, '4':4,
	'J':5, 'K':5, 'L':5, '5':5,
	'M':6, 'N':6, 'O':6, '6':6,
	'P':7, 'R':7, 'S':7, '7':7,
	'T':8, 'U':8, 'V':8, '8':8,
	'W':9, 'X':9, 'Y':9, '9':9
}

a, r = [], {}
T = int(raw_input())
for it in range(0, T):
	a.append(''.join([str(dic[c]) for c in raw_input().replace('-','')]))
a = sorted(a)
for i in xrange(0, len(a)):
	r[a[i]] = r[a[i]]+1 if r.has_key(a[i]) else 1
r = [(k[:3]+'-'+k[3:],v) for k, v in r.items() if v>1]
if len(r)>0: 
	for k, v in r: print(k + ' ' + str(v))
else: print('No duplicates.')