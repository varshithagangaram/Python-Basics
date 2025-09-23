#exceptional
#1.zero division error
# try:
#    num=int(input("enter num:"))
#    dem=int(input("enter dem:"))
#    div=num/dem
#    print(div)
# except ZeroDivisionError:
#    print("error")

# # 2.value

# try:
#  a=int(input("enter the no. :" ))
#  print(a)
# except:
#    print("float") 

# # # 3.type
# try:
#    a=int(input("enter the no:"))
#    b=[1,2,3]
#    print(a+b)
# except:
#    print("invalid")
# # 4.name
# try:
#    a="abhi"
#    print(b)      
# except:
#    print("error")

# # #5 index
# try:
#    list=[4,6,8,9]
#    print(list[4])
# except:
#    print("invalid")

# #6 key:
# try:
#     dict={"name":"varsha",
#          "group":"csc"}
#     print(dict["roll no."])
# except:
#   print("error")
 

#file not found
try:    
    file=open("stud.txt","w")
    file.write("hell")
    file=open("stud.txt","r")
    print(file.read())
except:
    print("error")








