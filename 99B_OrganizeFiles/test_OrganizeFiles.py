#!/usr/bin/env python3

# import standard lib
import sys
from pdb import set_trace
from unittest import main, TestCase

# import custom lib
import OrganizeFiles

class OrganizeFilesTestCase(TestCase):
    def test_get_target_dir(self):
        checks = {
            ('test.exe',):'Apps',
            ('test.abcd',):'Unknown',
        }
        for names, target_dir in checks.items():
            for name in names:
                result = OrganizeFiles.get_target_dir(name)
                msg = 'Failed to check ' + name
                self.assertEqual(result, target_dir, msg)

if __name__ == '__main__':
    result = main()
    sys.exit(result)
