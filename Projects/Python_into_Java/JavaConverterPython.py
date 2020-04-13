def convert(a ="python.py"):
    file = open("/home/kaushik/PROGRAMMING/python/Projects/Python_into_Java/d.py","r")
    demo = open("d.java","w")
    demo.write("class D{\npublic static void main(String[] args){\n")
    for i in file.readlines():
        if '"' in i and "=" in i or "'" in i and "=" in i:
            j = i.strip(" ")
            j = j.split(" ")
            j = "".join(j)
            demo.write(f"String {i}"+";")

        if "print(" in i:
            j = i.strip()
            j = j.split(" =")
            j = "".join(j)
            if "end=" in i:
                pass
            else:
                j=j.split()
                print(j)
                j.remove("(")
                j = j.remove(")")
                print("j")
                demo.write("\nSystem.out.println();")
    demo.write("\n}\n}")
convert()
