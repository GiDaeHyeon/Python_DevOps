import pytestfrom my_module import string2booltrue_values = ['yes', '1', 'Yes', 'True', 'TRUE', 'true', 'Yeah~']class TestStrToBool(object):    @pytest.mark.parametrize('value', true_values)    def test_if_detects_truish_strings(self, value):        assert string2bool(value)