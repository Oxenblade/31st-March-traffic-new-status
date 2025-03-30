import csv

filename = "traffic_data16062024.csv"

with open (filename, "r" ) as traffic:
    
    csv_reader = csv.reader(traffic)
    
    headerline = next(traffic)
    My_list = []
    My_second_list =[]
    New_list=[]
    Vehicles=[]
    My_third_list=[]
    My_fouth_list=[]

    Total_Time_list=[]
    rain_list=[]
    
    for i in csv_reader:
        My_list.append(i[8])
        My_second_list.append(i[9])
        
        if ( i[0] == "Elm Avenue/Rabbit Road" and i[4] == "N"):
            New_list.append(i[8])
        if  i[6]< i[7]:
            Vehicles.append(i[8])
        if i[0] == "Elm Avenue/Rabbit Road":
            My_third_list.append(i[8])
        if i[0] == "Hanley Highway/Westway":
            My_fouth_list.append(i[8])

        if i[0] == "Hanley Highway/Westway":
            Total_Time_list.append(i[2][0:2])
            
        if i[5] == "Heavy Rain":
            rain_list.append(i[2][3:5])    
        if i[5] == "Light Rain":
            rain_list.append(i[2][3:5])


    Total_Vehicle_list = [ Total_Time_list.count("0:"),
            Total_Time_list.count("00"),            
            Total_Time_list.count("01"),
            Total_Time_list.count("02"),
            Total_Time_list.count("03"),
            Total_Time_list.count("04"),
            Total_Time_list.count("05"),
            Total_Time_list.count("06"),
            Total_Time_list.count("07"),
            Total_Time_list.count("08"),
            Total_Time_list.count("09"),
            Total_Time_list.count("10"),
            Total_Time_list.count("11"),
            Total_Time_list.count("12"),
            Total_Time_list.count("13"),
            Total_Time_list.count("14"),
            Total_Time_list.count("15"),
            Total_Time_list.count("16"),
            Total_Time_list.count("17"),
            Total_Time_list.count("18"),
            Total_Time_list.count("19"),
            Total_Time_list.count("20"),
            Total_Time_list.count("21"),
            Total_Time_list.count("22"),
            Total_Time_list.count("23"),
            Total_Time_list.count("24")]


    
            
    two_wheel_vechicles = My_list.count("Bicycle"), My_list.count ("Motorcycle"), My_list.count("Scooter")
    
    number =  My_list.count("Truck")/ len(My_list)
    Percentage = "{:.0%}".format(number)
    average_number = My_list.count("Bicycle")/ 24
    percentage_of_scooters = My_third_list.count("Scooter")/ len(My_third_list)
    percentage_value_of_scooters = "{:.0%}".format(percentage_of_scooters)

    intinger_convertion = list(map(int,rain_list))

    k = 60

    b = [ k - x for x in intinger_convertion]

    result = ' '.join(b)

    #rain_hour_calculation = 


















    
print(len(My_list))
print(My_second_list.count("TRUE"))
print(My_list.count("Truck"))
print(sum(two_wheel_vechicles))

print(New_list.count("Buss"))

print(Percentage)
print(round(average_number))
print(len(Vehicles))
print(len(My_third_list))
print(len(My_fouth_list))
print(percentage_value_of_scooters)

print(max(Total_Vehicle_list))

print(result)














''''import csv

filename = "traffic_data15062024.csv"

with open (filename, "r" ) as traffic:
    csv_reader = csv.reader(traffic)

    header = next(csv_reader)
    print("header:", header)
    My_list=[]


    for row in csv_reader:
        #row = row.rstrip()
        #row = row.replace('',"")
        #row = row.split(',')
        My_list.append(row[8])
        
        #print("row:",row[8])
print(My_list.count("Truck"))
        #print(row[8].count("Truck"))




import csv


filename = "traffic_data15062024.csv"

with open(filename, "r") as traffic:
    csv_reader = csv.reader(traffic)

    header = next(csv_reader)


    My_list = []
    truck_count = 0

    for i in csv_reader:
        if len(i) > 8: 
            My_list.append(i[8])
            if i[8].strip() == "Truck":
                truck_count += 1

    print("Total count of 'Truck':", truck_count)

    My_second_list = []
    electric_vechiles = 0

    for row in csv_reader:
        if len(row)> 8:
            My_second_list.append(row[8])

            if row[9].strip()== True:
                electric_vechiles += 1
    print("Total count of Electrical Vechiles:", electric_vechiles)

    My_third_list = []
    two_wheel_vechicles = 0

    for row in csv_reader:
        if len(row)> 8:
            My_third_list.append(row[8])

            if row[8].strip()== "Bicycle":
                two_wheel_vechicles += 1
    print("Total count of two wheel vechicles:", two_wheel_vechicles)'''


    
