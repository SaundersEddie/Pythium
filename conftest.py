import pytest

@pytest.fixture
def setup():
    print("\nSetup before test EXTERNAL FIXTURE\n")
    yield
    print("\nTear down after test")

@pytest.fixture
def before():
    print("\nBefore test EXTERNAL FIXTURE \n")
    yield
    print("\nAfter test")