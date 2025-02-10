num = int(input("Enter a number: "))
if num % 5 == 0:
      print("The number is divisible by 5")
else:
      print("The number is not divisible by 5")

state = input("Enter a state: ")

if state == "Oregon":
      print("Salem")
elif state == "Washington":
      print("Olympia")
elif state == "California":
      print("Sacramento")
elif state == "Nevada":
      print("Carson City")
elif state == "Arizona":
      print("Phoenix")
else:
      print("I do not know that one")


#Under 2 years:  free,   Age 2–11:  $3,   Age 11–60:  $6, Over 60: $4
def pool_admission(age):
    if age < 2: 
        return 0 
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

age = int(input("Enter your age: ")) 
print("Your admission cost is $" + str(pool_admission(age)))

#import requests library
import requests 

#establish the url
url = "https://coccbobcat.com" 
response = requests.get(url) 

#count 160's 
count = response.text.count("160") 
print("The substring *160* appears", count, "in the HTML source of", url) 

#import psutil library
import psutil 

num_processes = len(psutil.pids()) 

print("Number of running processes:", num_processes)