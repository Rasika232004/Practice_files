# Hera Pheri
cast1 = ['Akshay Kumar','Suniel Shetty','Paresh Rawal','Tabu']
# Bhool Bhulaiyaa
cast2 = ['Akshay Kumar','Vidya Balan','Shiney Ahuja','Rajpal Yadav']
# Welcome
cast3 = ['Akshay Kumar','Katrina Kaif','Nana Patekar','Anil Kapoor']
# Dhamaal
cast4 = ['Sanjay Dutt','Arshad Warsi','Javad Jaffery','Riteish Deshmukh']
# Andaz Apna Apna
cast5 = ['Aamir Khan','Salman Khan','Raveena Tandon','Paresh Rawal']

movie_db = {
    "Hera Pheri": cast1,
    "Bhool Bhulaiyaa":cast2,
    "Welcome":cast3,
    "Dhamaal":cast4,
    "Andaz Apna Apna": cast5
}

# print(movie_db)

# '''
# Task 1 : display the name of movie one by one from your movie_db
# '''
# for title in movie_db.keys():
#     print(title)

# '''
# Task2: Display movie name who is having 'Akshay Kumar' init.
# '''
# # way 1
# for title, cast in movie_db.items():
#     if 'Akshay Kumar' in cast:
#         print(title)
 
# # way2       
# for movies in movie_db.keys():
#     if 'Akshay Kumar' in movie_db.get(movies):
#         print(movies)

# '''
# Task3: Find the count of actor/actress names per movie whos name having more then 15 characters
# eg. display like Hera Pheri -> 1
#                  Bhool Bhulaiyaa -> 0
#                  Welcome -> 4             
# '''
# length_of_char = 15

# for movie, cast in movie_db.items():
#     count = 0

#     for name in cast:
#         if len(name) > length_of_char:
#             count += 1

#     print(f"{movie} -> {count}")

'''
Task3: Task3: Find the count of actor/actress names per movie whos name having more then 15 characters also print their name
eg. display like Hera Pheri -> 1
                 Bhool Bhulaiyaa -> 0 : Retesh deshmukh
                 Welcome -> 4   
'''
# length_of_char = 15

# for movie, cast in movie_db.items():
#     count = 0
#     long_names = []

#     for name in cast:
#         if len(name) > length_of_char:
#             count += 1
#             long_names.append(name)

#     print(f"{movie} -> {count} : {long_names}")

'''
Task4 : find frequency/repetition of every actor/actress name in your db
eg. 
freq = {}

{
    'Akshay Kumar': 3,
    'Suniel Shetty': 1 
} 
make small dict of this record
'''
# for name in movie_db.values():
#     count = 0
#     freq = {}
    
#     if name == 'Akshay Kumar':
#         count +=1
    
        
#     freq['Akshay Kumar'] = count

'''
Task5 : find frequency of every character given in a string 
s = 'i love python programming'

{'i':2, ' ':3, 'l':1 .............}
'''
s = 'i love python programming'

# way 1
freq = {}
for char in s:
    key = char
    value = s.count(char)
    
    freq[key] = value 
print(freq)

'''
level 2: create 
                    str    :   list
movie_db2023 = {}
movie_db2024 = {}
movie_db2025 = {"Dhurander": []}
movie_db2026 = {"Dhurander revenge": []}

movie_db = {2023 : movie_db2023,2024: movie_db2024,2025 : movie_db2025,2026: movie_db2026}
'''
