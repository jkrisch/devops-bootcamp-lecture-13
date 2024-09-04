threshold =  int(input("Please define a threshold:"))
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
if bool(threshold):
    new_list = [entry for entry in my_list if entry >= threshold]
    print(new_list)

else:
    print("No threshold defined. Cancelling process.")
