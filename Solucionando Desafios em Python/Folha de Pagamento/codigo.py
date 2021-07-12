emp_no = int(input())

worked_hours = int(input())

receives_per_worked_hour = float(input())

salary = worked_hours*receives_per_worked_hour

print("NUMBER =",emp_no,end="\n")
print("SALARY = U$ %0.2f"%salary,end="\n")