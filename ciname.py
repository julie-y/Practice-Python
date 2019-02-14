#create a data structures to store information,age rating, number of seats

films = {'Finding Dory':[3,5],
         'Bourne':[18,5],
         'Tarzan':[15,1],
         'Ghost Busters':[12,5]
         }

while True:
    #ask the user what film they wanna watch/
    choice = input ('Please select a movie:').strip().title()
    if choice in films:
         age =int( input('How old are you?:').strip())
         if age>=int(films[choice][0]): #check user age
             #check number of tickets
             seats = int(input('How many tickets do you need?').strip())
             num_seats = films[choice][1]
             if seats<=num_seats and num_seats> 0:
                print ('Enjoy the film!')
                films[choice][1]=films[choice][1]-seats     
             else:
                print('''sorry, we are sold out''')
         else:
             print('You are too young for that film')        
    else:
        print ('''sorry we don't have that film.''')

