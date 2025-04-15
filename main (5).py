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
