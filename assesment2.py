import csv

def search(state, cost_rating, operation):
    file = open('hotels.csv', 'r')
    excel_file = csv.reader(file)

    vals = []
    if cost_rating == 'cost':
        cos_rat = 3
    else:
        cos_rat = 4

    # highest :
    def highest(cos_rat):
        st = state
        if state == 'India':
            st = ['Maharashtra', 'Karnataka', 'Tamilnadu']
        for row in excel_file:
            if row[2] in st:
                vals.append(row)
        if cost_rating == 'cost':
            l = [item[-2] for item in vals]
            l = max([float(i) for i in l])
        else:
            l = [item[-1] for item in vals]
            l = max([float(i) for i in l])
        for i in vals:
            if float(i[cos_rat]) == l:
                print('Hotel with highest '+ cost_rating +' in ' + i[2] + ' is '+i[1]+' with '+cost_rating+' '+str(l))

    # Cheapest :
    def cheapest(cos_rat):
        st = state
        if state=='India':
            st = ['Maharashtra', 'Karnataka', 'Tamilnadu']
        for row in excel_file:
            if row[2] in st:
                vals.append(row)
        if cost_rating == 'cost':
            l = [item[-2] for item in vals]
            l = min([float(i) for i in l])
        else:
            l = [item[-1] for item in vals]
            l = min([float(i) for i in l])
        for i in vals:
            if float(i[cos_rat]) == l:
                print('Hotel with cheapest '+ cost_rating +' in ' + i[2] + ' is '+i[1]+' with '+cost_rating+' '+str(l))

    # Average :
    def average(cos_rat):
        st = state
        if state == 'India':
            st = ['Maharashtra', 'Karnataka', 'Tamilnadu']
        for row in excel_file:
            if row[2] in st:
                vals.append(row)
        if cost_rating == 'cost':
            l = [item[-2] for item in vals]
            l = sum([float(i) for i in l])
        else:
            l = [item[-1] for item in vals]
            l = sum([float(i) for i in l])
        print('Average '+ cost_rating +' of Hotel in ' + state + ' is ' + str(l / len(vals)))



    if operation == 'highest':
        highest(cos_rat)
    elif operation == 'cheapest':
        cheapest(cos_rat)
    else:
        average(cos_rat)
    return file.close()



st = ['India', 'Maharashtra', 'Karnataka', 'Tamilnadu']
ct = ['cost', 'rating']
op = ['cheapest', 'highest', 'average']

state = input('Enter State : ')
if state not in st:
    print(state+' is not registered\nRegistered states are :\n'
                '1.Maharashtra.\n2.Karnataka\n3.Tamilnadu\n'
                '4.India(To see about all above state details)')
    quit()
cost_rating = input('Enter cost/rating : ')
if cost_rating not in ct:
    print('Invalid Choice, It should be either cost or rating')
    quit()
operation = input('Enter Operation : ')
if operation not in op:
    print('Invalid operation\nOperation choices :\n'
            '1. highest\n2. cheapest\n3. average')
    quit()

search(state, cost_rating, operation)
