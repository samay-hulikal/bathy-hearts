import pandas as pd
from pathlib import Path

def load_all_data(data_dir):
    """
    Import csv files from a directory.

    Input: 
        String containing the directory's path.

    Output:
        Combined dataframes sorted by the pattern of columns.
    """

    # Importing & sorting
    pth =  Path(data_dir)
    csv_files = sorted([f for f in pth.glob("*.csv") if not f.name.startswith(".")]) # Filtering out pesky .csv files

    # Grouping files by column list
    groups = {} # Dictionary of all column patterns
    for f in csv_files:
        df = pd.read_csv(f)
        cols = tuple(df.columns.tolist())

        if cols not in groups:
            groups[cols] = []
        groups[cols].append(f)
 
    # print(f"Found {len(groups)} different column patterns:\n")
    # for c, f in groups.items():
    #     print(f"{len(f)} files:")
    #     print(f"Columns: {list(c)}")
    #
    # Creating a dataframe for each group
    data_frames = {} # Dictionary of dataframes

    for cols, fls in groups.items():
        df = pd.concat([pd.read_csv(f) for f in fls], ignore_index=True)
        df["Time"] = pd.to_datetime(df["Time"])
        df = df.sort_values("Time")
        data_frames[cols] = df
    
    # Return the dictionary
    return data_frames
