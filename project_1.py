try:
    x = input("Please enter the first integer: ")
    y = input("Please enter the second integer: ")

    print "The sum of", x, "and", y, "is:", x + y
    print "The difference of", x, "and", y, "is:", x - y
    print "The product of", x, "and", y, "is:", x * y
    print "The quotient of", x, "and", y, "is:", x / y, "with remainder:", x%y

except NameError:
    print "*** PlEASE ENTER A NUMERIC VALUE ***"

    import sys
    import os
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    if __name__ == "__main__":
            restart_program()

except ZeroDivisionError:
    print "*** PLEASE DO NOT DIVIDE BY ZERO ***"

    import sys
    import os
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    if __name__ == "__main__":
            restart_program()