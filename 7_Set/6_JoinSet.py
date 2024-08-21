"""
-- Several ways to join two sets

    -- Union() & Update() : joins all the items from both sets
        -- | operator instead of union method [ Two sets, multiple sets ]
            -- | allows union of two sets only
            -- Union allows union of two sets as well as a set & a tuple
        -- Join multiple sets [ Two sets, multiple sets ]
        -- Join a set & a tuple

        -- Update()
            -- inserts all items from set into another
            -- changes original set and doesn't return a new set

    -- intersection() : keeps only duplicates
        -- intersection keyword
        -- & operator
            -- & allows you to join sets only
            -- intersection allows you to join sets and other data types
        -- intersection_upate
            -- will keep only duplicates but it will change the original set insetad of returning a new set
        -- True & 1 are same & same for False & zero

    -- difference() : keeps the items from the first set that are not in the other sets
        -- returns a new set that will contain only the items from the first set that are not present in the other set
        -- Operator - for difference
            - Operator - allows only for sets and not for other data types like difference keyword

    -- difference_update : To keep items that are not present in both sets
        -- keeps the items from the first set that are not in the other set but it will change the original set instead of returning a new set

    -- symmetric_Difference() : keeps only elements that are not present in both sets
        -- ^ operator does the same operation only for sets unline symmetric_Difference
        -- symmetric_Difference_update() method will keep all but the duplicates, but it will change the original set instead of returning a new set

"""
"""
-- Union : returns a new set with all items from both sets
"""
def addSpace():
    print()

print("========= Set with union ===========")
set1 = {"a","b","c"}
print(set1, ": Set 1 before union")
set2 = {1,2,3}
print(set2, ": Set 2 before union")
set3 = set1.union(set2)
print(set3, ": Set After union")
addSpace()

print("========= Set with | operator ===========")
set1 = {"a","b","c"}
print(set1, ": Set 1 before union")
set2 = {1,2,3}
print(set2, ": Set 2 before union")
set3 = set1 | (set2)
print(set3, ": Set After union")
addSpace()

print("========= Join multiple sets with union ===========")
setA = {"a","b","c"}
print(setA, ": setA before union")
setB = {1,2,3}
print(setB, ": setB before union")
setC = {"John", "Elenea"}
print(setC, ": setC before union")
setD = {"Banana", "apple", "Strawberry"}
print(setD, ": setD before union")
mysetunion = setA.union(setB, setC, setD)
print(mysetunion, ": All Sets After union")
addSpace()

print("========= Join multiple sets with | ===========")
setA = {"a","b","c"}
print(setA, ": setA before union")
setB = {1,2,3}
print(setB, ": setB before union")
setC = {"John", "Elenea"}
print(setC, ": setC before union")
setD = {"Banana", "apple", "Strawberry"}
print(setD, ": setD before union")
mysetunion = setA | setB | setC | setD
print(mysetunion, ": All Sets After union")
addSpace()

print("========= Join a set & a tuple ===========")
mySet = {"a","b","c"}
print(setA, ": mySet before union")
myTuple = (1,2,3)
print(myTuple, ": Tuple before union")
setAndTuple = mySet.union(myTuple)
print(setAndTuple, ": Union of set & Tuple")
addSpace()

print("========= Update a set ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before updation")
mySetB = {1,2,3}
print(mySetB, ": mySet B before updation")
mySetA.update(mySetB)
print(mySetA, ": Updation of both sets")
addSpace()

print("========= Intersection of a set with intersection keyword ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before intersection")
mySetB = {1,2,3,"a"}
print(mySetB, ": mySet B before intersection")
mySetC = mySetA.intersection(mySetB)
print(mySetC, ": Intersection of both sets")
addSpace()

print("========= Intersection of a set with intersection & ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before intersection")
mySetB = {1,2,3,"a"}
print(mySetB, ": mySet B before intersection")
mySetC = mySetA & mySetB
print(mySetC, ": Intersection of both sets")
addSpace()

print("========= Intersection of a set with intersection intersection_update ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before intersection")
mySetB = {1,2,3,"a"}
print(mySetB, ": mySet B before intersection")
mySetA.intersection_update(mySetB)
print(mySetA, ": Intersection of both sets")
addSpace()

print("========= Intersection of a set with intersection with True, False, 1 and zero ===========")
mySetA = {"a","b","c", True, 0}
print(mySetA, ": mySet A before intersection")
mySetB = {False,1,2,3,"a"}
print(mySetB, ": mySet B before intersection")
intersectionSet = mySetA.intersection(mySetB)
print(intersectionSet, ": Intersection of both sets")
addSpace()

print("========= difference ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before difference")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before difference")
differenceSet = mySetA.difference(mySetB)
print(differenceSet, ": Difference of both sets")
addSpace()

print("========= difference operator - ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before difference")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before difference")
differenceSet = mySetA - mySetB
print(differenceSet, ": Difference of both sets")
addSpace()

print("========= difference update()  ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before difference update")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before difference update")
mySetA.difference_update(mySetB)
print(mySetA, ": Difference of both sets")
addSpace()

print("========= Symmetric difference ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before symmetric difference ")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before symmetric difference")
differenceSet = mySetA.symmetric_difference(mySetB)
print(differenceSet, ": Difference of both sets")
addSpace()


print("========= Symmetric difference with ^ ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before symmetric difference ")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before symmetric difference")
differenceSet = mySetA ^ mySetB
print(differenceSet, ": Difference of both sets")
addSpace()

print("========= Symmetric difference with symmetric difference update() ===========")
mySetA = {"a","b","c"}
print(mySetA, ": mySet A before symmetric difference ")
mySetB = {"c", "d", "e"}
print(mySetB, ": mySet B before symmetric difference")
mySetA.symmetric_difference_update(mySetB)
print(mySetA, ": Symmetric difference update")
addSpace()