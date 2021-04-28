# Imports
import pandas as pd
import sys

if len(sys.argv[:]) < 2:
        print('No ydks! Quiting!')
        exit()

#######setup
# Open the file and enter the main header
f = open('decklist.ydk', 'w+')
f.write('#main\n')
extra_list = []

#######loop over each set of cards
for fname in sys.argv[1:]:
    print('Working on %s'%fname)
    # Get columns from collection
    df = pd.read_csv(fname)
    main = True
    for i in df.values[:-1]:
        if main==True and i != '#extra ': 
            f.write(str(i[0]) + '\n')
        elif i == '#extra ':
            main = False
        else:
            extra_list.append(i)

# Add extra and side headers
f.write('\n#extra\n')
for id in extra_list:
    f.write(str(id[0]) + '\n')

f.write('\n!side\n')

# Close the file
f.close()
