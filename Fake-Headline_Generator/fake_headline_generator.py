import random

subjects = ["Virat kohli" , "Prime minister narendra modi" , "Rocking star yash" , "Elon musk" , "A bus driver from banglore","A common man" , "A indian dog"]
actions = ["smashes" , "launches" , "shoots" , "prepares" , "drives" , "declares" , "writes" , "eats" , "swims" , "dances"]
places_or_things = ["a century" , "a missile" , "inside the parliment" , "a rocket" , "trees" , "on the sky" , "in the water" , "in a box" , "inside the court" ]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"  

    print("\n" , headline)
    print()
    print("-"*20)

    user_input = input("\nDo you want another headline (yes/no): ").strip().lower()
    if user_input == "no":
        break
print("\nThank you for using the Fake Headline Generator. Have a fun day.")