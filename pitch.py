import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

#read in the data 
df = pd.read_csv('passingdata/messibetis.csv')

df['x'] = df['x']*1.2
df['y'] = df['y']*.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*.8

#base pitch
pitch = Pitch(pitch_type='statsbomb',
              pitch_color='#22312b', line_color='white',) 
pitch.draw( constrained_layout=True)
plt.gca().invert_yaxis()


for x in range(len(df['x'])):
    if df['outcome'][x] == 'Successful':
        plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='green')
        plt.scatter(df['x'][x], df['y'][x], color='green')
    if df['outcome'][x] == 'Unsuccessful':
        plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='red')
        plt.scatter(df['x'][x], df['y'][x], color='red')

plt.title('Messi passes vs Betis',color= 'black', size=20)

plt.show()
plt.savefig('passingpngs/messibetis.png')

