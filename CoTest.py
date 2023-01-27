import random
#Daily Quote Machine!
Answer = ''
Quotes = ["Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen. - Winston Churchill", "You have enemies? Good. That means you've stood up for something, sometime in your life. - Winston Chruchill", "To improve is to change; to be perfect is to change often. - Winston Churchill", "Success consists of going from failure to failure without loss of enthusiasm. - Winston Churchill", "Attitude is a little thing that makes a big difference. - Winston Churchill", "...we shall fight in France, we shall fight on the seas and oceans, we shall fight with growing confidence and growing strength in the air, we shall defend our Island, whatever the cost may be, we shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender..."]
while Answer != 'Yes':
	Question = input("Do you want the quote of the day?:    ")
	if Answer == 'Yes':
		print(random.choice(Quotes))
