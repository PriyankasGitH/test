"""

-- Variables store different data types

-- Python uses classes to define data types. The class name are written in lower case

-- 8 Built in data types

1. Txt : str
2. Numeric : int, float, complex
3. Sequence : list, tuple, range
4. Mapping :  dict
5. Set : set, frozenset
6. Boolean : bool
7. Binary : bytes, bytearray, memory view
8. None : None Type

-- Operations

1. Get the data

2. Set the data

3. Set the specific data

"""
def addSpace():
    print()

# 1. Get the data

print("======== Getting the type ========")

a = 5
print(type(a))
print("Above got the type of a variable")
addSpace()

print("======== Setting the datatypes ========")

# 2. Set the data

# For string

b = "Hello world"
print("Setting the string type", b)

c = 0
print("Setting the int type", c)

d = 0.0
print("Setting the float type", d)

e = 1+1j
print("Setting the float type", e)

f = ["Apple", "Banana", "Cherry"]
print("Setting the list type", f)

g = ("Apple", "Banana", "Cherry")
print("Setting the tuple type", g)

h=range(0)
i=range(0,1)
j=range(2)
print("Setting the range type", h)
print("Setting the range type", i)
print("Setting the range type", j)

k={"name":"John","age":20}
print("Setting the dict type", k)

l={"Apple", "Banana", "Cherry"}
print("Setting the set type", l)

m=frozenset({"Apple", "Banana", "Cherry"})
print("Setting the frozen set type", m)

n=True
print("Setting the bool type", n)

o=b"Hello"
print("Setting the byte type", o)

p=bytearray(5)
print("Setting the bytearray type", p)

q=memoryview(bytes(5))
print("Setting the memoryview type", q)

r=None
print("Setting the None type", r)
addSpace()

print("======== Setting the specific type ========")

_b = str("Hello world")
print("Setting the specific specific string type", _b)

_c = int(0)
print("Setting the specific int type", _c)

_d = float(0.0)
print("Setting the specific float type", _d)

_e = complex(1+1j)
print("Setting the specific complex type", _e)

_f = list(("Apple", "Banana", "Cherry"))
print("Setting the specific list type", _f)

_g = tuple(("Apple", "Banana", "Cherry"))
print("Setting the specific tuple type", _g)

_h=range(0)
_i=range(0,1)
_j=range(2)
print("Setting the range type", _h)
print("Setting the range type", _i)
print("Setting the range type", _j)

_k=dict(name="John", age=0)
print("Setting the specific dict type", _k)

_l = set(("apple", "banana", "Cherry"))
print("Setting the specific set type", _l)

_m=frozenset(("Apple", "Banana", "Cherry"))
print("Setting the specific frozen set type", _m)

_n=bool(0)
print("Setting the specific bool type", _n)

_o=bytes(5)
print("Setting the specific byte type", _o)

_p=bytearray(5)
print("Setting the specific bytearray type", _p)

_q=memoryview(bytes(5))
print("Setting the specific memoryview type", _q)

