def load_and_process(filePath):
    import pandas as pd
    import statistics as stsc

    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Genre", "Global_Sales", "Year", "Platform"]) # So far our only focus of work
        .sort_values(by = "Global_Sales", ascending = False) # Cash money check
        .dropna(axis = 0, thresh = 3) # Drop any NA values completely
        .loc[lambda x: x["Global_Sales"].between(5, 90.00)] # Remove the overkill outlier Wii sport saes at 80
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )

    dfWii = (
        dfClean
        .loc[lambda x: x["Platform"] == "Wii"] # We love Wii only wanna play Wii
        .loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .loc[lambda x: x["Rank"] <= 2500] # Nothing ranked lower tan 2500
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/stsc.median(dfClean["Global_Sales"])) # Average out sales
        .sort_values(by= "Global_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )
    return dfWii


#load_and_process("../../data/raw/Video_game_sales_db.csv")
