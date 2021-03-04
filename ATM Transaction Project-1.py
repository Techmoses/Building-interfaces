"""
This program display ATM Transactions.
"""
import random


def welcome_screen():
    print('\nWELCOME')
    print('\nPLEASE INSERT YOUR CARD')
    
    # Ask the user to enter their pin
    flag = True
    while flag:
        pin = int(input('\nENTER YOUR 4 DIGIT PIN: '))
        if (pin < 1000 or pin > 9999):
            print('Invalid pin, try again')
        else:
            flag = False   
    
# Display the menu
def menu():
    # List of available options 
    print('\nPlease select an option')
    print('\t1. Withdrawal')
    print('\t2. Check Balance')
    print('\t3. Transfer')
    print('\t4. Quit')
    
    # Ensure that the user does not input a value different from the required input
    flag = True
    while flag:
        # Take input from the user
        option = int(input('Option: '))
    
        if option > 4:
            print('\nWrong input, try again')
        else:
            flag = False
    return option

# Set the type of account i.e savings or current
def account_type():
    # List of available options 
    print('\nSelect account type')
    print('\t1. Savings')
    print('\t2. Current')
    
    flag = True
    while flag:
        # Take input from the user
        acct_type = int(input('Option: '))
        # Ensure that the user does not input a value different from the required input
        if acct_type > 2:
            print('\nWrong input, try again')
        else:
            flag = False
    return acct_type

def balance_amount():
    bal = random.randint(500, 300000000)
    print('\nTransaction in progress...')
    print('Your balance is', float(bal))
    return bal

# Set the withdrawal amount
def withdrawal():
    
    # Show available options
    print('\nSelect amount to withdraw in Naira')
    print('\t1. 1000')
    print('\t2. 2000')
    print('\t3. 3000')
    print('\t4. 4000')
    print('\t5. Other Amount')
    

    flag = True
    while flag:
        # Take input from the user
        with_option = int(input('Enter option: '))
        
        # Ensure that the user enters a value not greater than values from the options
        if (with_option > 5):
            print('\nWrong input, try again')
        else:
            if (with_option == 5): 
                # If user selects other amount, ensure that it is not more than 20000
                # 20000 is the maximum withdrawal limit
                
                flag_1 = True
                while flag_1:
                    other_amount = int(input('\nEnter amount in multiples of 1000: '))
                    if (other_amount < 1000 or other_amount > 20000 or other_amount % 1000 != 0) :
                        print("'1000' is the minimum withdrawal limit while '20000' is the maximum withdrawal limit, try again")
                    else:
                        flag_1 = False
            print('Transaction in progress...')
            flag = False
    return with_option

# Set the recipient bank
def recipient_bank_name():
    print ('\nSelect recipient bank')
    print('\t1. Guaranty Trust Bank(GTB')
    print('\t2. Access Bank')
    print('\t3. First Bank')
    print('\t4. Union Bank')
    print('\t5. Diamond Bank')
    
    flag = True
    while flag:
        # Take input from the user
        rec_bank = int(input("\nEnter Recipient's Bank: "))
        if (rec_bank > 5):
            print('Wrong input, try again')
        else:
            flag = False
    return rec_bank

# Display recipient account type
def recipient_account_type():
    
    # List of available options 
    print("\nSelect Recipient's Bank Account Type")
    print('\t1. Savings')
    print('\t2. Current')
    
    flag = True
    while flag:
        # Take input from the user
        rec_acct_type = int(input('Option: '))
        
        # Ensure that the user does not input a value different from the required input
        if rec_acct_type > 2:
            print('\nWrong input, try again')
        else:
            flag = False
    return rec_acct_type
    
# Display recipient account number
def recipient_account_number():
    rec_acct_num = int(input("\nEnter recipients's account number: "))
    
# Display send money preference
def send_money():
    # Ask the user to enter amount to be sent
    print('\nEnter amount to be sent in Naira')
    print('\t1. 1000')
    print('\t2. 2000')
    print('\t3. 3000')
    print('\t4. 4000')
    print('\t5. Other Amount')
    
    flag = True
    while flag:
        # Take input from the user
        send_amount = int(input('Enter amount to be sent: '))
        
        # Ensure that the user enters a value not greater than values from the options
        if (send_amount > 5):
            print('\nWrong input, try again')
        else:
            if (with_option == 5): 
                # If user selects other amount, ensure that it is not more than 20000
                # 20000 is the maximum withdrawal limit
                
                flag_1 = True
                while flag_1:
                    other_amount = int(input('Enter amount in multiples of 1000'))
                    if (other_amount > 20000):
                        print('20000 is the maximum withdrawal limit, Try again')
                    else:
                        flag_1 = False
            flag = False

def show_transaction():
    welcome_screen()
    m = menu()  
    if (m == 1): # Withdrawal
        acc_type = account_type()
        withdrawal_amount = withdrawal()
        print('Please take your cash.')
        
    elif (m == 2): # Balance check
        balance = balance_amount()
        
    elif (m == 3): # Transfer
        recipient_bank = recipient_bank_name()
        rec_acc = recipient_account_type()
        rec_acct_number = recipient_account_number()
        print ('Transaction in progress...')
    
    elif (m == 4): # No transaction
        print('\nThank You For Banking With Us.')
        print('Merry Christmas and Happy New Year in Advance.')
        print('Have a Nice Day!')
        
def main():
    show_transaction()
    
    # Ask if the user will perform another transaction
    flag = True
    while flag:
        new_transaction = str(input('\nDo you want to perform another transaction? (Yes/No)\n'))
        if (new_transaction == 'Yes' or new_transaction == 'yes'):
            show_transaction()
        else:
            print('\nThank You For Banking With Us.')
            print('Merry Christmas and Happy New Year in Advance.')
            print('Have a Nice Day!')
            break 
           
# Display Transaction
main()