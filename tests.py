import unittest
import random
from linked_list import LinkedList
from cardmask import card_mask


class TestLinkedList(unittest.TestCase):

    def test_push(self):
        l = LinkedList()
        l.push(65255)
        l.push(65254)
        self.assertEqual(l.head.value, 65254)
        self.assertEqual(l.head.next.value, 65255)


class TestCardMask(unittest.TestCase):

    def test_card_mask(self):
        n1 = random.randint(10**15, 10**16-1)
        n2 = random.randint(10**17, 10**18-1)
        result1 = card_mask(n1)
        self.assertEqual(result1, f"{str(n1)[0:4]} {str(n1)[-4:]}")
        result2 = card_mask(n2)
        self.assertEqual(result2, f"{str(n2)[0:4]} {str(n2)[-6:-2]} {str(n2)[-2:]}")
        self.assertRaises(ValueError, card_mask, "123323232")



if __name__ == '__main__':
    unittest.main()