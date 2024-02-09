import random
from table import Table  #table class is defined in table.py
import pandas as pd

df=pd.read_csv('new_colleagues.csv')
# prints the first five elements of the table
print(df.head())
# converts each element into the list
data_list=df.values.tolist()
# merge all the elements into one single list
Name_list = [item for sublist in data_list for item in sublist]
print(Name_list)
class Openspace:
    def __init__(self, number_of_tables,capacity):
        # initialise openspace with the number of tables and capacity per table
        self.number_of_tables = number_of_tables
        # creates a new table with specified capcity
        self.tables = [Table(capacity) for _ in range(number_of_tables)]

    
     # method to organize the seating arrangement
    def organize(self, names):
     # shuffle the list of names
     random.shuffle(names)
     all_seats = [(i, j) for i in range(len(self.tables)) for j in range(len(self.tables[0].seats))]
     random.shuffle(all_seats)
     # iterate through each table and seat and assign names
     for (table_index, seat_index) in all_seats:
        if not names:
            break
        table = self.tables[table_index]
        seat = table.seats[seat_index]
        seat.set_occupant(names.pop(0))

    def display(self):
        # iterate through each table and seat,printing occupants
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                occupant = seat.occupant if not seat.free else "Empty"
                print(f"Seat {j}: {occupant}")
            print()
    # method to store the seating arrangement in an excel file
    def store(self, filename):
        # Create a list to store table data
        table_data = []
        # iterate through each table and seat, collecting data
        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                if Name_list:
                  occupant = Name_list.pop(0)
                else:
                  occupant = "Empty"
                # append table,seat and occupant information to the list
                table_data.append({"Table": i, "Seat": f"Seat {j}", "Occupant": occupant if seat.occupant else "Empty"})
            
        
        
        # Create a DataFrame from the table data
        df = pd.DataFrame(table_data)
        
        # Write the DataFrame to an Excel file
        df.to_excel(filename + '.xlsx', index=False)

# Example
if __name__ == "__main__":
    # Names of people to be assigned to seats
    names = Name_list
    # Create an Openspace with 6 tables
    openspace = Openspace(6,4)

    # Organize the names into the Openspace
    openspace.organize(names)

    # Display the assigned seats
    openspace.display()

    # Store the seat assignment in an Excel file
    openspace.store("new_colleagues.xlsx")
