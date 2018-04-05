import unittest
import mock
from service.exploration import Exploration

class TestCreateMap(unittest.TestCase):

    def test_explorationWakesUpPepper(self):
        "should wake up Pepper if it's still asleep."
        nav = mock.Mock()
        mot = mock.Mock()

        mot.robotIsWakeUp.return_value = False

        e = Exploration(nav, mot)
        e.createMap('FooMap', 2)

        mot.wakeUp.assert_called()

    def test_explorationDoesNotWakeUpPepperAgain(self):
        "should not call the wakup again if Pepper is still asleep."
        nav = mock.Mock()
        mot = mock.Mock()

        mot.robotIsWakeUp.return_value = False

        e = Exploration(nav, mot)
        e.createMap('FooMap', 2)

        mot.wakeUp.assert_called()
