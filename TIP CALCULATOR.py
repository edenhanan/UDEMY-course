print('Welcome to the tip calculator')
Bill_total = int(input('what was the total bill? '))
NUM_pepole = int(input('How many people split the bill? '))
Perc_Tip = int(input('what percentage tip would you like to give? 10, 12, or 15? '))
Perc_Tip = Perc_Tip / 100 + 1
Bill_person = round( Bill_total * Perc_Tip / NUM_pepole, 2)
print(Bill_person)
