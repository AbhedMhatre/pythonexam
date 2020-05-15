#1.1
'''num=int(input('enter number'))
count=0
while (num>0):
    num=num//10
    count=count+1
print(count)
'''

#1.2
'''
list1=[10,20,30,40,50]
for i in range(len(list1)+1):
    print(list1[-i-1])
'''

#2
'''
s1=(input(str('enter first string')))
s2=(input(str('enter second string')))
print(s1[0:4]+ s2 + s1[4:(len(s1)+1)])
'''

#3
'''
s=input(str('enter string'))
for i in range(len(s)):
    if s[i].islower():
        print(s[i])
for i in range(len(s)):
    if s[i].isupper():
        print(s[i])
'''
#5
'''
list1=[0,1,2,3,4,5]
list2=[6,7,8,9,10,11]
list3=[]
for i in range(0,len(list1),2):
    list3.append(list1[i])
    print(list3)
for i in range(1,len(list2),2):
    list3.append(list2[i])
    print(list3)
'''
