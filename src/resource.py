from enum import Enum
import random

class ResourceType(Enum):
    WOOD = 1
    STONE = 2
    IRON = 3
    RABBIT = 4
    DEER = 5

class ResourceDefinition:
    def __init__(self, type, successRate, min, maxUnproductive, maxProductive):
        self.type = type
        self.successRate = successRate
        self.min = min
        self.maxUnproductive = maxUnproductive
        self.maxProductive = maxProductive

    def createResource(self, isProductive):
        randNo = random.randint(0, 100)
        if (randNo <= self.successRate):
            max = self.maxUnproductive
            if (isProductive):
                max = self.maxProductive
            qty = random.randint(self.min,max)
            return Resource(qty, self.type)
        return None


class Resource:
    def __init__(self, qty, type):
        self.qty = qty
        self.type = type

    def getQty(self):
        return self.qty

    def getType(self):
        return self.type

    def decrease(self, qtyToDecrease):
        self.qty -= qtyToDecrease
