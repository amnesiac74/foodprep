#randomize lunch


protein = ["cheese","shrimp ball", "beef ball", "fish ball", "sausage","tofu","momo"]
vegetables = ['peas', 'broccoli', 'cauliflower', 'carrot',"corn","green beans"]
carbohydrates = ['rice ball', 'tortilla', 'bread', "sweet potato","pasta"]
fruits = ['raspberry', 'grapes', 'blackberry', 'melon', 'banana','kiwi', "peach"]


from random import choice
p = choice(protein)
v = choice(vegetables)
c = choice(carbohydrates)
f = choice(fruits)

for i in weekdays:
    


Monday = [p, v, c, f]

protein.remove(p)
vegetables.remove(v)
carbohydrates.remove(c)
fruits.remove(f)

p = choice(protein)
v = choice(vegetables)
c = choice(carbohydrates)
f = choice(fruits)

Tuesday = [p, v, c, f]

protein.remove(p)
vegetables.remove(v)
carbohydrates.remove(c)
fruits.remove(f)

p = choice(protein)
v = choice(vegetables)
c = choice(carbohydrates)
f = choice(fruits)

Wednesday = [p, v, c, f]
protein.remove(p)
vegetables.remove(v)
carbohydrates.remove(c)
fruits.remove(f)

p = choice(protein)
v = choice(vegetables)
c = choice(carbohydrates)
f = choice(fruits)

Thursday = [p, v, c, f]
protein.remove(p)
vegetables.remove(v)
carbohydrates.remove(c)
fruits.remove(f)

p = choice(protein)
v = choice(vegetables)
c = choice(carbohydrates)
f = choice(fruits)

Friday = [p, v, c, f]

import datetime
print (datetime.datetime.now())

m = print ("Monday : ", Monday)
t = print ("Tuesday : ", Tuesday)
w = print ("Wednesday : ", Wednesday)
th= print ("Thursday : ", Thursday)
f = print ("Friday : ", Friday)




print ('''
Monday
Tuesday
Wednesday
Thursday
Friday       
''')

import smtplib

FROM = user
To = youremail@gmail.com
message = message

server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(youremail@gmail.com, password)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'

