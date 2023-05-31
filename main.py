#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Wellcome to my tip calculator project\n")
main_bil = input("What was the total bil?\n$")

main_bil_int = int(main_bil)

tip_per = input("What percentage would you like to give him?\n")

tip_int = int(tip_per)

people = input("How many people to split the bil:\n")

people_int = int(people)

total_per_ammount = str(f"1.{tip_int}")

total_int = float(total_per_ammount)

total_with_per = main_bil_int * total_int

per_person_bil = total_with_per / people_int

round_bil = round(per_person_bil, 2)

print(f"each person should pay ${round_bil}")