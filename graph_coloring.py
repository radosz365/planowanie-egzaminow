from imports import *

data_path = "datasets/dataset1000.csv"
df = pd.read_csv(data_path)

G = nx.Graph()

for idx, row in df.iterrows():
    G.add_node(idx, lecturer=row["lecturer"], group=row["group"], room=row["classroom"])

for i, row1 in df.iterrows():
    for j, row2 in df.iterrows():
        if i < j:
            if (
                row1["lecturer"] == row2["lecturer"]
                or row1["group"] == row2["group"]
                or row1["classroom"] == row2["classroom"]
            ):
                G.add_edge(i, j)

coloring = nx.coloring.greedy_color(G, strategy="largest_first")

start_date = datetime(2025, 1, 30)
time_slots_per_day = [
    "8:00 - 8:45",
    "9:00 - 9:45",
    "10:00 - 10:45",
    "11:00 - 11:45",
    "12:00 - 12:45",
    "13:00 - 13:45",
    "14:00 - 14:45",
    "15:00 - 15:45",
    "16:00 - 16:45",
]
slot_index = 0
current_date = start_date
schedule = {}

for node, color in sorted(coloring.items(), key=lambda x: x[1]):
    while current_date.weekday() >= 5:
        current_date += timedelta(days=1)
    time_slot = time_slots_per_day[slot_index]
    schedule[node] = f"{current_date.date()} {time_slot}"

    slot_index += 1
    if slot_index >= len(time_slots_per_day):
        slot_index = 0
        current_date += timedelta(days=1)

df["datetime"] = df.index.map(schedule)

output_path = "datasets/schedule1000.csv"
df.to_csv(output_path, index=False)

print(f"Schedule saved to {output_path}")
