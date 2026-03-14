import pandas as pd

FOOTBALL_CSV_LINK = 'https://www.football-data.co.uk/mmz4281/2526/E0.csv'

df_premiere21 = pd.read_csv(FOOTBALL_CSV_LINK) # reading the csv file link address
print(df_premiere21)


# Renaming Column using rename(columns={'current_column_name': 'new_column_name'})
df_premiere21.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)
print(df_premiere21)
