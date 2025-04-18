def main():

    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Length of the fruit list:", len(fruit_list))
    
    fruit_list.append('mango')
    
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    if index >= 0 and index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if index >= 0 and index < len(lst):
        lst[index] = new_value
        return "Value updated successfully."
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice range."
    return lst[start:end]

def index_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, index, new_val))
            print("Updated list:", my_list)
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
main()

index_game()
