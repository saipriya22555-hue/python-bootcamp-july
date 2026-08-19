computer_science = {
    "student_1": {
        "name": "sai",
        "mark": 98
    },
    "student_2": {
        "name": "bena",
        "mark": 100
    }
}

for key, value in computer_science.items():
    print(key, value["name"], value["mark"])
