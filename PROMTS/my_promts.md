
# search max value by ternary operator python
# finding the largest of three numbers using pattern mathcing

def max_of_three(a, b, c):
    match a, b, c:
        case x, y, z if x >= y and x >= z:
            return x
        case x, y, z if y >= x and y >= z:
            return y
        case x, y, z:
            return z

# Example usage
print(max_of_three(10, 25, 8))  # Output: 25
print(max_of_three(100, 50, 75))  # Output: 100
print(max_of_three(7, 7, 7))  # Output: 7

# using unitest


# Пример 1. Создай программу для генерации случайных чисел

`create a program to generate random numbers`


## Результат

```python
import random

random_int = random.randint(1, 10)
print("Random integer:", random_int)

random_float = random.random()
print("Random float:", random_float)

# Generate a random floating-point number between 10 and 20
random_range = random.uniform(10, 20)
print("Random float in range:", random_range)

# Generate a random element from a list
my_list = ["apple", "banana", "cherry", "date"]
random_element = random.choice(my_list)
print("Random element from list:", random_element)

# Generate a list of random integers between 1 and 6 (like rolling dice)
dice_rolls = [random.randint(1, 6) for _ in range(5)]
print("Dice rolls:", dice_rolls)

```

# Пример 2. как работает цикл for

`how the cycle for works`

## Результат

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

```

# Пример 3. создай json -файл сотрудник телефон
`create a json file employee phone`

## Результат

```python
import json

# Define a list of employees with their phone numbers
employees = [
    {"name": "John Doe", "phone": "+1 555-1234"},
    {"name": "Jane Smith", "phone": "+1 555-5678"},
    {"name": "Bob Johnson", "phone": "+1 555-9012"},
    {"name": "Alice Williams", "phone": "+1 555-3456"}
]

# Convert the list of employees to JSON
json_data = json.dumps(employees, indent=4)

# Write the JSON data to a file
with open("employees.json", "w") as file:
    file.write(json_data)

print("JSON file 'employees.json' has been created.")

```

```json
[
    {
        "name": "John Doe",
        "phone": "+1 555-1234"
    },
    {
        "name": "Jane Smith",
        "phone": "+1 555-5678"
    },
    {
        "name": "Bob Johnson",
        "phone": "+1 555-9012"
    },
    {
        "name": "Alice Williams",
        "phone": "+1 555-3456"
    }
]


```

# Tic Tac Toe on Tkinter


