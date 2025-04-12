def get_cats_info(path):
    try:
        cat_data = []
    
        with open(path, "r", encoding = "utf-8") as info:
            for line in info:
                id, name, age = line.strip().split(",")
                cat_data.append({'id': id, 'name': name, 'age': age})
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f'{e} with file')
    return cat_data
    

    
cat_data = get_cats_info("D:/homework_4/info_cats.txt")
print(cat_data)


