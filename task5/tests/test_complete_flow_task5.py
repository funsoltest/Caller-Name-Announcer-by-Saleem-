import time
import pytest
from pages.language_page import LanguagePage
from pages.permission_page import PermissionPage
from pages.dialer_page import DialerPage

class TestCompleteAppFlow:

    def test_full_flow(self, app_ready):
        driver = app_ready
        lang = LanguagePage(driver)
        perm = PermissionPage(driver)
        dialer = DialerPage(driver)

        print("\n--- Language Flow ---")
        lang.complete_language_flow()

        print("\n--- Permission Flow ---")
        perm.handle_permissions()

        print("\n--- Dialer Flow ---")
        time.sleep(2)  # wait for home screen to fully load
        dialer.open_dialer()
