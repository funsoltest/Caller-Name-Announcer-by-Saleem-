import pytest
from drivers.driver_factory import create_driver


@pytest.fixture(scope="class")
def driver_setup(request):
    driver = create_driver()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def app_ready(driver_setup):
    print("\n--- App Ready For Test ---")
    return driver_setup
