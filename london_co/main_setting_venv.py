import london_co

def mission_one_one():
    device_name = input("Введите имя устройства:\n")
    
    for key, value in london_co.london_co.items():
        
        if device_name == key:
            print(london_co.london_co[key])
            
        elif device_name != key:
            print("Нет такого устройства")
            continue
        
        elif device_name == 'r':
            user_input
    
    
def mession_one_two():
    device_name = input("Введите имя устройства:\n")
    
    for keys, values in london_co.london_co.items():
        
        if device_name == keys:
            param_input = input("Введите параметр;\n")
            
            for key, value in london_co.london_co[keys].items():
                
                if param_input == key:
                    print(london_co.london_co[keys][key])
                    quit()
                    
    else:
        print("Нет такого устройства")

def mission_one_free():
    device_name = input("Введите имя устройства:\n")
    
    for keys, values in london_co.london_co.items():
        
        if device_name == keys:
            param_input = input(f"Введите параметр {london_co.london_co[keys]}:\n")

            for key, value in london_co.london_co[keys].items():
                
                if param_input == key:
                    print(london_co.london_co[keys][key])
                    quit()
                    
            else:
                print("Такого параметра нет")
                

if __name__ == "__main__":
    user_input = input("Выбери задание по какому пойдём:\n>>Задание 1:\n>>Задание 2:\n>>Задание 3:\n>>Exit выход\n")
    
    if user_input is '1':
        mission_one_one()
    elif user_input == '2':
        mession_one_two()
    elif user_input == '3':
        mission_one_free()
    elif user_input == 'Exit':
        quit()
    else:
        print("К сажалению нет такого выбора")
        quit()
        