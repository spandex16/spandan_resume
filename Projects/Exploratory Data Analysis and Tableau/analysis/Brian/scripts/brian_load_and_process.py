def load_and_process_all(filePath):
    import pandas as pd
    import statistics as stsc
    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Publisher", "Platform", "Genre", "Global_Sales", "Year"]) # So far our only focus of work
        # The global sales account for all regional sales so I am omitting the sales by region for this exploration
        .sort_values(by= "Global_Sales", ascending = False) # Cash money check
        #.loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .dropna(axis = 0, thresh = 3) # Drop any NA values completely
        .loc[lambda x: x["Global_Sales"].between(9, 90.00)]
        #Excessive low number sales mess up our median so we are removing it for now by specifying values between 15-90
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )


    dfAll = (
        dfClean
        .loc[lambda x: x["Rank"] <= 3500] # Nothing ranked lower than 2500
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/stsc.median(dfClean["Global_Sales"])) #Putting the sales number over its median to try and mitigate issues from the outliers
        .sort_values(by= "Averaged_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )
    return dfAll

def load_and_process_wii(filePath):
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


def load_and_process_nintendo(filePath):
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

    dfNin = (
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
    return dfNin


#dfAllM = load_and_process_all("../../data/raw/Video_game_sales_db.csv")
#dfWiiM= load_and_process_wii("../../data/raw/Video_game_sales_db.csv")
#dfNinM= load_and_process_nintendo("../../data/raw/Video_game_sales_db.csv")
#dfAllM
