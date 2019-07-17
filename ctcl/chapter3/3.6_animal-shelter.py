import unittest
import copy
from collections import deque
class AnimalShelter():
  def __init__(self):
    self.catQueue= deque()
    self.dogQueue= deque()
    self.order=0

  def enqueue(self, animal):
    animal.order=self.order
    self.order+=1
    if animal.__class__==Cat:
      self.catQueue.append(animal)
    else:
      self.dogQueue.append(animal)
  def dequeueAny(self):
    if not len(self.dogQueue):
      if not len(self.catQueue):
        return None
      return self.catQueue.popleft().name
    if not len(self.catQueue):
      return self.dogQueue.popleft().name
    firstDog=self.dogQueue[0]
    firstCat=self.catQueue[0]
    if firstDog.order>firstCat.order:
      return self.catQueue.popleft().name
    return self.dogQueue.popleft().name

  def dequeueDog(self):
    if not len(self.dogQueue):
      return None
    return self.dogQueue.popleft().name
  def dequeueCat(self):
    if not len(self.catQueue):
      return None
    return self.catQueue.popleft().name
class Animal():
  def __init__(self,name,next=None):
    self.next=next
    self.name=name
class Cat(Animal): pass
class Dog(Animal): pass

class Test(unittest.TestCase):
  def test_animal_shelter(self):
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))
    self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
    self.assertEqual(str(shelter.dequeueAny()), "Pluto")
    self.assertEqual(str(shelter.dequeueDog()), "Clifford")
    self.assertEqual(str(shelter.dequeueDog()), "Blue")
    self.assertEqual(str(shelter.dequeueCat()), "Garfield")
    self.assertEqual(str(shelter.dequeueDog()), "None")
    self.assertEqual(str(shelter.dequeueAny()), "Tony")
    self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
  Order=0
  unittest.main()