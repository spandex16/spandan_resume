def load_and_process_Nintendo(filePath):
    import pandas as pd
    import statistics as stsc

    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Publisher", "Platform", "Genre", "Global_Sales", "Year"]) # So far our only focus of work
        .sort_values(by= "Global_Sales", ascending = False) # Cash money check
        .dropna(axis = 0, thresh = 3) # Drop any NA values completely
        .loc[lambda x: x["Global_Sales"].between(5, 90.00)] # Remove the overkill outlier Wii sport saes at 80
        #Excessive low number sales mess up our median so we are removing it for now by specifying values between 5-90
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )

   # print(stsc.median(dfClean["Global_Sales"]))
   # print(stsc.mean(dfClean["Global_Sales"]))

    dfWii = (
        dfClean
        .loc[(dfClean["Publisher"] == "Nintendo")]
        #.loc[(dfClean["Platform"] == "Wii") | (dfClean["Platform"] == "DS")]
        .loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .loc[lambda x: x["Rank"] <= 2500] # Nothing ranked lower tan 2500
        #.assign(median = stsc.median(dfClean["Global_Sales"]))
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/stsc.median(dfClean["Global_Sales"])) #Putting the sales number over its median to try and mitigate issues from the outliers
        .sort_values(by= "Global_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )
    return dfWii

#load_and_process_Nintendo("../../data/raw/Video_game_sales_db.csv")
