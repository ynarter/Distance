# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:38:27 2021

@author: mnart
"""
"""
Write a function, distances() that takes a filename(str), an origin(str) and a
destination (str) as parameters. The function should read the file, and starting from the
origin, find and return the distance (kms) between the origin and the destination. If there
is no route found between the two cities, the function should return -1.
Important Notes:
• Each line of the file contains start_city, end_city and the distance between the
start_city and end_city (in kms).
• You may assume that the start_city on a given line was the end_city from the
previous line (i.e. the next city on the route).
• The origin may not be the first city in the file, and the destination may not be the
last city.
• You should NOT use a nested loop in your solution.
"""

def distances(filename,origin,destination):
    file= open(filename,'r')
    calc= -1
    for line in file:
        data= line.split(',')
        if data[0].lower()==origin.lower():
            calc=0
        #if they are on the same line
        if calc==0 and data[1].lower()==destination.lower():
            calc= float(data[2])
            return calc
            
        elif calc>=0:
            if data[1].lower()==destination.lower():
                calc += float(data[2])
                return calc
            else:
                calc += float(data[2])
                
    #if no destination found
    calc= -1            
    return calc
                

file= 'dis.txt'

orig= input('Enter origin(quit to exit): ')

dest= input('Enter destination: ')

while orig != 'quit':
    d= distances(file, orig, dest)
    print(f'{d:.1f}')
    
    orig= input('Enter origin(quit to exit): ')

    dest= input('Enter destination: ')
    
        
