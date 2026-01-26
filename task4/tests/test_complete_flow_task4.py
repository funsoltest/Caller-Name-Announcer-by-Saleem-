import pytest
from pages.language_page import LanguagePage
from pages.permission_page import PermissionPage
from pages.dialer_page import DialerPage


@pytest.mark.usefixtures("driver_setup")
class TestCompleteAppFlow:

    def test_full_flow(self, app_ready):
        lang = LanguagePage(self.driver)
        perm = PermissionPage(self.driver)
        dialer = DialerPage(self.driver)

        # ---------------- Language ----------------
        lang.select_english()
        lang.click_done()
        lang.handle_onboarding_and_premium()   # ✅ UPDATED METHOD

        # ---------------- Permissions ----------------
        perm.allow_access()
        perm.system_allow()

        # ---------------- Dialer ----------------
        dialer.open_dialer()
        dialer.dial_numbers(['0', '1', '2', '3'])
        dialer.press_call()
