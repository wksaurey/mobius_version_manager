import unittest

from mvm import unpacker

get_build_name = unpacker.get_build_name


class TestUnpacker(unittest.TestCase):
    def test_get_build_name(self):
        filenames = [
            'Mining 4.2 rc5 45584',
            'MINING MOBIUS 24-10-18 Release 4.1.1 RC1 Mobius Version 7.40.54645.43961',
            'MINING MOBIUS 24-08-15 Release 4.1 RC13 Mobius Version 7.39.54469.42812'
        ]
        test_build_infos = [
            {
                'market': 'mining',
                'version_number': '4.2',
                'build_type': 'rc',
                'build_number': '5',
                'build_id': '45584',
                'name': 'Mining 4.2 rc5 45584'
            },
            {
                'market': 'mining',
                'version_number': '4.1.1',
                'build_type': 'rc',
                'build_number': '1',
                'build_id': '43961',
                'name': 'Mining 4.1.1 rc1 43961'
            },
            {
                'market': 'mining',
                'version_number': '4.1',
                'build_type': 'rc',
                'build_number': '13',
                'build_id': '42812',
                'name': 'Mining 4.1 rc13 42812'
            }
        ]
        for index, filename in enumerate(filenames):
            # print(get_build_name(filename))
            test_build_info = test_build_infos[index]
            build_info = get_build_name(filename)
            for key in build_info:
                self.assertEqual(build_info[key], test_build_info[key])
