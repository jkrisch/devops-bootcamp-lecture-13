def youngest_employee(employees):
    min_age = 120
    for employee in employees:
        if employee["age"] <= min_age:
            min_age = employee["age"]
            index = employees.index(employee)
    print("The youngest co-worker is:")
    print(f"name: {employees[index]['name']}")
    print(f"age: {employees[index]['age']}")


def amount_upper_and_lower_case(sample_string):
    amount_upper = 0
    amount_lower = 0
    if isinstance(sample_string, str):
      for character in sample_string:
        if character.isupper():
          amount_upper += 1
        if character.islower():
          amount_lower += 1
      print(f"Amount of upper case letters: {amount_upper}")
      print(f"Amount of lower case letters: {amount_lower}")
    else:
      print("Please prove a string")


def get_even_numbers(list_of_numbers):
  even_numbers = []
  if(isinstance(list_of_numbers,list)):
    for entry in list_of_numbers:
      try:
        if entry % 2 == 0:
            even_numbers.append(entry)
      except ValueError:
          print(f"entry is not a number")
    print("The even numbers in the provided list are")
    print(even_numbers)
  else:
    print("you did not provide a list")