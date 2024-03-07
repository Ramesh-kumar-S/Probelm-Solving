import pytest
from Add_Test import checkSDE

#Runnning me using "python -m pytest Test_Add.py" Command
def test_checkSDE():
    # return True
    assert checkSDE("SDE") == True

