# question 1
dict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item"
}
print("option are : ",dict.keys())
a = input("enter hindi word : " )
# print("meaning is : " , dict[a])  #not a good approch
print("meaning is : " , dict.get(a))

#question 2
s1 = int(input("enter a number"))
s2 = int(input("enter a number"))
s3 = int(input("enter a number"))
s4 = int(input("enter a number"))
s5 = int(input("enter a number"))
s6 = int(input("enter a number"))
s7 = int(input("enter a number"))
s8 = int(input("enter a number"))
set = {s1 , s2 , s3 , s4 ,s5 ,s6 ,s7 ,s8}
print(set)

#question 3
s={18,"18"}
print(s)
print(len(s))

#question 4
st = set()
st.add(20)
st.add(20.0)
st.add("20")
print(st)
print(len(st))

#question 5
s ={}
print(type(s))

##question 6
dict = {}
n1 = input("enter your name : ")
l1 = input( n1 +" what is your fab. language : ")
n2 = input("enter your name : ")
l2 = input( n2 + " what is your fab. language : ")
n3 = input("enter your name : ")
l3 = input( n3 +" what is your fab. language : ")
n4 = input("enter your name : ")
l4 = input( n4 + " what is your fab. language : ")
dict= {n1 : l1 ,n2 : l2 ,n3 : l3 ,n4 : l4 }
print(dict)

