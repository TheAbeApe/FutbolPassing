import pandas as pd
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

#read in the CSV file
df = pd.read_csv('passingdata/valladolidA.csv')
#filtering the data to only include Barcelona
df=df[df['teamId']== 'Barcelona']
df['passer'] = df['playerId']
df['recipient'] = df['playerId'].shift(-1)

#filter data for sucessful passes
passes=df[df['type']=='Pass']
sucessful=passes[passes['outcome']=='Successful']

#accounting for the substitutions
subs = df[df['type']=='SubstitutionOff']
subs = subs['minute']
firstSub= subs.min()

successful= sucessful[sucessful['minute']<firstSub]

#changing the data type of the passer and recipient columns to integers
pas=pd.to_numeric(successful['passer'],downcast='integer')
rec=pd.to_numeric(successful['recipient'],downcast='integer')

successful['passer'] = pas
successful['recipient'] = rec

#average position of the players
average_positions = successful.groupby('passer').agg({'x':['mean'], 'y':['mean','count']})
average_positions.columns = ['x','y','count']

#pass between players
pass_between = successful.groupby(['passer','recipient']).id.count().reset_index() #study these two lines of code
pass_between.rename({'id':'pass_count'},axis='columns',inplace=True)

pass_between = pass_between.merge(average_positions, left_on='passer', right_index=True)
pass_between = pass_between.merge(average_positions, left_on='recipient', right_index=True,suffixes=['','_end'])

#filtering passes that are greater than 5
pass_between = pass_between[pass_between['pass_count']>5]

#plotting the pitch
pitch = Pitch(pitch_type='statsbomb',
              pitch_color='#22312b', line_color='white',) 
fig, ax = pitch.draw( constrained_layout=False,tight_layout=True)

arrows = pitch.arrows(1.2*pass_between.x, .8*pass_between.y, 1.2*pass_between.x_end, .8*pass_between.y_end, width=3, headwidth=3, color='white',zorder=1,alpha=.5,ax=ax)

nodes=pitch.scatter(1.2*average_positions.x, .8*average_positions.y, s=300, color='grey', edgecolors='black', linewidth=2.5, alpha=1, zorder=1,ax=ax)

plt.show()
plt.savefig('passingpngs/valladolidA.png')