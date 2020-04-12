#  Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    "brother": {
        "name": "Dustin",
        "age": 36
    },
    "mother": {
        "name": "Dorothy",
        "age": 68
    },
    "dad": {
        "name": "Coleman",
        "age": 69
    }
}
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old

for familyMember, props in my_family.items():
    sentence = f"{props['name']} is my {familyMember} and is {props['age']} years old."
    print(sentence)