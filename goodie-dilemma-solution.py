"""
The Given Program is classified into 3 parts
1. Gathered the data from input_file.txt and store it in a relevant data_structure(using a list to store all data).
2. The calculation part to calculate the difference between the highest and lowest prices for different goodies.
3. write the appropriate data in the output_file.txt.
"""

input_file = "input_file.txt"
output =[]
def get_goodies_form_input_file(file_name): #fetch the data stored in input file and the parameter is "filename"
    with open(file_name) as file:
        file.readline()
        header = file.readlines()
    data = [x.strip() for x in header]
    return data

def calculation(data): #The calculation part to calculate the difference between the highest and lowest prices for different goodies.
    for d in data:
        price = d.split(':')
        output.append(price[1].replace(" ",""))

    int_higest_lowest = list(map(int, output))
    max_value = max(int_higest_lowest)
    min_value = min(int_higest_lowest)
    return int(max_value) - int(min_value)

def write_output_data(data_list,number_of_emp): #writing the output data in the specific file, parameter is inputfile data, number of Employee.
    with open("output_file.txt",'+w') as file:
        file.write("Number of the employees: {}\n\n".format(number_of_emp))
        file.write("Here the goodies that are selected for distribution are:\n")
        for d in data:
            file.write("{}\n".format(d))
        difference = calculation(data_list)
        file.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}".format(difference))



if __name__ == "__main__":
    print("====" * 30)
    print("Execution is Started")
    num_of_emp = 2   #Need to provide Number of Employees.
    print("Number of the employees:",num_of_emp)
    input_file_data = get_goodies_form_input_file(input_file)
    import random
    data = random.sample(input_file_data, num_of_emp)
    write_output_data(data,num_of_emp)
    print("Execution is completed. \nThe output present in the current working directory and the filename is 'output_file.txt' ")
    print("===="*30)

