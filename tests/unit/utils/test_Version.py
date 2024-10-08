from unittest import TestCase

from osbot_utils.utils.Files import file_name, folder_name, parent_folder

import osbot_serverless_flows
from osbot_serverless_flows.utils.Version import Version, version__osbot_serverless_flows


class test_Version(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.version = Version()

    def test_path_code_root(self):
        assert self.version.path_code_root() == osbot_serverless_flows.path

    def test_path_version_file(self):
        with self.version as _:
            assert parent_folder(_.path_version_file()) == osbot_serverless_flows.path
            assert file_name    (_.path_version_file()) == 'version'

    def test_value(self):
        assert self.version.value() == version__osbot_serverless_flows