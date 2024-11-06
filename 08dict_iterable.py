for key in dict.fromkeys(range(5)).items():
    print(key, type(key))

# dict views on dict.items(), dict.keys(), dict.values()
dicta = {"name": "Mhoamed", "age": 40, "thing": "thingy"}
print(type(dicta.keys()))
print(type(dicta.values()))
print(type(dicta.items()))

print(len(dicta))

# filter, map, zip are iterables
a = list(range(3))
b = {"a", "b", "c"}
print(a, b)

print(map(lambda x: x**2, a))
print(filter(lambda x : x%2==0, a))
print(zip(a,b))
