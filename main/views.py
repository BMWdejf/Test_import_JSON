from django.shortcuts import render
from main.models import Population
import requests

def get_population():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)
    data = response.json()['data']
    #print(data)
    for country in data:
        Population.objects.update_or_create(
            country=country['Nation'],
            year=country['Year'],
            human_count=country['Population'],
        )
        print("saved")