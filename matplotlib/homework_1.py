from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",size='large')
fig=plt.figure(figsize=(20,8),dpi=80)

x=range(11,31)
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

plt.plot(x,y)
_x=list(x)
_xtick_labels=["{}岁".format(i) for i in range(11,31)]
plt.xticks(_x,_xtick_labels,fontproperties=my_font)
_y=list(range(min(y),max(y)+1))
_ytick_labels=["{}个".format(i) for i in range(min(y),max(y)+1)]
plt.yticks(_y,_ytick_labels,fontproperties=my_font)
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("个数",fontproperties=my_font)
plt.title("每年交往女朋友数量",fontproperties=my_font)
#plt.savefig("./homework1.png")

plt.show()
