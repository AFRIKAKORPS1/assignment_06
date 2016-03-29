import random
import unittest
from ..point import Point


class TestFunctionalPointPattern(unittest.TestCase):
    def test_set_point(self):
        testPoint=Point(1,4)
        self.assertTrue(testPoint.x==1 and testPoint.y==4)
       
    def test_coincidence(self):
        testPoint=Point(1,4)
        self.assertTrue(testPoint.check_if_coincident((1,4)))
    
    def test_shift(self):
        testPoint=Point(1,4)
        shift_x=10
        shift_y=10
        testPoint.shift_point(shift_x,shift_y)
        self.assertEqual((testPoint.x,testPoint.y),(11,14))
    
    def test_marked(self):
        mark_list=['earth', 'wind', 'fire', 'heart']
        point_list=[]
        earth_count=0
        wind_count=0
        fire_count=0
        heart_count=0
        random.seed(43523)
        for i in range(1,20):
            curr_choice=random.choice(mark_list)
            point_list.append(Point(1,1,curr_choice))      
            if(curr_choice=='earth'):
                earth_count+=1
            elif(curr_choice=='wind'):
                wind_count+=1
            elif(curr_choice=='fire'):
                fire_count+=1
            else:
                heart_count+=1
        earth_count_check=0
        wind_count_check=0
        fire_count_check=0
        heart_count_check=0
        
        for i in range(1,20):
            curr_mark=point_list.pop().mark
            if(curr_mark=='earth'):
                earth_count_check+=1
            elif(curr_mark=='wind'):
                wind_count_check+=1
            elif(curr_mark=='fire'):
                fire_count_check+=1
            elif(curr_mark=='heart'):
                heart_count_check+=1
        
        self.assertEqual(earth_count,earth_count_check)
        self.assertEqual(wind_count, wind_count_check)
        self.assertEqual(fire_count, fire_count_check)
        self.assertEqual(heart_count, heart_count_check)
        
