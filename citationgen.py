#This is a basic use of python for an automatic citation citer thing idk
creator = input("Please enter an editor, author or compiler name for your source in the format LastName, FirstName: ")
title = input("Please enter the title of your source whether it be a book, a website title, ect: ")
date = input("Please enter the date the piece of literature was published DD Mmm. YYYY: ")
place = input("Please enter the publisher of the piece of literature you are citing: ")
access = input("Please enter the current date DD Mmm. YYYY ")
print("Now you may copy pasta this text:" + (creator) + ". " + (title) + ". " + (date) + ". " + (place) + ", " + (access) + ". ")
