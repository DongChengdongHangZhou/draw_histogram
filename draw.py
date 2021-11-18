import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
axis_size = 20

font_title = {'family' : 'Times New Roman',
'weight' : 'normal',
'size' : 30,
}

font_x_label = {'family' : 'Times New Roman',
'weight' : 'normal',
'size' : 30,
}

font_y_label = {'family' : 'Times New Roman',
'weight' : 'normal',
'size' : 30,
}

font_decorate = {'family' : 'Times New Roman',
'weight' : 'normal',
'size' : 25,
}

df = pd.read_excel('./test.xlsx')
n = df[df.columns.values[0]].unique().__len__()+1
random.seed(100)
c = ['darkblue', 'lightblue', 'peru', 'olivedrab', 'palegoldenrod', 'lavenderblush', 'purple', 'lightslategray', 'brown', 'lightblue', 'black', 'teal', 'tomato']
plt.figure(figsize=(20,15), dpi= 60)
plt.tick_params(labelsize=axis_size)
plt.bar(df[df.columns.values[0]], df[df.columns.values[1]], color=c, width=.5)
for i, val in enumerate(df[df.columns.values[1]].values):
    plt.text(i, val, str(format(val*100,'.2f'))+'%', horizontalalignment='center', verticalalignment='bottom', fontdict=font_decorate)

# Decoration
def to_percent(temp, position):
  return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.gca().set_xticklabels(df[df.columns.values[0]], rotation=30, horizontalalignment= 'right')
plt.title("Distribution of scale size", font_title)
plt.xlabel('Scales',font_x_label)
plt.ylabel('Ratio',font_y_label)
plt.ylim(0, 0.35)
plt.savefig('test.png')