# QUESTION 1

a=str(input("Enter any Strings: "))
list=a.split() #To split all the elements of string in a list dict() #initializing an empty dictionary
dict={} #initialising an empty dictionary
if list.__len__()==1: #if statement will be implemented when a single word is
	for i in list [0]: 
		if i in dict:
			dict [i]+=0
		else:
			dict[i]=1
	print (dict)
else:  
	for i in list:
		if i in dict:
			dict[i]+=1
		else:
			dict [i]=1
	print (dict)
print("\n")
---------------------------------------------------------------------------------------------------------------
>>>  OUTPUT OF QUESTION NO. 1:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter any Strings: hello world
{'hello': 1, 'world': 1}

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter any Strings: hey
{'h': 1, 'e': 1, 'y': 1}
_______________________________________________________________________________________________________________



# QUESTION 2

print("""Please provide inputs of date, month and year fulfilling the following conditions:-

C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025
""")

#Taking input from the user and checking conditions in format(dd/mm/yyyy)
day=int(input("Day "))
if(day>31 or day<1):
	print("invalid input date")
month=int(input("Month "))
if(month>12 or month<1):
	print("invalid input month")
year=int(input("year "))
if(year>2025 or year<1800):
	print("input year out of range")

print("Input date: %d/%d/%d" %(day,month,year))

#For all months except february and days ranging from 1 to 29
if(1<=day<30 and month!=2):
	day+=1  

#For the 30th day of january, march, may, july, august, october and december
elif((day==30) and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12)) :
	day+=1

#For the 30th day of april, june,september and november
elif((day==30) and (month==4 or month==6 or month==9 or month==11)):
	day=1
	month+=1

#For the 31st day of january, march, may, july, august and october
elif((day==31) and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 )):
	day=1
	month+=1

#For the 31st day of december(New year's eve!)
elif(day==31 and month==12):
	day=1
	month=1
	year+=1

#For february of a leap year
elif(year%4==0 and month==2):
 	if(1<=day<29):
 		day+=1
 	elif(day==29):
 		day=1
 		month=3

#For february of a non-leap year
elif(year%4!=0 and month==2):
	if(1<=day<28):
		day+=1
	elif(day==28):
		day=1
		month=3
else:
	print("invalid format")
print("Next date : %d/%d/%d" %(day,month,year))
--------------------------------------------------------------------------------------------------------------
>>>  OUTPUT OF QUESTION NO. 2:-
C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Please provide inputs of date, month and year fulfilling the following conditions:-

C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025

Day 31
Month 12
year 2015
Input date: 31/12/2015
Next date : 1/1/2016

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Please provide inputs of date, month and year fulfilling the following conditions:-

C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025

Day 28
Month 02
year 2016
Input date: 28/2/2016
Next date : 29/2/2016

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Please provide inputs of date, month and year fulfilling the following conditions:-

C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025

Day 29
Month 02
year 2016
Input date: 29/2/2016
Next date : 1/3/2016
>>>
______________________________________________________________________________________________________________
__

#QUESTION 3
i=0
#Creating lists
lis=[]
tup=[]
outlist=[]
#Taking input from the user for number of elements in list
x=int(input("Enter number of elements in list "))
print("" "")
#using while loop
while(i<x):
	print("Enter Element no.",i+1)
	a=int(input())
	#Adding elements provided by the user to the list
	lis.append(a)
	i+=1	
i=0
#using another while loop
while(i<x):

	tup.append(lis[i])
	tup.append(lis[i]**2)
	#Converting tup(type: list) into tupple data type
	tup=tuple(tup)
	outlist.append(tup)
	#Converting tup(type: tupple) into list data type
	tup=list(tup)
	tup=[]
	i+=1
#Printing desired output
print("Desired Output: ",outlist)

----------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 3:-
C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter number of elements in list 3

Enter Element no. 1
3
Enter Element no. 2
9
Enter Element no. 3
10
Desired Output:  [(3, 9), (9, 81), (10, 100)]
>>>
________________________________________________________________________________________________________________

#QUESTION 4

#Taking grade point input from the user
a=int(input("Enter your grade point:- "))
if(4<=a<=10):
	if(a==10):
		perf="Outstanding"
		grade="A+"
	if(a==9):
		perf="Excellent"
		grade="A"
	if(a==8):
		perf="Very Good"
		grade="B+"
	if(a==7):
		perf="Good"
		grade="B"
	if(a==6):
		perf="Average"
		grade="C+"
	if(a==5):
		perf="Below Average"
		grade="C"
	if(a==4):
		perf="Poor"
		grade="D"

	#Printing desirable output
	print("Your Grade is", grade,"and", perf, "Performance.")
else:
	#Printing Error if grade point is not in the range 4 to 10
	print("Error!")
------------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 4:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter your grade point:- 9
Your Grade is A and Excellent Performance.

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter your grade point:- 4
Your Grade is D and Poor Performance.
>>>
__________________________________________________________________________________________________________________

#QUESTION 5

#Printing the given pattern 
n = 6

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
    	#As ASCII value of A is 65
        print(chr(65 + j), end='')
    print()
-------------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 5:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
ABCDEFGHIJK
 ABCDEFGHI
  ABCDEFG
   ABCDE
    ABC
     A
___________________________________________________________________________________________________________________
#QUESTION 6
dic={}
a = str(input("""Do you want to enter SID and name?
if yes press "Y" otherwise press "N" """))
while(a=="Y" ):
	key=int(input("Enter SID "))
	value=str(input("Enter Name "))
	dic[key]=value
	a = str(input("If you want to continue press 'Y' otherwise press 'N' "))
else:
	#A) Printing students details stored in the dictionary.
	print(dic)
	#Else closing the dictionary
	print("Thank You")
print("")

#B) Sorting dictionary using student names
print("Sorted dictionary using student names")
dic2={}
for i in sorted(dic):
   dic2[i]=dic[i]
print(dic2)
print("")

#C) Sorting dictionary using SID
print("Sorted dictionary using SID")
dic2=dict(sorted(dic.items(),key= lambda x:x[1]))
print(dic2)
print("")

#D)Searching a student details with SID and printing name of that student.
e=int(input("Enter the SID to print name of that student "))
d=dic[e]
print(d)
---------------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 6:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Do you want to enter SID and name?
if yes press "Y" otherwise press "N" Y
Enter SID 20102021
Enter Name Jahanvi
If you want to continue press 'Y' otherwise press 'N' Y
Enter SID 20102049
Enter Name Aaditya
If you want to continue press 'Y' otherwise press 'N' Y
Enter SID 20102000
Enter Name Rythm
If you want to continue press 'Y' otherwise press 'N' N
{20102021: 'Jahanvi', 20102049: 'Aaditya', 20102000: 'Rythm'}
Thank You

Sorted dictionary using student names
{20102000: 'Rythm', 20102021: 'Jahanvi', 20102049: 'Aaditya'}

Sorted dictionary using SID
{20102049: 'Aaditya', 20102021: 'Jahanvi', 20102000: 'Rythm'}

Enter the SID to print name of that student 20102021
Jahanvi
>>>
_____________________________________________________________________________________________________________________
#QUESTION 7

#Taking input from user
n=int(input("Enter no. of elements you want in your fibonnaci series: "))
#Defining a function to create fibonnaci series
def fibo(n):
	if(n==0 or n==1):
		return n
	else:
		return fibo(n-1)+fibo(n-2)


i=0
lis=[]


#Printing fibonnaci till nth term
while(i<n):
	print(fibo(i), end=" ")
	i+=1
print("")

i=0
#For average of the fibonnaci series
while(i<n):
	a=fibo(i)
	lis.append(a)
	i+=1
i=0
s=0
while(i<n):
	s=s+lis[i]
	i+=1
print("The average of the above fibonnaci series is:",s/n)
-----------------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 7:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
Enter no. of elements you want in your fibonnaci series: 8
0 1 1 2 3 5 8 13
The average of the above fibonnaci series is: 4.125
>>>
________________________________________________________________________________________________________________________

#QUESTION 8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

#A)Creating a new set of all elements that are in Set1 and Set2 but not both.
a= (set1|set2)-(set1&set2)
print("A)",a)
print("")

#B)Creating a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
b=(set1|set2|set3)-(set1&set2)-(set3&set2)-(set1&set3)-(set1&set2&set3)
print("B)",b)
print("")

#C)Creating a new set of elements that are exactly two of the sets Set1, Set2 and Set3.
c=(set1&set2)|(set3&set2)|(set1&set3)
print("C)",c)
print("")


#D)Creating a new set of all integers in the range 1 to 10 that are not in Set1.

#Here we have defined a new set with elements ranging from 1 to 10
newset={1,2,3,4,5,6,7,8,9,10}
d=newset-set1
print("D)",d)
print("")

#E)Creating a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
e=newset-(set1|set2|set3)
print("E)",e)

--------------------------------------------------------------------------------------------------------------------------
>>>   OUTPUT OF QUESTION NO. 8:-

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\a.py"
A) {1, 3, 5, 6, 8}

B) {17, 3, 6, 8, 9, 13}

C) {1, 2, 4, 5}

D) {6, 7, 8, 9, 10}

E) {10, 7}
>>>
___________________________________________________________________________________________________________________________




























