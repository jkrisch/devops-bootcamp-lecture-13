employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

#update the job
employee["job"] = "Software Engineer"

#remove age key
del employee["age"]

#loop through the dict and print key value pairs

for key in employee.keys():
    print(f"{key}:{employee[key]}")


dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}


#merge dict into 1 new

dict_new = dict_one|dict_two

print(f"Sum of merged dicts: {sum(dict_new.values())}")

print(f"Max value in merged dict: {max(dict_new.values())}")
print(f"Min value in merged dict: {min(dict_new.values())}")
