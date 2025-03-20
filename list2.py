fruits = ["apple", "banana", "cherry", "date"]
# Adding items to a list
fruits.append("elderberry")  # Add to the end
fruits.insert(2, "fig")  # Insert at index 2
print("List after adding:", fruits)
# Removing items
fruits.remove("cherry")  # Remove by value
popped_fruit = fruits.pop()  # Removes the last item
print("List after removal:", fruits)
print("Popped fruit:", popped_fruit)
# Checking for an element
print("Is 'apple' in the list?", "apple" in fruits)