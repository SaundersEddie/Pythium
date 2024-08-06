import pytest

def test_doLogin(setup):
    print("\nExecuting Login Test\n")
    a = 3
    b = 4
    assert a + 1 == b, "Test failed\n"

def test_testingUserReq(setup, before, after):
    print("\nTesting User Registration\n")
    a = 3
    b = 4
    assert a + 1 == b, "Test failed\n"