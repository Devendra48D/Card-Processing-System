import sys

#if input is in the form : python cardps.py testfile.txt 
if len(sys.argv) == 2:
	filename = sys.argv[1]

#if input is in the form: python cardps.py \< testfile.txt  (on bash)
#or f the input is : python cardps.py < testfile.txt
if len(sys.argv) == 3:
	filename = sys.argv[2]

#Opening input file under read only mode
f = open(filename, 'r')

#credit card database with all users info 
database = {}

#Luhn10 check function for credit card numbers
def validcard(cardnum):
    cardnum  = int(cardnum)
    r = [int(i) for i in str(cardnum)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(j*2, 10)) for j in r[1::2])) % 10 == 0 


while True:
    #read in each line
    command = f.readline()
    if len(command) == 0:
    	break
    command_array = command.strip().split(' ')
    #if the command is add, add card to the database if card number is valid
    if command_array[0] == 'Add':
	name = command_array[1]
	limit = command_array[3]
	card_number = command_array[2]
	if validcard(card_number):
            #create card if the card number is validated with Luhn 10
    	    database[name] = {'valid':True, 'balance':0, 'limit':int(limit[1::])}
	else:
	    database[name] = {'valid':False}
    #if command is charge,if the card number is valid and if the balance is less than the given limit
    #increase balance with the given amount
    elif command_array[0] == 'Charge':
	name = command_array[1]
	amount = int((command_array[2])[1::])
	if name in database and (database[name])['valid']:
	    bal = (database[name])['balance']
	    if bal+amount <= (database[name])['limit']:
		(database[name])['balance'] += amount
    #if command is credit and if the card is valid, decrease balance with the given amount
    elif command_array[0] == 'Credit':
	name = command_array[1]
	amount = int((command_array[2])[1::])
	if name in database and (database[name])['valid']:
	    bal = (database[name])['balance']
	    (database[name])['balance'] -= amount

#sort the names in ascending order
names = sorted(database.keys())
for person in names:
    #if card is valid, print name and balance
    if (database[person])['valid']:
	print person+': $'+str((database[person])['balance'])
    #if card is invalid, print name and error
    else:
	print person+': error'
    
