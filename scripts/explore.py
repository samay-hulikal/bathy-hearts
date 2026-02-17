import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_all_data

# Path to the directory containing heart rate data
data_directory = "/home/samay/Desktop/Samay/Collective Behavior/Deep sea data/Heart/smoothed_highfreq_for_orit"

# Dataframes by column patterns
heart_dict = load_all_data(data_directory)

# Time limits for each pattern
for i, (cl, fls) in enumerate(heart_dict.items()):
    print(f"Pattern {i}:")
    print(f"  Columns: {list(cl)}")
    print(f"  Start: {fls['Time'].min()}")
    print(f"  End: {fls['Time'].max()}")
    print(f"  Duration: {fls['Time'].max() - fls['Time'].min()}")

"""
Pattern 0: Aq2
    Start: 2025-11-27 16:38
    End: 2025-12-17 14:33

Pattern 1: Aq1
    Start: 2025-11-27 16:30
    End: 2026-01-05 14:38

Pattern 2: Aq2-1
    Start: 2025-12-12 14:13
    End 2026-01-05 14:42
"""
# Plotting the data from the sorted files from start_date to end_date for pattern number pt
start_date = "2025-12-12 15:00:00"
end_date = "2025-12-22 23:10:00"
pt = 2
# resampling_interval = "10min" # 100ms, 1s, 1min, 10min, 1h
resampling_interval = "1h" # 100ms, 1s, 1min, 10min, 1h

heart_vals = list(heart_dict.items())
clm, df_full = heart_vals[pt]
df_chunk = df_full[(df_full["Time"] >= pd.to_datetime(start_date)) & (df_full["Time"] <= pd.to_datetime(end_date))] # Extracting the chunk of time needed
df = df_chunk.set_index("Time").resample(resampling_interval).mean().reset_index() # Resampled by taking the mean every minute

fig, axes = plt.subplots(len(clm) - 1, 1, figsize = (12, 24), sharex=True) #Plots share x-axis
for i, ax in enumerate(axes):
    ax.plot(df["Time"], df[clm[i + 1]], linewidth=0.3) # clm[i + 1] to prevent a Time vs Time plot
    ax.set_ylabel(clm[i + 1])

axes[-1].set_xlabel("Time")
plt.tight_layout()
print(f"Plotting pattern {pt}")
plt.savefig(f"prelim-figs/resampled_{pt}_{resampling_interval}_{start_date}_{end_date}.pdf")
print("Saved plot!")

plt.close(fig) # Saves memory, apparently
