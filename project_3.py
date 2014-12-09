try:
    x = input("Please enter a speed in miles/hour: ")
    x = float(x)

    print "Original speed in mph is:", x
    print "Converted to barleycorn/day is:", x * 1609.34 * 117.647 * 24
    print "Converted to furlongs/fortnight is:", x * 8 * 336
    print "Converted to Mach number is:", (x * 5280 / 1130) / 3600
    print "Converted to the percentage of the speed of light is:", (x * 1609.34) / 3600 / 299792458

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