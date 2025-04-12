def total_salary(path):
    try:
        total = 0
        average = 0
        line_count = 0
        with open(path, "r", encoding = "utf-8") as pay:
            for line in pay:
                name, salary = line.strip().split(",")
                total += int(salary)
                line_count += 1
            if line_count > 0:
                average = total // line_count
            else:
                average = 0
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f'{e} with file')
    return total, average
total, average = total_salary("D:\\homework_4\\salary.txt")
print (f"Total salary: {total}, Average salary: {average}")