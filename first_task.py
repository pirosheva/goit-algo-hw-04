def total_salary(path):
    inform_emp={}
    num_workers = 0
    total = 0
    average = 0
    with open(path, "r") as emp_file:
        while True:
            line = emp_file.readline().strip()
            if not line:
                break
            line = line.split(",")
            num_workers += 1
            total += int(line[1])
    average = int(total/num_workers)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

print(total_salary("test_1.txt"))
