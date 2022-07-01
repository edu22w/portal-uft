"""Portal settings tests."""
from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestPortalSettings(unittest.TestCase):
    """Test that Portal configuration is correctly done."""

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_portal_title(self):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Portal da UFT"
        self.assertEqual(value, expected)
