# NOTE: This assumes the csv is named "collection.csv", and is in the same directory as the program
#       The output is "decklist.ydk" in the same directory as the program

# Imports
import pandas as pd

# Get columns
df = pd.read_csv('collection.csv')
quantity = df['cardq']
ids = df['cardid']

# Open the file and enter the main header
f = open('decklist.ydk', 'w+')
f.write('#main\n')

# Loop over the columns
for q, id in zip(quantity, ids):
    # Print id to file q times
    for x in range(q):
        f.write(str(id) + '\n')

# Add extra and side headers
f.write('\n#extra\n')
f.write('\n!side\n')

# Close the file
f.close()
