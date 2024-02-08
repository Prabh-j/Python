x = input('give any number: ')
match x:
    case 'a':
        print('its 0')
    case 1:
        print('its 1') #to get result, use typecasyting
    case '2':
        print('its 2') #to avoid typecasting
    case 3:
        print('its 3')
    case 4:
        print('its 4')
    case 5:
        print('its 5')
    case 6:
        print('its 6')
    case 7:
        print('its 7')
    case _ if x== 50:
        print('we can also put conditionals')
    case _:
        print('its for default value') #default value make remainig code unreachable because it offer result for everything that is not mentioned above so to bypass it put a conditional
    # case _:
    #     print('there can be multiple default values')
    # case _ if x== 50:
    #     print('we can also put conditionals')