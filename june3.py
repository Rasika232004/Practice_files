# # s = set()
# # print(type(s))

# # s.add(10)
# # s.add("Sai")
# # s.add(10)
# # s.add("SAI")
# # s.add(10)

# # print(s)
# # print(len(s))
# # print(id(s))

# # s.update([23,45.5])
# # print(s)    #{10, 'SAI', 45.5, 'Sai', 23}

# # s.update((23,56,34))
# # print(s)    #{34, 10, 'SAI', 45.5, 'Sai', 23, 56}

# # s.add(False)
# # s.add('hii')
# # s.add(2+3j)    

# # # list = [True, 90, 'Hii', 3+2j]
# # # s.add(list) #TypeError: unhashable type: 'list'
# # s.add(3.4)

# # print(s)   # {False, 34, 'hii', 3.4, 10, 'SAI', (2+3j), 45.5, 'Sai', 23, 56}

# # # s2 = {34,90,56,45,56}
# # # s.add(s2)
# # # print(s2)   # TypeError: unhashable type: 'set' reason: set is unhashable

# # t = (23,45,67)
# # s.add(t)
# # print(s)    # {False, 34, 'hii', 3.4, 10, 'SAI', (2+3j), 45.5, 'Sai', (23, 45, 67), 23, 56}

# # # d = {1:'one', 2:'two'}
# # # s.add(d) # TypeError: unhashable type: 'dict' reason: dict is unhashable
# # # print(s)

# # print(45 in s)  #False

# # s3 = {5,6,7,8}
# # for s in s3:
# #     print(s)    
    
# '''
# Task 1: Prove that the set is mutable by code
# '''
# s4 = {1,2,3,4,5,6,7,8}
# print("original id",id(s4))    # 140432644203456

# # adding an element to the set
# s4.add(9)
# print("after add id",id(s4))    

# if id(s4) == id(s4):
#     print("The set is mutable") # Hence proved that the set is mutable as the id of the set remains the same after adding an element to it.

# s = {1,2,3,4,5,6,7,8}
# s2 = {9,10,11,12,13,14,15}
# print(s | s2)    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# print(s & s2)    # set() as there are no common elements between s and s2
# s3 = s.intersection(s2)
# print(s3)    # set() as there are no common elements between s and s2

'''
Task 2 : Find common subjects both the students are learning 
ans: python and java are the common subjects both the students are learning
'''
student1 = {'Python','Java','SQL','HTML'}
student2 = {'PHP','Python','React','JAVA'}

for subject in student1:
    for subject2 in student2:
        if subject.lower() == subject2.lower(): # lower() method is used to convert the subject and subject2 to lowercase before comparing them, so that the comparison is case insensitive
            print(subject)   # Python and Java are the common subjects both the students are learning

'''
student1 = {'Python','Java','SQL','HTML'}
student2 = {'PHP','Python','React','JAVA'}
print(student1.intersection(student2))  # Common subjects

# way 2 : 
common_subjects = set()
for subject in student1:    # subject iterates through each element in student1
    if subject in student2: # if the subject is present in student2 then add it to common_subjects set
        common_subjects.add(subject)    # add method is used to add the common subject to the common_subjects set
print("Common subjects:",common_subjects)   # Common subjects: {'Python'}

# way 3
s = student1 & student2
print(s)    # {'Python'}
'''