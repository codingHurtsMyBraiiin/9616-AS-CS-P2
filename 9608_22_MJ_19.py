#QUESTION-6

#create two .txt files to store stuff 

def get_info():
    pref_name = input("Enter your preferred name: ")

    id_status = False
    while id_status == False:
        id = input("ID: ")
        if len(id) == 5:
            if "A" <= id[0] <= "Z":
                count = 0
                for i in range(1, 5):
                    if int(id[i]) >= 0 and int(id[i]) <= 9:
                        count += 1
                        if count == 4:
                            id_status = True

    return f"{pref_name}*{id}"  

def write_info(file_choice, info):
    if file_choice == 1:
        with open(r"File1.txt", "a") as f:            
            f.write(info + "\n")
    else:
        with open(r"File2.txt", "a") as f:c
            f.write(info + "\n")

def top_level():
    info = get_info()
    if info.split("*")[1][0] >= "A" and info.split("*")[1][0] <= "M":
        file_choice = 1
        write_info(file_choice, info)
    else:
        file_choice = 0
        write_info(file_choice, info)

top_level()
