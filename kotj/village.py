from kotj import villager
from kotj import resource
import random

class Village:

    def __init__(self):
        rndmno = random.randint(16, 20)
        self.villagers = [villager.Villager() for _ in range(rndmno)]
        self.resources = []
        self.food = []

    def addResource(self, theResource):
        if theResource.getType() == resource.ResourceType.DEER or theResource.getType() == resource.ResourceType.RABBIT:
            self.food.append(theResource)
        else:
            self.resources.append(theResource)

    def getVillagers(self):
        return self.villagers

    def feedVillage(self):
        for theVillager in self.villagers:
            if not self.food:
                break
            if self.food[0].getQty() == 0:
                self.food.pop()
            else:
                self.food[0].decrease(1)
                theVillager.eat()
                theVillager.drink()

    def tick(self):
        # Feed the people and make them drink
        self.feedVillage()

        # The people get older...
        for theVillager in self.villagers:
            theVillager.tick()
