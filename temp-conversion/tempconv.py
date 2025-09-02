temp_input=str(input("Which scale do you want to enter the temperature in (only celcius): "))
temp=float(input('Enter temperature: '))
if temp_input == 'Celcius':
    conv=str(input('Which scale do you want to convert into: '))
    if conv == 'Kelvin':
        C_K= temp + 273
        print(f'In terms of kelvin: {C_K}')
    if conv == 'Farenheit':
        C_F= (temp*1.8)+32
        print(f'In terms of Farenheit: {C_F}')
    


