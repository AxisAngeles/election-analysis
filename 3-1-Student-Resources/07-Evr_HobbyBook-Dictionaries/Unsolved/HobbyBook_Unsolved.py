# @TODO: Your code here
PetInfo = {
    "name":"Puchy",
    "age":8,
    "hobby":["eating","walking","sleeping"],
    "woke":{
        "monday":"10am",
        "tuesday":"9am",
        "wednesday":"11am"
    }
}

print(f'My pet´s name is {PetInfo["name"]} and he is {PetInfo["age"]} years old.')

print(f'My pet has {len(PetInfo["hobby"])} hobies and its favorite is {PetInfo["hobby"][1]}.')

print(f'My dog, {PetInfo["name"]}, wakes up at {PetInfo["woke"]["wednesday"]} every wednesday.')