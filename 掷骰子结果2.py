from 掷骰子 import Die
import pygal

die1=Die()
die2=Die()
results=[]

for roll_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)

frequencies=[]
max_result=die1.num_sides+die2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
    
hist=pygal.Bar()

hist.title="Results of rolling one D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('3.svg')