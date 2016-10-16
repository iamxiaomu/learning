# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3023&konwledgeId=134
>题目描述									
	小赛经常沉迷于网络游戏。有一次，他在玩一个打怪升级的游戏，他的角色的初始能力值为a。在接下来的一段时间内，他将会依次遇见n个怪物，每个怪物的防御力为b1,b2,b3,…bn。如果遇到的怪物防御力bi小于等于小赛的当前能力值c，那么他就能轻松打败怪物，并且使得自己的能力值增加bi；如果bi大于c，那他也能打败怪物，但他的能力值只能增加bi与c的最大公约数。那么问题来了，在一系列的锻炼后，小赛的最终能力值为多少？
>输入
	对于每组数据，第一行是两个整数n(1<=n<=100000)表示怪物的数量和a表示小赛的初始能力值，第二行n个整数，b1,b2..bn.(1<=bi<=n)表示每个怪物的防御力
	数据保证——
	50%的n<=100,
	80%的n<=1000,
	90%的n<=10000,
	100%的n<=100000.
>输出
	对于每组数据，输出一行。每行仅包含一个整数，表示小赛的最终能力值。
>样例输入
	3 50
	50 105 200
	5 20
	30 20 15 40 100
>样例输出
	110
	205
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
def gcd(a, b): return a if b == 0 else gcd(b, a%b)

while True:  
	li = raw_input()  
	if not li: break
	n, c = map(int, li.split())
	a = map(int, raw_input().split())
	for i in xrange(0, n): c += a[i] if a[i]<=c else gcd(a[i], c)
	print(c)