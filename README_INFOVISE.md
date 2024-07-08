"""
This project is InfoVise, a terminal-based application that recommends the user potential career paths based on 
classes that they have actually or hypothetically taken. We offer an account feature that allows one to create an account, 
change their password if need be, print the available differntiable classes offered at the iSchool, and add courses to their 
specific account.    

Since the program runs off of terminal, all  one would need to do to run it is to enter "python/python3 final.py" within the 
directory in which the file is located. Here's an example: 

Then, the user can interact with the number based menu system. To interact with it, all 
you would need to do is enter the number that corresponds with the action that you would like to do and follow the instructions. 
Once you make a number action, you cannot go back! To exit the program, you would press 6 and enter when on the main menu.

Annotated Bibliography: 

Diveintopython. (n.d.). Update(). Dive into Python: Free Tutorials, Books to Learn Python. 
    https://diveintopython.org/functions/dictionary-methods/update


    We utlized this website to better understand how to use update(). This built-in function aided us going into the self 
    for the user and updating the possible career option for them. 

    
Programiz. (n.d.). Python Dictionary items(). Programiz: Learn to Code for Free. 
    https://www.programiz.com/python-programming/methods/dictionary/items

    To print out all of the Cognate Classes that one could take at the iSchool, we needed a for loop. And in that for loop, 
    items was used to access the variable_classes dictionary. 

Uejio, J. (n.d.). Immutable vs. Hashable - Real Python [Video]. Python Tutorials - Real Python. 
    https://realpython.com/lessons/immutable-vs-hashable/

    Throughout our code, we were facing issues with making sure that the courses taken and the potential career paths 
    that the user could take were only mentioned once. This require us to understand mutability, hashability, and how that relates 
    to lists vs. sets. This ultimately led use to using sets within our code. 
"""
