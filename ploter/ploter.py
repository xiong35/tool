
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

font = fm.FontProperties(fname=R'SIMHEI.TTF')


with open('./data.txt', 'r', encoding='utf8') as fr:
    lines = fr.readlines()

opts = lines[1].split(',')

data = lines[3:]

x = []

if data[1][0] == ',':
    dataNum = len(data)
    begin = float(data[0][0])
    end = float(data[-1][0])
    step = (end-begin)/(dataNum-1)
    for i in range(dataNum):
        x.append(begin+step*i)
else:
    for item in data:
        x.append(float(item.split(',')[0].strip('\n')))

y = []

for item in data:
    y.append(float(item.split(',')[-1].strip('\n')))

if opts[3] in 'yY':
    plt.scatter(x, y, c='#0077ff', alpha=0.8,s=14)
if opts[4].strip('\n') in 'yY':
    plt.plot(x, y, c='#0077ff', alpha=0.8)

plt.ylabel(opts[1])
plt.xlabel(opts[0])

plt.title(opts[2], fontproperties=font)

plt.savefig(f'{opts[2]}.png')
plt.show()
