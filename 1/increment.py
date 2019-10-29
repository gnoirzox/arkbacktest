from  unittest  import  TestCase


def increment_dictionary_values(d, i):
    copied_dict = dict(d)

    for  k, v  in  copied_dict.items():
        copied_dict[k] = v + i
    return  copied_dict


class TestIncrementDictionaryValues(TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)
