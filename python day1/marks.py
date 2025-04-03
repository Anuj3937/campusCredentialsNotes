p1=int(input("enter marks 1 ="))
p2=int(input("enter marks 2 ="))
p3=int(input("enter marks 3 ="))
p4=int(input("enter marks 4 ="))
p5=int(input("enter marks 5 ="))
countt=0
if p1>=40 and p2>=40 and p3>=40 and p4>=40 and p5>=40:
    print("u passed buddy")
    countt+=1
else:
    print("u fail;")
total=p1+p2+p3+p4+p5
per=total/5.0
p22=input("enter sex")
if p22=="female" and countt==1 and per>=70.0:
    print("u got job")
else:
    ("u got no job")
if p22=="male" and countt==1 and per>=41.0:
    print("u got job")
else:
    ("u got no job")