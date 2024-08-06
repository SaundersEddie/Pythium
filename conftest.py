import pytest

@pytest.fixture
def setup():
    print("\n Setup Start \n")
    yield
    print("\n Setup Finish \n")

@pytest.fixture
def before():
    print("\n Before Start \n")
    yield
    print("\n Before Finish \n")

@pytest.fixture
def after():
    print("\n After Start \n")
    yield
    print("\n After Finish \n")