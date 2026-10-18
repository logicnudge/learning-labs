values = [0, None, "", [], "0"]
for value in values:
    print(type(value).__name__, bool(value))
