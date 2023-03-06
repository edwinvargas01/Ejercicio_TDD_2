import math
from function_f_small import find_Num

def test_is_smallest():
    assert find_Num([5,7,4,3.8])==3.8;
    assert find_Num([10,math.sqrt(16),math.pow(2,6),math.factorial(9)])==4.0;
    assert find_Num([abs(-18),-23,-15,0])==-23;
    assert find_Num([7,1,0,2])==0;
    
