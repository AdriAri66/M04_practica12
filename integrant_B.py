import json

data ="""
    {
    "books":[
        {"title": "Harry Potter: Caliz de fuego", 
        "cover": "dura", 
        "year": 2000, 
        "pages": 767
        },
        {"title": "Stephen King: Cuento de hadas", 
        "cover": "dura", 
        "year": 2022, 
        "pages": 865
        },
        {"title": "Dispersión", 
        "cover": "blanda", 
        "year": 2021, 
        "pages": 193
        },
        {"title": "Asi es la puta vida", 
        "cover": "dura", 
        "year": 2022, 
        "pages": 206
        }
    ]
}
"""
with open("data1", "w") as file:
    json.dump(data,file)

with open("data1", "r") as file:
    result = json.load(file)
    print(result)
