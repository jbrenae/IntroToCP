# Sentinel Value Example

salary = 0
total = 0
count = 0

while(salary >= 0):
    salary = int(input("Please enter salary (-1 to stop): "))
    if (salary > 0):
        total += salary
        count += 1

    print("Average salary =",total / count)