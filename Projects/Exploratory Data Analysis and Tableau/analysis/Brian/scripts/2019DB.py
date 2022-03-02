def load_and_process_all(filePath):
    import pandas as pd
    import statistics as stsc
    dfClean = (
        pd.read_csv(filePath,
        usecols = ["Rank", "Name", "Publisher", "Platform", "Genre", "Critic_Score","Year"]) # So far our only focus of work
        .sort_values(by= "Rank", ascending = True) # Cash money check
        #.loc[lambda x: x["Year"] >= 2000] # Check for only recent games
        .dropna(axis = 0, thresh = 2) # Drop any NA values completely
        #.loc[lambda x: x["Global_Sales"].between(15, 90.00)]
        #Excessive low number sales mess up our median so we are removing it for now by specifying values between 15-90
        .reset_index(drop=True) # Reset index so we don't mess up orders
    )


    df2019 = (
        dfClean
        #.loc[lambda x: x["Rank"] <= 3500] # Nothing ranked lower than 2500
        #.assign(Averaged_Sales = lambda x: x["Global_Sales"]/stsc.median(dfClean["Global_Sales"])) #Putting the sales number over its median to try and mitigate issues from the outliers
        #.sort_values(by= "Averaged_Sales", ascending = False) # Re-sort in case any vales got changed
        .reset_index(drop = True) # Order things nicely
    )

    return df2019

load_and_process_all("../../data/raw/vgsales-12-4-2019.csv")
