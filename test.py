



# %%
print ("hello world")
 # %%
print ("bye")


print ("hello world")


# %%


type(3)
# %%
type("three")
# %%
type(3.0)
# %%
type(True)

# %%

my_list=[3, "three", 3.0, True]
type(my_list)
# %%


my_list=['Johnn', 'Paul', 'George', 'Ringo']
my_list


my_list[3:-500]
# %%
my_list[0]
# %%
my_list[0:3]
# %%
my_list[1:]
# %%
my_list[:3]
# %%
my_list[3:-500]

my_list[::2]

# %%
print(my_list[-1])
print(my_list[-2])
# %%
print(my_list[::-1])
# %%
my_list[1] = my_list[1].upper()
my_list
# %%
my_list + ['Yoko']
print(my_list)
# %%
my_list = my_list + ['Yoko']

my_list
# %%
my_list = my_list[:4]

my_list
# %%
# The list can be multiplied by integer x to replicate the original list x times.
print(my_list * 2)
# As mentioned previously, to make changes to the original list, it must be reassigned.
my_list
# %%
# A list can be contained within another list.
# The concept of inserting a list into another is called nesting.
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# A nested list is formed by making a list of lists.
nest_list = [lst_1,lst_2,lst_3]
nest_list
# %%
my_list.reverse()
my_list
# %%
print('Accessing second item', nest_list[1])
print('Accessing second item of the second item', nest_list[1][1])
# %%

my_list = ['John', 'Paul', 'George', 'Ringo']
len(my_list)

# %%
len(3)
# %%
num_list = [3, 7, 1, 9, 42]
print(min(num_list))
print(max(num_list))
# %%
print(min(my_list))
print(max(my_list))
# %%
my_list = ['John', 'Paul', 'George', 'Ringo']
my_list.append(['Lennon','McCartney','Harrison', 'Starr'])

print(my_list)
# %%
# add items in iterable itemwise by the .extend() method.
my_list = ['John', 'Paul', 'George', 'Ringo']
my_list.extend(['Lennon','McCartney','Harrison', 'Starr'])

my_list
# %%
my_list = ['John', 'Paul', 'George', 'Ringo']
my_list.insert(1, 'Lennon')
my_list
# %%
# last_item will be assigned the value of the last element.
last_item = my_list.pop()
last_item
# %%
my_list
# %%
my_list.pop(0)
my_list
# %%
my_list = ['John', 'Lennon', 'Paul', 'George']
my_list.remove('Yoko')
# %%
num_list = [13,42,4,24,2,46,3,7]
num_list.reverse()

print(num_list)
# %%
list_of_strings = ["This", "is", "a", "sentence."]

print("    Random String    ".join(list_of_strings))
# %%
my_list = ['John', 'Lennon', 'Paul', 'George']
idx = my_list.index('Lennon')
print(idx)
# %%my_list = ['John', 'Lennon', 'Paul', 'George']
idx = my_list.index('Yoko')
print(idx)

# %%
set_1 = {'Dog', 'Cat', 'Platypus', 'Koala'}
set_2 = {'Crocodile', 'Hyena', 'Koala', 'Cat'}
print(set_1)
print(set_2)
union_set = set_1.union(set_2)
print(union_set)
# %%
differ_set = set_1.difference(set_2)
print(differ_set)