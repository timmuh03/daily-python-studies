import pytest
from .solution import Solution


@pytest.mark.parametrize("password, expected", [
    ("IloveLe3tcode!",
     True),
    
    ("Me+You--IsMyDream",
    False),
    
    ("1aB",
     False),
    
    ("a1A!A!A!",
     True),
    
    ("$!)+-$-^(@)@#-(#)+@#*&%+*%($^%+)#()&)!)*()-+&$*@*)+%+*^!%!&!$#%-*!@&%!)%+()^$&+-",
     False)
])

def test_strong_password_checker_II(password, expected):
    result = Solution().strongPasswordCheckerII(password)
    assert result == expected, f"Failed on password:{password}, expected:{expected}, result:{result}"