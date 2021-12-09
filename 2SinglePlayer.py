import random
options = ["roe","sham","boe"]
pc = random.choice(options)
print('EKANSH JAIN A2305218211 7CSE-4X')
while True:
    user = input("\nPick either roe, sham or boe: ")
    print('PC chose: ', pc)
    print('User chose: ', user)
    if user == 'roe':
        if pc == 'roe':
            print('Tie Game')
        elif pc == 'sham':
            print('PC Wins')
        else:
            print ('User Wins')
    if user == 'sham':
        if pc == 'roe':
            print ('User Wins')
        elif pc == 'sham':
            print ('Tie Game')
        else:
            print ('PC Wins')
    if user == 'boe':
        if pc == 'roe':
            print ('PC Wins')
        elif pc == 'sham':
            print ('User Wins')
        else:
            print ('Tie Game')
    if input('\nDo You Want To Continue? ') not in ['y','Y']:
        break
