import csv
import matplotlib.pyplot as plt

def read_csv_column(file_path, column_name):
    column_values = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            column_values.append(row[column_name])

    return column_values

if __name__ == "__main__":
    file_path = "C:/Users/Brenda/Desktop/matplotlib/data.csv"
    column_name = "World Population Percentage" 

    column_values = read_csv_column(file_path, column_name)
    print(column_values)



    

plt.pie(range(len(column_values)), column_values)
plt.show()