import unittest
import villager
import resource

class TestVillager(unittest.TestCase):
    def checkEvolution(self, theVillager, expectedState):
        theVillager.tick()
        self.assertEqual(theVillager.mood(), expectedState)

    def tick(self, theVillager, numOfTick):
        for x in range (0, numOfTick):
            theVillager.tick()

    def test_initial_happy_mood(self):
        theVillager = villager.Villager()
        self.assertEqual(theVillager.mood(), villager.State.HAPPY)

    def test_becoming_unhappy(self):
        theVillager = villager.Villager()
        self.checkEvolution(theVillager, villager.State.HAPPY)
        self.checkEvolution(theVillager, villager.State.UNHAPPY)

    def test_ate_but_thirsty(self):
        theVillager = villager.Villager()
        theVillager.tick()
        theVillager.eat()
        self.checkEvolution(theVillager, villager.State.UNHAPPY)

    def test_ate_and_drank(self):
        theVillager = villager.Villager()
        theVillager.tick()
        theVillager.eat()
        theVillager.drink()
        self.checkEvolution(theVillager, villager.State.HAPPY)

    def test_gather_wood_happy(self):
        theVillager = villager.Villager()
        theVillager.work(villager.Skill.CHOPPING)
        theVillager.tick()
        gatheredResources = theVillager.givesResources()

        self.assertEqual(len(gatheredResources), 1)
        self.assertTrue(gatheredResources[0].getQty() in range(1,4))
        self.assertEqual(gatheredResources[0].getType(), resource.ResourceType.WOOD)

    def test_gather_wood_unhappy(self):
        theVillager = villager.Villager()
        self.tick(theVillager,2)
        theVillager.work(villager.Skill.CHOPPING)
        theVillager.tick()
        gatheredResources = theVillager.givesResources()

        self.assertEqual(len(gatheredResources), 1)
        self.assertEqual(gatheredResources[0].getQty(), 1)
        self.assertEqual(gatheredResources[0].getType(), resource.ResourceType.WOOD)

    def test_dying_of_hunger_or_thirst(self):
        theVillager = villager.Villager()
        self.tick(theVillager,7)
        self.checkEvolution(theVillager, villager.State.DEAD)

    def test_rebelling(self):
        theVillager = villager.Villager()
        self.tick(theVillager,4)
        self.checkEvolution(theVillager, villager.State.REBELLING)

    #def test_gather_wood_rebelling(self):
    #    theVillager = villager.Villager()
    #    self.tick(theVillager,4)
    #    theVillager.work(villager.Skill.CHOPPING)
    #    theVillager.tick()
    #    gatheredResources = theVillager.givesResources()

    #    self.assertEqual(len(gatheredResources), 1)
    #    self.assertEqual(gatheredResources[0].getQty(), -1)
    #    self.assertEqual(gatheredResources[0].getType(), resource.ResourceType.WOOD)

if __name__ == '__main__':
    unittest.main()
