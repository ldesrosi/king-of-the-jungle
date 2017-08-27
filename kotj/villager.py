from enum import Enum

from kotj import resource

class State(Enum):
    HAPPY = 1
    UNHAPPY = 2
    REBELLING = 3
    DEAD = 4

class Skill(Enum):
    CHOPPING = 1
    MINING = 2
    HUNTING = 3

class Villager:
    def __init__(self):
        self.tickCount = 0
        self.ate = False
        self.drank = False
        self.working = None
        self.skillToResourceMap = {
            Skill.CHOPPING.name: [
                resource.ResourceDefinition(resource.ResourceType.WOOD, 100, 1, 1, 3)
                ],
            Skill.MINING.name: [
                resource.ResourceDefinition(resource.ResourceType.STONE, 85, 1, 1, 3),
                resource.ResourceDefinition(resource.ResourceType.IRON, 15, 1, 1, 3),
                ],
            Skill.HUNTING.name: [
                resource.ResourceDefinition(resource.ResourceType.RABBIT, 75, 1, 1, 3),
                resource.ResourceDefinition(resource.ResourceType.DEER, 30, 1, 1, 3),
                ]
            }

    def mood(self):
        if self.tickCount < 2:
            return State.HAPPY
        elif self.tickCount < 4:
            return State.UNHAPPY
        elif self.tickCount < 7:
            return State.REBELLING
        else:
            return State.DEAD

    def tick(self):
        if self.ate and self.drank:
            self.reset()
        else:
            self.tickCount += 1

    def eat(self):
        self.ate = True

    def drink(self):
        self.drank = True

    def reset(self):
        self.ate = False
        self.drank = False
        self.tickCount = 0

    def work(self, skill):
        self.working = skill

    def givesResources(self):
        if self.working is None:
            return None

        resDefList = self.skillToResourceMap[self.working.name]

        self.working = None

        isProductive = self.mood() == State.HAPPY

        listOfResources = []
        for resDef in resDefList:
            res = resDef.createResource(isProductive)
            if (res is not None):
                listOfResources.append(res)

        return listOfResources
