# NOTE: This assumes the csv is named "collection.csv", and is in the same directory as the program
#       The output is "decklist.ydk" in the same directory as the program

# Imports
import pandas as pd

# Get columns from collection
df = pd.read_csv('collection.csv')
quantity = df['cardq']
ids = df['cardid']

# Get extra deck ids
df = pd.read_csv('database.csv')
extra_ids = df[df['Card Type'].isin(['Fusion Monster', 'Synchro Monster', 'Synchro Tuner Monster', 'Synchro Pendulum Effect Monster', 'XYZ Monster', 'XYZ Pendulum Effect Monster', 'Link Monster', 'Pendulum Effect Fusion Monster'])]['Card ID'].values
extra_list = []

# Open the file and enter the main header
f = open('decklist.ydk', 'w+')
f.write('#main\n')

# Loop over the columns
for q, id in zip(quantity, ids):
    # Check if card is extra deck card
    if id in extra_ids:
        #if so add to extra deck list q times
        for x in range(q):
            extra_list.append(id)
        continue
    else:
        # Print id to file q times
        for x in range(q):
            f.write(str(id) + '\n')

# Add extra and side headers
f.write('\n#extra\n')
for id in extra_list:
    f.write(str(id) + '\n')

f.write('\n!side\n')

# Close the file
f.close()
