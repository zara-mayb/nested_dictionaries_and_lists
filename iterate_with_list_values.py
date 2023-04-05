dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# def printInfo(dict):
#     print(str(len(dict["locations"])) + " " + "LOCATIONS")
#     for i in range(0, len(dict["locations"])):
#         print(dict["locations"][i])
#     print()
#     print(str(len(dict["instructors"])) + " " + "INSTRUCTORS")
#     for i in range(0, len(dict["instructors"])):
#         print(dict["instructors"][i])
# printInfo(dojo)

def printInfo(dict):
    for key in dict:
        print(len(dict[key]), key.upper())
        for element in dict[key]:
            print(element)
printInfo(dojo)


# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
