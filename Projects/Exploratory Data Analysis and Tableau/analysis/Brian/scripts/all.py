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
        .loc[lambda x: x["Global_Sales"].between(5, 90.00)] # Remove the overkill outlier Wii sport saes at 80
        #Excessive low number sales mess up our median so we are removing it for now by specifying values between 5-90
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

def load_and_process_allG(filePath):
    import pandas as pd
    import statistics as stsc
    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Publisher", "Platform", "Genre", "Global_Sales", "Year"]) # So far our only focus of work
        .sort_values(by= "Global_Sales", ascending = False) # Cash money check
        #.loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .dropna(axis = 0, thresh = 3) # Drop any NA values completely
        .loc[lambda x: x["Global_Sales"].between(5, 90.00)] # Remove the overkill outlier Wii sport saes at 80
        #Excessive low number sales mess up our median so we are removing it for now by specifying values between 5-90
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )


    dfWii = (
        dfClean
        .loc[lambda x: x["Rank"] <= 3500] # Nothing ranked lower than 2500
        .assign(Averaged_Sales = lambda x: x["Global_Sales"]/stsc.median(dfClean["Global_Sales"])) #Putting the sales number over its median to try and mitigate issues from the outliers
        .sort_values(by= "Averaged_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )

    dfHi = (
        dfWii
        .groupby(by = "Rank")
    )


    return dfWii
