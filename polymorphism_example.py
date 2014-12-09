class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastesLike(self):
        raise Exception("Subclasses are responsible for creating this method")
 

class HotDog(Food):

    def tastesLike(self):
        print self.name, "is type", self.__class__
        print "has", self.calories, "calories"
        print "Tastes like extremely processed meat"
 

class Hamburger(Food):

    def tastesLike(self):
        print self.name, "is type", self.__class__
        print "has", self.calories, "calories"
        print "Tastes like grilled goodness"
 

class ChickenPatty(Food):

    def tastesLike(self):
        print self.name, "is type", self.__class__
        print "has", self.calories, "calories"
        print "Tastes like chicken"
 
dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))
 
for course in dinner:
    course.tastesLike()