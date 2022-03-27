import pandas as pd
import statistics
import plotly.express as px

df = pd.read_csv('Data Story Project.csv')

fig = px.scatter(df, y = 'quant_saved', color = 'wealthy')
fig.show()

import csv
import plotly.graph_objects as go

with open('Data Story Project.csv', newline = '') as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1
fig = go.Figure(go.Bar(x = ['Reminded', 'Not Reminded'], y = [total_people_given_reminder, (total_entries-total_people_given_reminder)]))
fig.show()

all_savings = []

for data in savings_data:
  all_savings.append(float(data[0]))
print(f'mean-{statistics.mean(all_savings)}')
print(f'median-{statistics.median(all_savings)}')
print(f'mode-{statistics.mode(all_savings)}')

reminded_savings = []
not_reminded_savings = []

for data in savings_data:
  if int(data[3]) == 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

print("Reminded")
print()
print(f'mean-{statistics.mean(reminded_savings)}')
print(f'median-{statistics.median(reminded_savings)}')
print(f'mode-{statistics.mode(reminded_savings)}')
print(f'Std_Deviation-{statistics.stdev(reminded_savings)}')
print()
print("Not Reminded")
print()
print(f'mean-{statistics.mean(not_reminded_savings)}')
print(f'median-{statistics.median(not_reminded_savings)}')
print(f'mode-{statistics.mode(not_reminded_savings)}')
print(f'Std_Deviation-{statistics.stdev(not_reminded_savings)}')