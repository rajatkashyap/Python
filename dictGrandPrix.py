# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:04:12 2018

@author: U40MV02
"""

race_results={'Australia': ['Sebastian Vettel',
               'Lewis Hamilton',
               'Kimi Raikkonen',
               'Daniel Ricciardo',
               'Fernando Alonso',
               'Max Verstappen',
               'Nico Hulkenberg',
               'Valtteri Bottas',
               'Stoffel Vandoorne',
               'Carlos Sainz'],
 'Austria': ['Max Verstappen',
             'Kimi Raikkonen',
             'Sebastian Vettel',
             'Romain Grosjean',
             'Kevin Magnussen',
             'Esteban Ocon',
             'Sergio Perez',
             'Fernando Alonso',
             'Charles Leclerc',
             'Marcus Ericsson'],
 'Azerbaijan': ['Lewis Hamilton',
                'Kimi Raikkonen',
                'Sergio Perez',
                'Sebastian Vettel',
                'Carlos Sainz',
                'Charles Leclerc',
                'Fernando Alonso',
                'Lance Stroll',
                'Stoffel Vandoorne',
                'Brendon Hartley'],
 'Bahrain': ['Sebastian Vettel',
             'Valtteri Bottas',
             'Lewis Hamilton',
             'Pierre Gasly',
             'Kevin Magnussen',
             'Nico Hulkenberg',
             'Fernando Alonso',
             'Stoffel Vandoorne',
             'Marcus Ericsson',
             'Esteban Ocon'],
 'Belgium': ['Sebastian Vettel',
             'Lewis Hamilton',
             'Max Verstappen',
             'Valtteri Bottas',
             'Sergio Perez',
             'Esteban Ocon',
             'Romain Grosjean',
             'Kevin Magnussen',
             'Pierre Gasly',
             'Marcus Ericsson'],
 'Canada': ['Sebastian Vettel',
            'Valtteri Bottas',
            'Max Verstappen',
            'Daniel Ricciardo',
            'Lewis Hamilton',
            'Kimi Raikkonen',
            'Nico Hulkenberg',
            'Carlos Sainz',
            'Esteban Ocon',
            'Charles Leclerc'],
 'China': ['Daniel Ricciardo',
           'Valtteri Bottas',
           'Kimi Raikkonen',
           'Lewis Hamilton',
           'Max Verstappen',
           'Nico Hulkenberg',
           'Fernando Alonso',
           'Sebastian Vettel',
           'Carlos Sainz',
           'Kevin Magnussen'],
 'France': ['Lewis Hamilton',
            'Max Verstappen',
            'Kimi Raikkonen',
            'Daniel Ricciardo',
            'Sebastian Vettel',
            'Kevin Magnussen',
            'Valtteri Bottas',
            'Carlos Sainz',
            'Nico Hulkenberg',
            'Charles Leclerc'],
 'Germany': ['Lewis Hamilton',
             'Valtteri Bottas',
             'Kimi Raikkonen',
             'Max Verstappen',
             'Nico Hulkenberg',
             'Romain Grosjean',
             'Sergio Perez',
             'Esteban Ocon',
             'Marcus Ericsson',
             'Brendon Hartley'],
 'Great Britain': ['Sebastian Vettel',
                   'Lewis Hamilton',
                   'Kimi Raikkonen',
                   'Valtteri Bottas',
                   'Daniel Ricciardo',
                   'Nico Hulkenberg',
                   'Esteban Ocon',
                   'Fernando Alonso',
                   'Kevin Magnussen',
                   'Sergio Perez'],
 'Hungary': ['Lewis Hamilton',
             'Sebastian Vettel',
             'Kimi Raikkonen',
             'Daniel Ricciardo',
             'Valtteri Bottas',
             'Pierre Gasly',
             'Kevin Magnussen',
             'Fernando Alonso',
             'Carlos Sainz',
             'Romain Grosjean'],
 'Italy': ['Lewis Hamilton',
           'Kimi Raikkonen',
           'Valtteri Bottas',
           'Sebastian Vettel',
           'Max Verstappen',
           'Esteban Ocon',
           'Sergio Perez',
           'Carlos Sainz',
           'Lance Stroll',
           'Sergey Sirotkin'],
 'Monaco': ['Daniel Ricciardo',
            'Sebastian Vettel',
            'Lewis Hamilton',
            'Kimi Raikkonen',
            'Valtteri Bottas',
            'Esteban Ocon',
            'Pierre Gasly',
            'Nico Hulkenberg',
            'Max Verstappen',
            'Carlos Sainz'],
 'Spain': ['Lewis Hamilton',
           'Valtteri Bottas',
           'Max Verstappen',
           'Sebastian Vettel',
           'Daniel Ricciardo',
           'Kevin Magnussen',
           'Carlos Sainz',
           'Fernando Alonso',
           'Sergio Perez',
           'Charles Leclerc']}
def find_country(driver_name, rank):
    c=[]
    for i in race_results:
        #print race_results[i]
        if race_results[i][rank-1]==driver_name:
            c.append(i)
    #print  (c)
    
find_country ("Lewis Hamilton", 1)

points1=[10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]

def three_top_driver(points):
    d={}
    topthree=[]
    d1={}
    for i in race_results:
        #print i
        for x in range(len(race_results[i])):
            if race_results[i][x] in d:
                d[race_results[i][x]]=d[race_results[i][x]]+points1[x]
            else:
                d[race_results[i][x]]=points1[x]
    topthree=sorted(d,key=d.get,reverse=True)[0:3]
    for i in topthree:
        d1[i]=d[i]
    return d1

    #return sorted(d,key=d.get,reverse=True)[0:3]
points2=[10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]
standing2 = three_top_driver(points2)
assert type(standing2) is dict,  "Did not create a dictionary."
assert len(standing2) == 3, "Dictionary has the wrong number of entries."
assert {'Lewis Hamilton', 'Sebastian Vettel', 'Kimi Raikkonen'} == set(standing2.keys()), "Dictionary has the wrong keys."
assert standing2['Lewis Hamilton'] == 116, 'Wrong points for: Lewis Hamilton'
assert standing2['Sebastian Vettel'] == 106, 'Wrong points for: Sebastian Vettel'
assert standing2['Kimi Raikkonen'] == 87, 'Wrong points for: Kimi Raikkonen'

def podium_count(driver_name):
    cnt=0
    for i in race_results:
        if driver_name in race_results[i][0:3]:  
            cnt+=1
    return cnt

print podium_count('Lewis Hamilton')
