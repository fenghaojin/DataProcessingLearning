from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",size='large')
fig=plt.figure(figsize=(20,8),dpi=80)

x_3=range(1,32)
x_10=range(41,72)
y_3=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

plt.scatter(x_3,y_3,label="三月份")
plt.scatter(x_10,y_10,label="十月份")
_x=list(x_3)+list(x_10)
_xtick_labels=["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-40) for i in x_10]
plt.xticks(_x[::3],_xtick_labels[::3],fontproperties=my_font,rotation=90)
plt.legend(prop=my_font,loc=0)
plt.xlabel("日期",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("月份温度散点图",fontproperties=my_font)

plt.show()
