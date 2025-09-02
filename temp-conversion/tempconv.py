temp_input=float(input("Which scale do you want to enter the temperature in (only celcius): "))

if temp_input == 'Celcius':
    conv=float(input('Which scale do you want to convert into: '))
    if conv == 'Kelvin':
        C_K= temp_input + 273
        print('In terms of kelvin: {C_K}')
    if conv == 'Farenheit':
        C_F= (temp_input*1.8)+32
        print(f'In terms of Farenheit: {C_F}')
    


