import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from Login.test_Login import Test_Login
from Swag_Labs.test_swag_labs import Test_Swag

if __name__ == "__main__":
    pytest.main()