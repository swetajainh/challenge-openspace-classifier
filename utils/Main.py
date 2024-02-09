import random
from table import Table  
import pandas as pd
from openspace import Openspace

df=pd.read_csv('new_colleagues.csv')
# prints the first five elements of the table
print(df.head())
# converts each element into the list
data_list=df.values.tolist()
# merge all the elements into one single list
Name_list = [item for sublist in data_list for item in sublist]
print(Name_list)



# Create a DataFrame from the table data
df = pd.DataFrame(table_data)
        
        # Write the DataFrame to an Excel file
df.to_excel(filename + '.xlsx', index=False)

# Example
if __name__ == "__main__":
    # Names of people to be assigned to seats
    names = Name_list
    # Create an Openspace with 6 tables
    openspace = Openspace(4,6)

    # Organize the names into the Openspace
    openspace.organize(names)

    # Display the assigned seats
    openspace.display()