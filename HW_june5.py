# '''
# Task4 : find frequency/repetition of every actor/actress name in your db
# eg. 
# freq = {}

# {
#     'Akshay Kumar': 3,
#     'Suniel Shetty': 1 
# } 
# make small dict of this record
# '''
# # Hera Pheri
# cast1 = ['Akshay Kumar','Suniel Shetty','Paresh Rawal','Tabu']
# # Bhool Bhulaiyaa
# cast2 = ['Akshay Kumar','Vidya Balan','Shiney Ahuja','Rajpal Yadav']
# # Welcome
# cast3 = ['Akshay Kumar','Katrina Kaif','Nana Patekar','Anil Kapoor']
# # Dhamaal
# cast4 = ['Sanjay Dutt','Arshad Warsi','Javad Jaffery','Riteish Deshmukh']
# # Andaz Apna Apna
# cast5 = ['Aamir Khan','Salman Khan','Raveena Tandon','Paresh Rawal']

# movie_db = {
#     "Hera Pheri": cast1,
#     "Bhool Bhulaiyaa":cast2,
#     "Welcome":cast3,
#     "Dhamaal":cast4,
#     "Andaz Apna Apna": cast5
# }

# freq = {}   # empty dict

# for cast_list in movie_db.values():
#     for actor in cast_list:
#         if actor in freq:
#             freq[actor] += 1
#         else:
#             freq[actor] = 1
        
# print(freq)
    
        
'''
level 2: create 
                    str    :   list
movie_db2023 = {}
movie_db2024 = {}
movie_db2025 = {"Dhurander": []}
movie_db2026 = {"Dhurander revenge": []}

movie_db = {2023 : movie_db2023,2024: movie_db2024,2025 , movie_db2025,2026: movie_db2026}
'''

movie_db2023 = {
    "Pathaan" : ['Shah Rukh Khan', 'John Abraham', 'Deepika Padukone'],
    "Jawan" : ['Shah Rukh Khan', 'Nayanthara', 'Vijay Sethupathi', 'Deepika Padukone'],
    "Tiger3" : ['Salman Khan', 'Katrina Kaif', 'Emraan Hashmi']
}

movie_db2024 = {
    "Fighter" : ['Hrithik Roshan', 'Deepika Padukone', 'Anil Kapoor', 'Karan Singh Grover'],
    "Stree2" : ['Rajkummar Rao', 'Shraddha Kapoor', 'Pankaj Tripathi', 'Aparshakti Khurana'],
    "Bhool_bhulaiyaa3"  : ['Kartik Aaryan', 'Vidya Balan', 'Madhuri Dixit', 'Triptii Dimri'],
    "Singham_again" : ['Ajay Devgn', 'Kareena Kapoor Khan', 'Ranveer Singh', 'Akshay Kumar', 'Deepika Padukone']
}

movie_db2025 = {
    "Sky_force" : ['Akshay Kumar', 'Veer Pahariya', 'Sara Ali Khan', 'Nimrat Kaur'],
    "Fateh" : ['Sonu Sood', 'Naseeruddin Shah', 'Jacqueline Fernandez'],
    "Chhaava" : ['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna'],
    "Azaad" : ['Ajay Devgn', 'Diana Penty', 'Aaman Devgan', 'Rasha Thadani']
}

movie_db2026 = {
    "Welcome_jungle" : ['Akshay Kumar', 'Sanjay Dutt', 'Suniel Shetty', 'Arshad Warsi', 'Paresh Rawal'],
    "Dhamaal4" : ['Ajay Devgn', 'Anil Kapoor', 'Madhuri Dixit', 'Riteish Deshmukh', 'Arshad Warsi', 'Jaaved Jaaferi'],
    "Love_and_war" : ['Ranbir Kapoor', 'Alia Bhatt', 'Vicky Kaushal'],
    "Ramayana_p1" : ['Ranbir Kapoor', 'Sai Pallavi', 'Sunny Deol', 'Yash']
}

movie_db = {2023 : movie_db2023, 2024: movie_db2024, 2025 : movie_db2025, 2026: movie_db2026}
print(movie_db)