# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:06:56 2023

@author: jaidev
"""

inred=[]
notinred=[]
oneinred=[]
twoinred=[]
while True:
    flag = input("\n\n++++++++++++++++++\nType N for next input and E for ending the game\n")
    if flag == 'N':
        n = int(input("Enter the Number\n"))
        val = input("Enter the Alphabets in Space Separated format\n").split()
        if n == 3:
            inred.extend(val)
        elif n == 0:
            notinred.extend(val)
        elif n == 1:
            oneinred.append(val)
        elif n== 2:
            twoinred.append(val)
        
        if len(oneinred)!=0:
            remove_oneinred = []
            for i in range(len(oneinred)):
                #print("***",oneinred, i,"***")
                if oneinred[i][0] in inred:
                    notinred.append(oneinred[i][1])
                    notinred.append(oneinred[i][2])
                    remove_oneinred.append(i)
                elif oneinred[i][1] in inred:
                    notinred.append(oneinred[i][0])
                    notinred.append(oneinred[i][2])
                    remove_oneinred.append(i)
                elif oneinred[i][2] in inred:
                    notinred.append(oneinred[i][1])
                    notinred.append(oneinred[i][0])
                    remove_oneinred.append(i)
                elif oneinred[i][0] in notinred and oneinred[i][1] in notinred:
                    inred.append(oneinred[i][2])
                    remove_oneinred.append(i)
                elif oneinred[i][1] in notinred and oneinred[i][2] in notinred:
                    inred.append(oneinred[i][0])
                    remove_oneinred.append(i)
                elif oneinred[i][0] in notinred and oneinred[i][2] in notinred:
                    inred.append(oneinred[i][1])
                    remove_oneinred.append(i)

        
        if len(twoinred)!=0:
            remove_twoinred = []
            for i in range(len(twoinred)):
                if twoinred[i][0] in notinred:
                    inred.append(twoinred[i][1])
                    inred.append(twoinred[i][2])
                    remove_twoinred.append(i)
                elif twoinred[i][1] in notinred:
                    inred.append(twoinred[i][0])
                    inred.append(twoinred[i][2])
                    remove_twoinred.append(i)
                elif twoinred[i][2] in notinred:
                    inred.append(twoinred[i][1])
                    inred.append(twoinred[i][0])
                    remove_twoinred.append(i)
                elif twoinred[i][0] in inred and twoinred[i][1] in inred:
                    notinred.append(twoinred[i][2])
                    remove_twoinred.append(i)
                elif twoinred[i][1] in inred and twoinred[i][2] in inred:
                    notinred.append(twoinred[i][0])
                    remove_twoinred.append(i)
                elif twoinred[i][0] in inred and twoinred[i][2] in inred:
                    notinred.append(twoinred[i][1])
                    remove_twoinred.append(i)
        
            
        print("The list of red is: ", set(inred))
        print("\nThe list of not red is: ", set(notinred))
                    
    else:
        print("The list of red is: ", set(inred))
        print("\nThe list of not red is: ", set(notinred))
        break