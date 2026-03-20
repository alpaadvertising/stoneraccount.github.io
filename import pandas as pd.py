import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import matplotlib.dates as mdates # type: ignore
from datetime import datetime

# 1. Setup Data from your provided list
data = [
    ["Entity formation", "2026-02-01", "2026-03-23", "Legal"],
    ["PEZA & Gov Docs", "2026-02-01", "2026-04-01", "Legal"],
    ["Partner Selection (Bank/Acc)", "2026-02-01", "2026-04-01", "Legal"],
    ["Logistics Selection", "2026-02-01", "2026-03-01", "Legal"],
    ["Site Selection", "2026-04-01", "2026-06-01", "Infrastructure"],
    ["Trademarks Registration", "2026-04-01", "2026-07-01", "Legal"],
    ["Paste Wax Process Design", "2026-03-01", "2026-04-15", "Paste Wax"],
    ["Paste Wax Equip Install", "2026-05-02", "2026-10-01", "Paste Wax"],
    ["IGRC Tool Setup", "2026-05-01", "2026-07-01", "IGRC Tool"],
    ["Safety Training", "2026-09-02", "2026-10-01", "Operations"]
]

df = pd.DataFrame(data, columns=["Task", "Start", "End", "Category"])
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = (df['End'] - df['Start']).dt.days

# 2. Assign Colors by Category
colors = {"Legal": "#3498db", "Infrastructure": "#e67e22", 
          "Paste Wax": "#2ecc71", "IGRC Tool": "#9b59b6", "Operations": "#f1c40f"}

# 3. Plotting
fig, ax = plt.subplots(figsize=(12, 8))

for i, task in df.iterrows():
    ax.barh(task['Task'], task['Duration'], left=task['Start'], 
            color=colors.get(task['Category'], "gray"), edgecolor='black')

# Formatting the Timeline
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
plt.title("Philippines Market Entry - Project Gantt Chart 2026", fontsize=16)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis() # Put first task at the top

plt.tight_layout()
plt.savefig("Philippines_Entry_Gantt.pdf") # Saves the PDF
plt.show()