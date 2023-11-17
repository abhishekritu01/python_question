
string ='amaama'
half =int( len(string)/2)

first_half = string[:half]
second_half = string[half:]

if first_half == second_half:
    print('palindrome')
else:
    print('not palindrome')

if first_half == second_half[::-1]:
    print('symetrical')
else:
    print('not symetrical')

