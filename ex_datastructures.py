# --- List ---
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "blueberry"
sliced_fruits = fruits[1:]
print("List:", fruits)
print("Sliced List:", sliced_fruits, "\n")

# --- Tuple ---
coordinates = (10, 20)
print("Tuple:", coordinates)
print()

# --- Set ---
colors = {"red", "blue", "green"}
colors.add("yellow")
colors.update(["red", "purple"])
print("Set:", colors)
print()

# --- Dictionary ---
student = {"name": "Alice", "age": 20}
student["major"] = "CS"
print("Dictionary:", student)
for key, value in student.items():
    print(f"{key} -> {value}")
print()

# --- String ---
message = "Hello, world!"
print("String:", message)
print("Sliced String:", message[:5], "\n")

# --- List Comprehension ---
squares = [x**2 for x in range(1, 6)]
print("List Comprehension (Squares):", squares)

# --- Set Operations ---
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
intersection = set1.intersection(set2)
print("Union:", union)
print("Intersection:", intersection)
