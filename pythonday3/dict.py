# mydict={"name":"anuj"
#         ,"roll":23}
# print(mydict)
# print(type(mydict))
d={101:"anuj",102:"ssa",103:"asa",101:"pathal"}
print(d)
a=d[102]
print(a)
a="peter"
print(a)
for x in d :
    print(x)
for x in d.values():
    print(x)
for x,Y in d.items():
    print(x,Y)
#HOW TO ADD A KEY AND VALUE PAIR
d["mob no."]=45631189
print(d)
d.pop(101)
print(d)