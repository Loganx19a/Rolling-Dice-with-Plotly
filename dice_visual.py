import plotly.express as px

from die import Die

# create two D6 
die_1 = Die()
die_2 = Die()

# make some rolls, and store the results in a list
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# additional chart customization
fig.update_layout(xaxis_dtick=1)

fig.show()