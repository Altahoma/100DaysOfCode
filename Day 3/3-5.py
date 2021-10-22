# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = (name1 + name2).lower()
score_true = 0
score_love = 0

score_true += names.count('t')
score_true += names.count('r')
score_true += names.count('u')
score_true += names.count('e')

score_love += names.count('l')
score_love += names.count('o')
score_love += names.count('v')
score_love += names.count('e')

score = int(str(score_true) + str(score_love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
