#Dictionary = a collection of {key:value} pairs
                # ordered and changeable. Duplicate Ok

capitals = {"Bangladesh": "Dhaka",
            "India": "New Delhi",
            "USA" : "Washington D.C.",
            "China" : "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))
# print(capitals.get("japan"))

# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print("That capital does not exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem() # this will remove latest key added means the last will be removed
# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# print(keys) # advance : object

# for key in keys:
#     print(key)

# for capital in capitals.values():
#     print(capital)

# for key, value in capitals.items():
#     print(f"{key}: {value}")
