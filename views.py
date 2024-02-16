import csv

def add(data):
    try:
        with open('data.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except IOError as e:
        print("Error occurred while adding data:", e)

def view():
    data = []
    try:
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except IOError as e:
        print("Error occurred while reading data:", e)
    return data

def remove(telephone):
    try:
        new_data = []
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                if telephone not in row:
                    new_data.append(row)
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
    except IOError as e:
        print("Error occurred while removing data:", e)

def remove_all(data):
    try:
        with open('data.csv', 'w', newline='') as file:
            pass  # Empty the file
    except IOError as e:
        print("Error occurred while removing all data:", e)

# Update function
def update(new_data):
    try:
        old_data = view()
        updated = False
        for i, row in enumerate(old_data):
            if row[2] == new_data[2]:  # Assuming telephone number is at index 2
                old_data[i] = new_data
                updated = True
        if updated:
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(old_data)
            return True
        else:
            return False
    except IOError as e:
        print("Error occurred while updating data:", e)
        return False



def search(telephone):
    data = []
    try:
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                if telephone in row:
                    data.append(row)
    except IOError as e:
        print("Error occurred while searching data:", e)
    return data
