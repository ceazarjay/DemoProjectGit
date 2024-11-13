# Code to open and read a CSV file
import csv

def read_cars_file():
    # Open the cars.csv file for reading
    with open('cars.csv', mode='r') as document:
        csv_reader = csv.reader(document)
        next(csv_reader)  # Skip the header row
        
        # Read and print each row in the CSV
        for row in csv_reader:
            print(row)

# Run the function to read the file
read_cars_file()
