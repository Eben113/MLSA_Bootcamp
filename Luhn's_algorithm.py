def validate_card_no(number):
    reversed = str(number)[-1:0:-1] + str(number)[0]
    sum = 0
    for digit in str(reversed):
        digit = int(digit)*2
        if digit > 9:
            digit -= 9
        sum += int(digit)
        if sum%10 == 0:
            return('card is valid')
        else:
            return('invalid card')
number = input('type your card number here: ')
print(validate_card_no(number))