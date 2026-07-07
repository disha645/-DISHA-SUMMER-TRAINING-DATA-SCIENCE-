#student information
student ={
    "name": "disha",
    "age": 21,
    "college": "ADGIPS",
      
}
print(student)

student =dict(name="rohan", age=21, college="IIT DELHI")
print(student)
student["marks"] = 90
print(student)
#update a value
student["age"] = 22
print(student)
#delete a key-value pair
del student["college"]
print(student)
print(len(student))

#world cup information
world_cup ={
    2021: {
        "teams": ["India", "Australia", "England"],
        "captains": ["ms dhoni", "Aaron Finch", "Eoin Morgan"],
        "winner": ["India"]
    },
    2024: {
        "teams": ["India", "Pakistan", "Sri Lanka"],
        "captains": ["Virat Kohli", "Babar Azam", "Dasun Shanaka"],
        "winner": ["India"]
    },
    2026: {
        "teams": ["India", "New Zealand", "South Africa"],
        "captains": ["Rohit Sharma", "Kane Williamson", "Temba Bavuma"],
        "winner": ["India"]
    }
}
for year in world_cup:
    print("Year:", year)
    print("Teams:", world_cup[year]["teams"])
    print("Captains:", world_cup[year]["captains"])
    print("Winner:", world_cup[year]["winner"])
i = int(input("Enter the year of the World Cup: "))
if i in world_cup:
    print("Teams:", world_cup[i]["teams"])
    print("Captains:", world_cup[i]["captains"])
    print("Winner:", world_cup[i]["winner"])
