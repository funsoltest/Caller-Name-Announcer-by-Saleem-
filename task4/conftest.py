import pytest
from drivers.driver_factory import create_driver

@pytest.fixture(scope="session")
def session_setup():
    print("\n=== Appium Session Started ===")
    yield
    print("\n=== Appium Session Ended ===")

@pytest.fixture(scope="class")
def driver_setup(request, session_setup):
    driver = create_driver()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="function")
def app_ready():
    print("\n--- App Ready For Test ---")
    yield
    print("\n--- Test Completed ---")
