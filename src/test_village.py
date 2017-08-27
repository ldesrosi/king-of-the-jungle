import unittest
import village
import villager
import resource

class TestVillage(unittest.TestCase):

    def test_villager_generation(self):
        theVillage = village.Village()
        self.assertTrue(len(theVillage.getVillagers()) in range(16,20))

    def test_village_unhappy(self):
        theVillage = village.Village()
        for theVillager in theVillage.getVillagers():
            self.assertTrue(theVillager.mood() == villager.State.HAPPY)
        theVillage.tick()
        theVillage.tick()
        for theVillager in theVillage.getVillagers():
            self.assertTrue(theVillager.mood() == villager.State.UNHAPPY)

    def test_feeding_half_village(self):
        theVillage = village.Village()
        half = len(theVillage.getVillagers())//2

        theVillage.addResource(resource.Resource(half, resource.ResourceType.RABBIT))

        theVillage.tick()
        theVillage.tick()

        happyVillagerCount = 0
        for theVillager in theVillage.getVillagers():
            if theVillager.mood() == villager.State.HAPPY:
                happyVillagerCount += 1

        self.assertEqual(half, happyVillagerCount)
