fibonacci = [1, 1]
months = int(input("for how long should the rabbits breed? "))
k_pairs = int(input("how many baby pairs does an adult pair produce? "))

for i in range(months-2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2]*k_pairs)

print(fibonacci)
print(fibonacci[-1])
