# find the second maximum and second minimum from the list
salary = [67000, 45000, 78000, 55000, 28000,44000,33000]

half = len(salary)//2
second_half = salary[half:]
print("Second half:", second_half)

print("Max:", max(second_half))
print("Min:", min(second_half))

