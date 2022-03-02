def sales_by_region(filepath):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(filepath)

    dfGR = df[["Rank","Name","Genre","Year","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]

    dfGR_Clean = (
      dfGR
    .dropna(axis=0) #Drop the rows which have missing values
    .reset_index(drop = True)
    )
    dfGR_BN = (
        dfGR_Clean
    .loc[lambda x: x["Year"] >= 2000] # Filter for games in this century
    .loc[lambda x: x["Rank"] <= 2500] # Only looking for games ranked 2500 or less
    .reset_index(drop = True)
    )

    dfGR_NA = (dfGR_BN[["Rank","Genre","Year","NA_Sales"]])
    dfGR_EU = (dfGR_Clean[["Rank","Genre","Year","EU_Sales"]])
    dfGR_JP = (dfGR_Clean[["Rank","Genre","Year","JP_Sales"]])
    dfGR_Other = (dfGR_Clean[["Rank","Genre","Year","Other_Sales"]])

    P1 = (
   dfGR_NA[['Genre','NA_Sales']]
    .groupby('Genre').sum('NA_Sales')
    )
    P2 = (
   dfGR_EU[['Genre','EU_Sales']]
    .groupby('Genre').sum('EU_Sales')
    )
    P3 = (
   dfGR_JP[['Genre','JP_Sales']]
    .groupby('Genre').sum('JP_Sales')
    )
    P4 = (
   dfGR_Other[['Genre','Other_Sales']]
    .groupby('Genre').sum('Other_Sales')
    )
    SbG = P1
    SbG['EU_SALES']= P2['EU_Sales']
    SbG['JP_SALES']= P3['JP_Sales']
    SbG['OTHER_SALES']= P4['Other_Sales']

    return SbG

def genre_popularity_old(filepath):
    import pandas as pd
    df = pd.read_csv(filepath)

    dfGR = df[["Rank","Name","Genre","Year","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]

    dfGR_Clean = (
      dfGR
    .dropna(axis=0) #Drop the rows which have missing values
    .reset_index(drop = True)
    )
    dfGR_old = (
    dfGR_Clean
    .loc[lambda x: x["Year"] <= 1999] # Filter for 1980-1999
    .sort_values(by = 'Year' , ascending = True)
    )

    return dfGR_old

def genre_popularity_new(filepath):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(filepath)

    dfGR = df[["Rank","Name","Genre","Year","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]

    dfGR_Clean = (
      dfGR
    .dropna(axis=0) #Drop the rows which have missing values
    .reset_index(drop = True)
    )

    dfGR_new = (
    dfGR_Clean
    .loc[lambda x: x["Year"] >= 2000] # Filter for 2000-latest
    .sort_values(by = 'Year' , ascending = True)
    )
    return dfGR_new

def top_genre_best(filepath):
    import pandas as pd
    import numpy as np

    df = pd.read_csv(filepath)

    dfGR = df[["Rank","Name","Genre","Year","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]

    dfGR_Clean = (
      dfGR
    .dropna(axis=0) #Drop the rows which have missing values
    .reset_index(drop = True)
    )
    dfp = dfGR_Clean[['Rank','Genre','Year']]

    dfp_Clean = (
    dfp
    .loc[lambda x: x["Year"] >= 2000] # Filter for games in this century
    .loc[lambda x: x["Rank"] <= 100] #Best 100 over this last century so far
    .dropna(axis = 0)
    .reset_index(drop = True)
    .sort_values(by = 'Year',ascending = True)
    )

    return dfp_Clean

#top_genre_best("../../data/raw/Video_game_sales_db.csv")
