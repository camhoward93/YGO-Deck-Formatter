# NOTE: The output name still has backslashes on the special characters from the php file
#       Ultimately this doesn't matter since we can compare by ID, but it can be cleaned up later if desired
#       The runtime is also pretty slow with larger databases. The code can be parallelized if needed

# Imports
import csv
import re

# Functions
def create_header(attributes, outfile):
    # Fill the top line of the outfile with the attributes
    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(attributes)

def download_cards(infile, regex):
    # declare result list
    cardList = list()

    # DEBUG_COUNT = 0

    # for each line in the input file (NOTE: I think our input php is one long line)
    for line in open(infile):
        # for each card found
        for match in re.finditer(regex, line):
            # add fields to card list
            print(match.group(1))
            cardList.append([match.group(1), match.group(2), match.group(3)])
            # if(DEBUG_COUNT > 5):
            #     break
            # ++DEBUG_COUNT

    # return the card list
    return cardList

def upload_cards(cardList, outfile):
    # Fill the csv with the card list
    with open(outfile, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for card in cardList:
            writer.writerow(card)

# Declare variables
outputFile = 'database.csv'
inputFile = 'cardDatabase2-9.php'
header = ['Card ID', 'Card Name', 'Card Type'] # more can be added based on needs
pattern = re.compile(r'(?=\{\"id\":(\d+),\"name\":\"(.+?)\",\"type\":\"(.+?)\".*\},)')

# Create header row of csv
create_header(header, outputFile)
# Load the cards from the php
cards = download_cards(inputFile, pattern)
# Fill the csv with the card list
upload_cards(cards, outputFile)

