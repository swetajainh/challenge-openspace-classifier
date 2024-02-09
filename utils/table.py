# create a class seat with attributes free and occupant
class Seat:    
#create a constructor 
    def __init__(self):
        # iniialising the seat as free with no occupant
        self.free=True
        self.occupant=None
# define method to assign seat if its free
    def set_occupant(self,name):
            if self.free:
                # setting the occcupant and marking the seat as occupied
                self.occupant=name
                self.free=False
                return f"{name} has been assigned to seat"
            else:
                return "seats is occupied"
# remove a person from the seat and return its name
    def remove_occupant(self,name=None):
         if not self.free:
              # removing the occupant and marking the seat as free
              occupant_name=self.occupant
              self.occupant=None
              self.free=True
              return f"{occupant_name} has been removed"
         else:
              return "seat is empty"
        
                



# create a class table
class Table:
     def __init__(self,capacity):
          # initialising the table with a specified capacity and creating seats
          self.capacity=capacity
          self.seats=[Seat() for _ in range(capacity)]
    # Method to check if free spot is available
     def has_free_spot(self):
          return any(seat.free for seat in self.seats)
     
     # Method to assign a person to the seat at a table
     def assign_seat(self,name):
          for seat in self.seats:
                if seat.free:
                     # Assigning the person to the first available seat
                     seat.set_occupant(name)
                     return f"{name} has been assigned a seat"
          return "no available seats at this table"
     # Method to calculate the number of empty seats at the table
     def left_capacity(self):
           return sum(seat.free for seat in self.seats)
# creating an instance of the class Table
table = Table(4)
print(table.has_free_spot())
# Assigning occupants to the seat and removing them

print(table.assign_seat('Andrea'))
print(table.assign_seat("Sweta"))
print(table.assign_seat("Afaf"))
print(table.seats[1].remove_occupant())
print(table.seats[1].remove_occupant())
print(table.seats[2].remove_occupant())          

          
      

        



        
