import csv 

def extract_data(file): 
    actions = {}
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            price = int(row[1])
            gain = int(row[2])
            realised_gain = price * gain
            actions[row[0]] = (price, gain, realised_gain)
    return actions

def main():
    actions = extract_data('list-dactions.csv')
    print(actions)

if __name__ == "__main__":
    main()