numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print("So\nGuys welcome to my game\n\tThe name of my game is\n\tPoison number\nSo\nBasically in this game\n\tThere are two players both have to choose different number\nThe number you choose will be posioned and after you both have to choose one number between 1 to 20 except the poison you choosed\n\tIf you choose the number poisoned by another player you die\nI hope you understood\nIf you face any error please contact me at\n\t9816841722\nThanks for pplaying my game\nNOW\n\tTHE GAME BEGINS")
print("When you enter your poison here make sure that your opponets eye is close")
poison1 = int(input("First player please enter your poison number between(1-20):"))
print("So now we are going to ececute random letters so ur poison numbeer gets hidden")
print("dfshfhsdfhsdhdfuhshdjsdhjkvjkjkvdfjkhkfk\nudfuudfsdgygsydgfiysdgyfdsyfs\nhdhifusdifudsiyfgs\njhdsfusdiuf\nfshudhfuih\nudfsghdfiusfus\nfhisdoiufhsuo\ndfusdhuf\nfijdsfuhsuidfs\njdfhoshdifho\njsdhfusdhfiu\nfihsohdfhosdhof\nifddsohfusdhousdhfds\nifohsdofhosidf\ndufuhdsofdso\nhfushdufudisf\ndfgisdfgiysd\ndhufsdufodshuf\nidohfiohsuohosds\nsdfusgufds\njkjhdfshuifsdgsdsdffsdj\ngfisudgfgisdfgiudsf\ngfsdgufyhg\njsgdfgsdiufgs\nsjdfisdugfds\nhsgfygdsf\ndshgfuisdfusdui\ndsfuidsifgisd\njdgfisdgfs\nfugsdiugfsd\njgfgds\n")
print("dfshfhsdfhsdhdfuhshdjsdhjkvjkjkvdfjkhkfk\nudfuudfsdgygsydgfiysdgyfdsyfs\nhdhifusdifudsiyfgs\njhdsfusdiuf\nfshudhfuih\nudfsghdfiusfus\nfhisdoiufhsuo\ndfusdhuf\nfijdsfuhsuidfs\njdfhoshdifho\njsdhfusdhfiu\nfihsohdfhosdhof\nifddsohfusdhousdhfds\nifohsdofhosidf\ndufuhdsofdso\nhfushdufudisf\ndfgisdfgiysd\ndhufsdufodshuf\nidohfiohsuohosds\nsdfusgufds\njkjhdfshuifsdgsdsdffsdj\ngfisudgfgisdfgiudsf\ngfsdgufyhg\njsgdfgsdiufgs\nsjdfisdugfds\nhsgfygdsf\ndshgfuisdfusdui\ndsfuidsifgisd\njdgfisdgfs\nfugsdiugfsd\njgfgds\n")
print("So now when you are enetring your poison make sure your opponets eye is close")
poison2 = int(input("Second player please enter your poison number between(1-20):"))
print("dfshfhsdfhsdhdfuhshdjsdhjkvjkjkvdfjkhkfk\nudfuudfsdgygsydgfiysdgyfdsyfs\nhdhifusdifudsiyfgs\njhdsfusdiuf\nfshudhfuih\nudfsghdfiusfus\nfhisdoiufhsuo\ndfusdhuf\nfijdsfuhsuidfs\njdfhoshdifho\njsdhfusdhfiu\nfihsohdfhosdhof\nifddsohfusdhousdhfds\nifohsdofhosidf\ndufuhdsofdso\nhfushdufudisf\ndfgisdfgiysd\ndhufsdufodshuf\nidohfiohsuohosds\nsdfusgufds\njkjhdfshuifsdgsdsdffsdj\ngfisudgfgisdfgiudsf\ngfsdgufyhg\njsgdfgsdiufgs\nsjdfisdugfds\nhsgfygdsf\ndshgfuisdfusdui\ndsfuidsifgisd\njdgfisdgfs\nfugsdiugfsd\njgfgds\n")
print("dfshfhsdfhsdhdfuhshdjsdhjkvjkjkvdfjkhkfk\nudfuudfsdgygsydgfiysdgyfdsyfs\nhdhifusdifudsiyfgs\njhdsfusdiuf\nfshudhfuih\nudfsghdfiusfus\nfhisdoiufhsuo\ndfusdhuf\nfijdsfuhsuidfs\njdfhoshdifho\njsdhfusdhfiu\nfihsohdfhosdhof\nifddsohfusdhousdhfds\nifohsdofhosidf\ndufuhdsofdso\nhfushdufudisf\ndfgisdfgiysd\ndhufsdufodshuf\nidohfiohsuohosds\nsdfusgufds\njkjhdfshuifsdgsdsdffsdj\ngfisudgfgisdfgiudsf\ngfsdgufyhg\njsgdfgsdiufgs\nsjdfisdugfds\nhsgfygdsf\ndshgfuisdfusdui\ndsfuidsifgisd\njdgfisdgfs\nfugsdiugfsd\njgfgds\n")
print("AND\nYEAH\n\tIF IT SAYS you died then its the end dont continue")
a = int(input("First player please enter your number between(1-20):"))
if a == poison2:
	print("First player you died ") 
else : 
		print("Safe please continue:")
numbers.remove(a)
print("So your remaining numbers are:", numbers)
b = int(input("Second player please enter your number:"))
if b == poison1:
	print("Second player you died:")
else :
	print("Safe please continue:") 
numbers.remove(b)
print("So your remaining numbers are:", numbers)
c = int(input("First player please enter your number between(1-20):"))
if c == poison2 :
	print("First player you died:")
else : 
	print("Safe please continue")
numbers.remove(c)
print(numbers)
print("So your remaining numbers are:", numbers)
d = int(input("Second player please enter your number between(1-20):"))
if d == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(d)
print("So your remaining numbers are:", numbers)
e = int(input("First player please enter your number between(1-20):"))
if e == poison2 :
	print("First player you died")
else :
	print("Safe please continue")
numbers.remove(e)
print("So your remaining numbers are:", numbers)
f = int(input("Second player please input your number between(1-20):"))
if f == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(f)
print("So your reamining numbers are:", numbers)
g = int(input("First player please enter your number between(1-20):"))
if g == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(g)
print("So your remaining numbers are:", numbers)
h = int(input("Second player please enter your number between(1-20):"))
if h == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(h)
print("So your remaining numbers are:", numbers)
i = int(input("First player please enter your number between(1-20):"))
if i == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(i)
print("So your remaining numbers are:", numbers)
j = int(input("Second player please enter your number between(1-20):"))
if j == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(j)
print("So your remaining numbers are:", numbers)
k = int(input("First player please enter your number between(1-20):"))
if k == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(k)
print("So your remaining numbers are:", numbers)
l = int(input("Second player please enter your number between(1-20):"))
if l == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(l)
print("So your remaining numbers are:", numbers)
m = int(input("First player please enter your number between(1-20):"))
if m == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(m)
print("So your remaining numbers are:", numbers)
n = int(input("Second player please enter your number between(1-20):"))
if n == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(n)
print("So your remaining numbers are:", numbers)
o = int(input("First player please enter your number between(1-20):"))
if o == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(o)
print("So your remaining numbers are:", numbers)
p = int(input("Second player please enter your number between(1-20):"))
if p == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(p)
print("So your remaining numbers are:", numbers)
q = int(input("First player please enter your number between(1-20):"))
if q == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(q)
print("So your remaining numbers are:", numbers)
r = int(input("Second player please enter your number between(1-20):"))
if r == poison1 :
	print("Second player you died:")
else :
	print("Safe please continue:")
numbers.remove(r)
print("So your remaining numbers are:", numbers)
s = int(input("First player please enter your number between(1-20):"))
if s == poison2 :
	print("First player you died:")
else :
	print("Safe please continue:")
numbers.remove(s)
print("So your remaining numbers are:", numbers)

