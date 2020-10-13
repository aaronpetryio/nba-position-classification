# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:45:58 2020

@author: apetry
"""

#Import requests, csv, and BeautifulSoup
import requests
import csv
from bs4 import BeautifulSoup

#Create lists for the NBA teams to pull from and the years to pull from
nba_teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BRK', 'ORL', 'CHO', 'WAS', 'CHI', 'NYK', 'DET', 'ATL', 'CLE', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR', 'MEM', 'PHO', 'SAS', 'SAC', 'NOP', 'MIN', 'GSW']
years = ['2020']

#Create an empty list to store the data
nba_player_data = []

#Create the header row with labels from the table 
url = "https://www.basketball-reference.com/teams/" + nba_teams[0] + "/" + years[0] + ".html"

#Get the URL from basketball-refernece
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Find the roster header row
roster_table = soup.find('table', attrs={'id':'roster'})
roster_headers = roster_table.find('thead')
headers = roster_headers.find_all('th')
headers = [ele.text.strip() for ele in headers]

#Manually add the Team header
team_header = ['Team']
combined_headers = team_header + headers

#Append the headers to the beginning of the nba_player_data list
nba_player_data.append([ele for ele in combined_headers])

#Manually add the Country column because it is blank on basketball-reference
nba_player_data[0][6] = "Country"

#Complete the data scrape for all NBA teams 
for nba_team in nba_teams:
    #Create a dynamic URL that can pull information from both the nba_teams and years lists 
    url = "https://www.basketball-reference.com/teams/" + nba_team + "/" + years[0] + ".html"
    
    #Get the URL from basketball-refernece
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #Find the roster table 
    roster_table = soup.find('table', attrs={'id':'roster'})
    roster_body = roster_table.find('tbody')
    roster_rows = roster_body.find_all('tr')
    
    #For each row in the roster table, add the player data to the nba_player_data list
    for row in roster_rows:
        #Create a Team column
        team_column = [nba_team]
        
        #Find the 'Number' column
        number_column = row.find_all('th')
        number_column = [ele.text.strip() for ele in number_column]

        #Find the rest of the data columns
        data_columns = row.find_all('td')
        data_columns = [ele.text.strip() for ele in data_columns]
        
        #Combine the columns and add them to the nba_player_data list 
        combined_columns = team_column + number_column + data_columns 
        nba_player_data.append([ele for ele in combined_columns])

#Create a dynamic CSV file name based on the year scraped
csv_file = "nba_player_data_" + years[0] + ".csv"

#Write the nba_player_data list to a CSV
with open(csv_file, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in nba_player_data:
        writer.writerow(data)
