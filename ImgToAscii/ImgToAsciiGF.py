from PIL import Image
m=Image.open('t.jpg')
p=m.load()
g=list("@%#*+=-:. ")
w,h=m.size
x=lambda x:g[(int)((x[0]+x[1]+x[2])/3)//26-1]
for i in range(h):
    r=""
    for j in range(w):r+=x(p[j,i])
    print(r)