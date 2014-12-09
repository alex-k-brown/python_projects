"""

******************************
 PROJECT 7 - MENU
******************************
1. Write input to file
2. Write input to screen
3. Quit
******************************
Enter your choice [1-3] : 2
Enter a phrase: Yet another phrase
You entered: 'Yet another phrase'

"""

print "******************************* \n"
print " PROJECT 7 - MENU \n"
print "******************************* \n"
print "1. Write input to file \n"
print "2. Write input to screen \n"
print "3. Quit \n"
print "******************************* \n"
user_choice = raw_input("Enter your choice [1-3]: ")
if user_choice == "1":
    file_phrase = raw_input("Enter a phrase: ")
    print "Writing", file_phrase, "to file user_input.dat"
    f = open("user_input.dat", "w")
    for _ in range(1):
        f.write(file_phrase)
        f.write("\n")
    f.close()

elif user_choice == "2":
    screen_phrase = raw_input("Enter a phrase: ")
    print "You entered: ", screen_phrase
else:
    print "Goodbye."
