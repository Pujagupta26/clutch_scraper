from operator import mod
import requests
import csv
from bs4 import BeautifulSoup
url = "https://clutch.co/directory/mobile-application-developers"

r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

soup = BeautifulSoup(htmlcontent,'html.parser')
provider = soup.find_all(class_="provider-row")
data=[]
for each in provider:
    company = each.find(class_="company_info").find("a").text.lstrip().rstrip()
    website = each.find(class_="website-link__item", href=True)["href"].lstrip().rstrip()
    rating=each.find(class_="sg-rating__number").text.lstrip().rstrip()
    module=each.find(class_="module-list").text.split('\n')
    modified=[i for i in module if len(i)>0]
    size=modified[0]
    hourly=modified[1]
    employee=modified[2]
    location=modified[3]
    quote=each.find(class_="blockquote-in-module").find("p").text.lstrip().rstrip()
    tag=each.find(class_="company_info__wrap").text.lstrip().rstrip()
    reviews = each.find(class_="reviews-link").text.lstrip().rstrip()
    
    data.append([str(company),str(website),str(location),str(rating),str(reviews),str(hourly),str(size),str(employee),str(quote),str(tag)])       
    print(company)
    print(website)
    print(rating)
    print(modified)
    print(quote)
    print(tag)
    print(reviews)
    print('+++++++++++++++++++++++++++++')
print(len(provider))   
fields = ['Company', 'Website', 'Location', 'Rating', 'Review Count', 'Hourly Rate', 'Min Project Size', 'Employee Size','Qoutation','Tagline']
file_name = 'Clutch_data.csv'
with open(file_name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    # csvwriter.writerows(data)
    for each in data:
        try:
            csvwriter.writerow(each)
        except:
            continue
        

