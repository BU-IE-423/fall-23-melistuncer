import pandas as pd
import gzip
import matplotlib.pyplot as plt  

with gzip.open('all_ticks_long.csv.gz', 'rt') as file:
    df = pd.read_csv(file)


company_names = df['short_name'].unique()
our_companies = ['AKSA', 'ARCLK', 'GARAN', 'MGROS', 'OTKAR', 'THYAO']


#our_companies_table = df['short_name'].str.contains('|'.join(our_companies))
#df_selected = df[our_companies_table]     # our companys' data frame
#df_chronological = (df_selected.sort_values (by= 'timestamp')).reset_index(drop=True)   # sort by chronological order



aksa_df = df[df['short_name'].str.contains('AKSA')].sort_values(by= 'timestamp').reset_index(drop=True)
arclk_df = df[df['short_name'].str.contains('ARCLK')].sort_values(by= 'timestamp').reset_index(drop=True)
garan_df = df[df['short_name'].str.contains('GARAN')].sort_values(by= 'timestamp').reset_index(drop=True)
mgros_df = df[df['short_name'].str.contains('MGROS')].sort_values(by= 'timestamp').reset_index(drop=True)
otkar_df = df[df['short_name'].str.contains('OTKAR')].sort_values(by= 'timestamp').reset_index(drop=True)
thyao_df = df[df['short_name'].str.contains('THYAO')].sort_values(by= 'timestamp').reset_index(drop=True)

'''print(aksa_df)
print(arclk_df)
print(garan_df)
print(mgros_df)
print(otkar_df)
print(thyao_df)'''            # printed and checked if all the indices span over at least 2 years


aksa_df_times = aksa_df['timestamp'].str.split('[-T:]', expand=True)
arclk_df_times = arclk_df['timestamp'].str.split('[-T:]', expand=True)
garan_df_times = garan_df['timestamp'].str.split('[-T:]', expand=True)
mgros_df_times = mgros_df['timestamp'].str.split('[-T:]', expand=True)
otkar_df_times = otkar_df['timestamp'].str.split('[-T:]', expand=True)
thyao_df_times = thyao_df['timestamp'].str.split('[-T:]', expand=True)


aksa_merged_df = pd.concat([aksa_df, aksa_df_times], axis=1)
columns = ['company', 'timestamp', 'price', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']

aksa_merged_df.columns = columns


grouped_year = aksa_merged_df.groupby('Year')

aksa_year_dfs = []
for group_name, group_df in grouped_year:
    aksa_year_dfs.append(group_df)

grouped_month = []
for i in aksa_year_dfs:
    x = i.groupby('Month')
    for group_name, group_df in x:
        grouped_month.append(group_df)
    

#print(grouped_month[-1])


def form_boxplot(df):
    plt.figure(figsize=(8,6))
    plt.boxplot(df['price'])
    plt.show()


form_boxplot(grouped_month[1], grouped_month[2])





'''plt.figure(figsize=(8,6))
plt.boxplot(aksa_df['price'])
plt.xlabel('timestamp')
plt.ylabel('price')
plt.title('Box Plot')

plt.show()'''

