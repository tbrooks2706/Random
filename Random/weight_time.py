import csv
from datetime import date, datetime, time

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Random\weight_time2.csv") as new_csv:
    csv_obj = csv.DictReader(new_csv)
    line_count = 0
    new_dict = {}
    for row in csv_obj:
        new_dict[line_count] = row
        line_count += 1

#print(new_dict[0].values())
set1 = list(new_dict[0].values())
print(set1)
def clean_data(dictionary):
    for key, value in dictionary.items():
        #print(value)
        for key, value in value.items():
            if key == "weight":
                value = int(value)
            elif key == "time":
                newval = datetime.strptime(value, "%H:%M:%S").time()
                value = newval
            elif key == "date":
                newval = datetime.strptime(value, "%d/%m/%Y").date()
                value = newval
                #print(value.day())
            else:
                value = value
            #print(type(value))
    #print(dictionary)
clean_data(new_dict)

class RunningTime:
    def __init__(self, time, date, weight):
        self.time = time
        self.date = date
        self.weight = weight

#running_time_1 = RunningTime(new_dict)

#tested and class initialisation works
# time1 = RunningTime("00:29:21", "28/11/2022", "113.7")
# print(time1.time)

#format data so time is time, date is date, weight is int
#DONE

#create time items as objects of RunningTime class (as per time1 above)
#CAN'T DO THIS - ABANDONING OOP - can't figure out a way to create a new variable of this class, for each iteration in the dictionary

#create function for time per weight inside class

#do some kind of print as part of a sentence "At DATE, your time was X per kg"

#write the sentences to a txt file and export it?

#write the time per weight as a new column inside the original CSV?

#x = date(2020, 5, 8)
#y = x.replace(year=2009, day=9)
#z = x.month
#print(z)
#print(type(y))