# Pizza Calculator
# Assumptions: 1 pizza = 8 slices, family size = 4

person1 = int(input("Enter slices for person 1: "))
person2 = int(input("Enter slices for person 2: "))
person3 = int(input("Enter slices for person 3: "))
person4 = int(input("Enter slices for person 4: "))

total_slices = person1 + person2 + person3 + person4

pizzas_needed = total_slices // 8
leftover_slices = total_slices % 8

if leftover_slices > 0:
    pizzas_needed = pizzas_needed + 1
    leftover_slices = (pizzas_needed * 8) - total_slices

print("\n--- Pizza Order Summary ---")
print("Total slices eaten:", total_slices)
print("Total pizzas needed:", pizzas_needed)
print("Leftover slices after everyone eats:", leftover_slices)
