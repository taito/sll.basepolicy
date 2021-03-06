from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from sll.basepolicy.tests.base import IntegrationTestCase
from zope.component import getUtility

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_set_record_abita_development_rate(self):
        registry = getUtility(IRegistry)
        registry['abita.development.rate'] = 2.0
        self.assertEqual(registry['abita.development.rate'], 2.0)

        from sll.basepolicy.upgrades import set_record_abita_development_rate
        set_record_abita_development_rate(5.0)

        self.assertEqual(registry['abita.development.rate'], 5.0)

    def test_install_packages__one_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.development'])
        self.assertFalse(installer.isProductInstalled('abita.development'))

        from sll.basepolicy.upgrades import install_packages
        install_packages(self.portal, 'abita.development')

        self.assertTrue(installer.isProductInstalled('abita.development'))

    def test_install_packages__two_packages(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['abita.development', 'hexagonit.socialbutton'])
        self.assertFalse(installer.isProductInstalled('abita.development'))
        self.assertFalse(installer.isProductInstalled('hexagonit.socialbutton'))

        from sll.basepolicy.upgrades import install_packages
        install_packages(self.portal, ['abita.development', 'hexagonit.socialbutton'])

        self.assertTrue(installer.isProductInstalled('abita.development'))
        self.assertTrue(installer.isProductInstalled('hexagonit.socialbutton'))

    @mock.patch('sll.basepolicy.upgrades.install_packages')
    def test_install_sll_basepolicy(self, install_packages):
        from sll.basepolicy.upgrades import install_sll_basepolicy
        install_sll_basepolicy(self.portal)
        install_packages.assert_called_with(self.portal, 'sll.basepolicy')

    def test_reimport_registry(self):
        from sll.basepolicy.upgrades import reimport_registry
        setup = mock.Mock()
        reimport_registry(setup)
        setup.runImportStepFromProfile.assert_called_with(
            'profile-sll.basepolicy:default', 'plone.app.registry', run_dependencies=False, purge_old=False)
