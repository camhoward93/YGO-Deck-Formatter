# NOTE: This assumes the csv is named "collection.csv", and is in the same directory as the program
#       The output is "decklist.ydk" in the same directory as the program

# Imports
import pandas as pd
import sys

if len(sys.argv[:]) < 2:
        print('No cards! Quiting!')
        exit()

#######setup
# Open the file and enter the main header
f = open('decklist.ydk', 'w+')
f.write('#main\n')

# Get extra deck ids
df = pd.read_csv('database.csv')
extra_ids = df[df['Card Type'].isin(['Fusion Monster', 'Synchro Monster', 'Synchro Tuner Monster', 'Synchro Pendulum Effect Monster', 'XYZ Monster', 'XYZ Pendulum Effect Monster', 'Link Monster', 'Pendulum Effect Fusion Monster'])]['Card ID'].values
extra_list = []

#######loop over each set of cards
for fname in sys.argv[1:]:
    if fname=='database.csv':
        continue
    else:
        print('Working on %s'%fname)
    # Get columns from collection
    df = pd.read_csv(fname)
    quantity = df['cardq']
    ids = df['cardid']

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
