import csv

dictionary = { 1: 31, 2:28, 3:31,4:30 ,5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}    
   
while True:
    
    try:
        user_inputYYYY = int(input ( " Please enter the year of the survey in the format YYYY : "))
        
        if 2002 <= user_inputYYYY <= 2024:                
                print()
                print("leap year")
                year = user_inputYYYY
                break               
        
        else:
            print()
            print("Out of range")
                
    except ValueError:
             
            print("Invalid input! Please enter an integer.")
            
while True:

    try:
        
        user_inputMM = int(input ( " Please enter the month of the survey in the format MM : "))
            
        if 1 <= user_inputMM <= 12:
            
            print()
            print("month")
            month = user_inputMM
            break
            
        else:
            print()
            print("Out of range")
                
    except ValueError:
             
        print("Invalid input! Please enter an integer.")
        
while True:    
    try:
        user_inputDD = int(input ( " Please enter the day of the survey in the format DD : "))
        
        if (user_inputYYYY % 4 == 0 and user_inputYYYY % 100 != 0) or (user_inputYYYY % 400 == 0):
                dictionary.update({2:29})
                
        if 1 <= user_inputDD <= dictionary[user_inputMM]:
            print()
            print("baba yaga")
            date = user_inputDD
            break
        else:
            print()
            print("Out of range")
                    
    except ValueError:
            print("Invalid input! Please enter an integer.")


x = str(date),"0"+str(month),str(year)

corresponding_date = ''.join(x)

print(corresponding_date)


