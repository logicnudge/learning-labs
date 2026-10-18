profile = {"name": "Sam"}
print(profile.get("role", "guest"))
try:
    print(profile["role"])
except KeyError:
    print("KeyError")
