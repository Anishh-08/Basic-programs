#Split the given email into two parts, one before the @ symbol and one after the @ symbol 

email=input('Enter your email: ')

split=email.index('@')

k=email[:5:2]
t=email[5::2]

print(f'Your username is {k} and Domain is {t} ')
 