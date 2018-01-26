#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:37:46 2018

@author: jerry
"""

def rotate_matrix(matrix, direction):
    m = len(matrix)                 #number of rows in the original matrix
    n = len(matrix[0])              #number of columns in the original matrix
    
    #r = 0                          #row number in the new matrix
    #c = 0                          #column number in the new matrix
    
    newMat = [[0 for r in range(n)] for c in range(m)]  #set up new, rotated matrix with n rows and m columns
    
    r = 0                           #reuse r as current row being set in newMat
    c = 0                           #reuse c as current column being set in newMat
        
    if direction == 'left':         #rotate matrix left         
        while r < n:                
            while c < m:            
                newMat[r][c] = matrix[c][n - r - 1]
                c = c + 1       
            c = 0
            r = r + 1
            
    elif direction == 'right':      #rotate matrix right
        while r < n:
            while c < m:
                newMat[r][c] = matrix[m - c - 1][r]
                c = c + 1
            c = 0
            r = r + 1
            
    return newMat                   #return rotated matrix
            
sampleMat = [['1', '2', '3', '4'],
             ['5', '6', '7', '8'],
             ['9', 'A', 'B', 'C'],
             ['D', 'E', 'F', 'G']]

x = 0                               #current row in sampleMat to be printed
y = 0                               #current column in sampleMat to be printed

print('Original matrix: ')          #print sampleMat
while x < len(sampleMat):
    print('['),
    while y < len(sampleMat):
        print(sampleMat[x][y]),
        y = y + 1
        if(y < len(sampleMat)):
            print(', '),
        else:
            print(']')
    y = 0
    x = x + 1

rotatedSampleMat = rotate_matrix(sampleMat, 'right')        #rotated sampleMat

x = 0
y = 0

print('Rotated matrix: ')           #print rotatedSampleMat
while x < len(rotatedSampleMat):
    print('['),
    while y < len(rotatedSampleMat):
        print(rotatedSampleMat[x][y]),
        y = y + 1
        if(y < len(rotatedSampleMat)):
            print(', '),
        else:
            print(']')
    y = 0
    x = x + 1
