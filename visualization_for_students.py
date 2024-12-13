from imports import *

all_time_slots = [
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

file_path = "datasets/schedule1000.csv"
data = pd.read_csv(file_path)

group_to_display = "UWR.OR4.NYJ.8726.KYV"
data = data[data["group"] == group_to_display]

data["date"] = pd.to_datetime(data["datetime"].str.split(" ").str[0])
data["time_slot"] = data["datetime"].apply(lambda x: x.split(" ", 1)[1])

unique_dates = data["date"].unique()
full_index = pd.MultiIndex.from_product(
    [all_time_slots, unique_dates], names=["time_slot", "date"]
)
data = data.set_index(["time_slot", "date"]).reindex(full_index).reset_index()
data["details"] = data["course"] + ", " + data["lecturer"] + ", " + data["classroom"]

pivot_table = data.pivot_table(
    index="time_slot",
    columns="date",
    values="details",
    aggfunc=lambda x: "\n".join(x) if pd.notna(x).any() else "",
)

pivot_table = pivot_table.replace("", pd.NA).dropna(how="all")

pivot_table = pivot_table.reindex(all_time_slots).dropna(how="all")


def wrap_text(text, width=15):
    if pd.isna(text) or not text.strip():
        return ""
    return "\n".join(textwrap.wrap(text, width=width))


fig, ax = plt.subplots(figsize=(18, 10))
ax.set_axis_off()

table = Table(ax, bbox=[0, 0, 1, 1])

n_cols = len(pivot_table.columns)
n_rows = len(pivot_table.index) + 1

header_cell = table.add_cell(
    0, 0, width=2, height=0.5, text="Time / Date", loc="center", facecolor="lightgrey"
)
header_cell.get_text().set_fontsize(14)
header_cell.get_text().set_weight("bold")

for col, date in enumerate(pivot_table.columns):
    cell = table.add_cell(
        0,
        col + 1,
        width=1.5,
        height=0.5,
        text=date.strftime("%Y-%m-%d"),
        loc="center",
        facecolor="lightgrey",
    )
    cell.get_text().set_fontsize(14)
    cell.get_text().set_weight("bold")

for row, time_slot in enumerate(pivot_table.index):
    cell = table.add_cell(
        row + 1,
        0,
        width=2,
        height=0.5,
        text=time_slot,
        loc="center",
        facecolor="lightgrey",
    )
    cell.get_text().set_fontsize(12)
    for col, date in enumerate(pivot_table.columns):
        value = pivot_table.loc[time_slot, date]
        wrapped_value = wrap_text(value, width=15)
        cell = table.add_cell(
            row + 1,
            col + 1,
            width=1.5,
            height=0.5,
            text=wrapped_value,
            loc="center",
            facecolor="white",
        )
        cell.get_text().set_fontsize(12)

ax.add_table(table)

plt.title(f"Exam schedule for group: {group_to_display}", fontsize=18, pad=20)
plt.show()
