import re
a = input("Enter time in 12-hour clock : ").strip(" ")
if re.search("PM$",a):
    a = a[:len(a)-2]
    a = a.split(":")
    if "0" ==a[0][0]:
        a[0] = a[0][1:]
        a[0] = int(a[0])+12
        a[0] = str(a[0])

    elif 12>int(a[0])>9:
        a[0] = int(a[0])+12
        a[0] = str(a[0])
    print(":".join(a))


else:
    a = a[:len(a)-2]
    a = a.split(":")
    if a[0][:2]=="12":
        a[0] = "00"
    print(":".join(a))

    
        


