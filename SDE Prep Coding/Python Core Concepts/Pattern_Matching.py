# X=input()
import math

#Capture Pattern Matching

# match(input()):
#     case "microsoft":
#         print("Ramesh is an Brilliant Research Software Engineer @ Microsoft Have Ever Seen")
#     case "google" as G:
#         print("Ramesh is an Brilliant Software Engineer @ {} Have Ever Seen".format(G))
#     case "adobe":
#         print("Ramesh is an Brilliant Computer Scientist Engineer @ Adobe Have Ever Seen")
#     case "None":
#         print("Ramesh is an Brilliant Problem Solver in Software Engineering Domain")
#     case "":
#         print("Ramesh is an Brilliant Scientist in Software Engineering Domain")
#     case _:
#         print("Ramesh - Site Reliability Engineer(Walmart)")

### Sequential Pattern Matching 

operations = [
    ["Add", 1, 2, 3, 4, 5],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

result = 0

# process each operation along with the set of given numbers
for op in operations:
    match op:
        case "Add", num1, *nums:
            result = num1 + sum(nums)
        case "Mul", num1, num2:
            result = num1 * num2
        case "Sqrt", num:
            result = math.sqrt(num)
        case _:
            continue

    # print(f"{op}: {result}")
# Example file for Advanced Python: Language Features by Joe Marini
# Using pattern guards to restrict how matches are made

# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5),
          Rectangle(9, 9)]

# use pattern matching to process each shape
# include pattern guards for more detailed processing
for shape in shapes:
    match shape:
        case Circle(radius=r) if r >= 6:
            print(f"Large Circle with area {shape.getarea()}")
        case Circle():
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle(width=w, height=h) if w == h:
            print(f"Square Rectangle with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")

# Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"{d}: Upper case string")
        case str():
            print(f"{d}: Not an upper-case string")
        # order is important here - Python will treat bools as ints
        # so the check for bool has to come before int
        case bool():
            print(f"{d}: Boolean")
        case int():
            print(f"{d}: Integer")
        case _:
            print(f"{d}: Something else")


# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order
for orders in test_orders:
    D_C = 0
    for order in orders:
        match order:
            case "shirt" | "pants" | "jacket" | "dress",size, starch, same_day:
                D_C += 12.95
                if starch:
                    starch="Starched"
                    D_C += 2.00
                else:
                    starch =""
                if same_day:
                    same_day = "same-day"
                    D_C += 10.00
                else:
                    same_day = ""
                print(f'Dry Clean: ({size}) {order[0]} {starch} {same_day}')
            case str() as desc, weight:
                if weight >= 15.0:
                    D_C += (weight * 4.95) * .9
                else:
                    D_C += (weight * 4.95)
                print(f"Wash/Fold: {desc}, weight: {weight:.1f}")
            case "comforter" | "cover" as blanket, dry_clean, size:
                D_C += 25.00
                print(f"Blanket: ({size}) {blanket}",
                      "Dry clean" if dry_clean else "")
            case _:
                print("invalid item format")
    print(f"Order total: {D_C:.2f}")
    print("--------------")
# print(D_C)
