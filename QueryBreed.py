import petpy
import json
import csv
import datetime

#Create a timeline of the 30 days
Last30 = datetime.date.today() - datetime.timedelta(30)
CurrentDate = datetime.date.today()

#Auth to Pet Finder
pf = petpy.Petfinder(key="zJ2a8xkrhz9OUmCG0FSDqlmO2cZJtc76o3xhMBYlMxm6BFzhF7" , secret="T9QRnte2ypmPXaanWYHSerpdTIEPrgC2E7E6VlRo")

#Get 50 Results of adoptable dogs
adoptoable_Dog = pf.animals(animal_type='dog',status='adoptable',results_per_page=50,before_date=str(CurrentDate), after_date=str(Last30))

#organize the json file properly
json_object = json.dumps(adoptoable_Dog, indent=4)

#create the adoptable json file
with open("Adoptable_List.json", "w") as outfile:
    outfile.write(json_object)

#Get 50 results of adoped dogs
adopted_Dog = pf.animals(animal_type='dog',status='adopted',results_per_page=50,before_date=str(CurrentDate), after_date=str(Last30))
#organize the json file properly
json_object = json.dumps(adopted_Dog, indent=4)

#create the adopted json file
with open("adopted_Dog.json", "w") as outfile:
    outfile.write(json_object)
