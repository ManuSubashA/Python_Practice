import csv

class ReadAndWriteData:

    def __init__(self, filename):
        self.filename = filename

    def fetch_data(self):
        try: 
            with open(self.filename, mode="r", newline='') as file:
                reader = csv.DictReader(file)
                print("Fetching data from CSV:")
                for row in reader:
                    print(f"Name: {row['Name']}, SkillSet: {row['SkillSet']}, Experience: {row['Experience']}")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as e:
                    print(f"An error occurred: {e}")
                
reader = ReadAndWriteData('csvdata.csv')
reader.fetch_data()