try:

    x = input("Please enter the number of gallons of gasoline: ")

    x = float(x)

    print "Original number of gallons is:", x
    print x, "gallons is the equivalent of", x * 3.7854
    print x, "gallons of gasoline requires", x / 19.5
    print x, "gallons of gasoline produces", x * 20, "pounds of CO2"
    print x, "gallons of gasoline is energy equivalent to", (x * 115000)/75700, "gallons of ethanol"
    print x, "gallons of gasoline requires", "$", x * 4.00, "USD"

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