import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from Login.test_Login import Test_Login

if __name__ == "__main__":
    pytest.main()