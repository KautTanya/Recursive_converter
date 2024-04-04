"""Десяткове число у двійкове"""


def recursive_dec_to_bin_converter(n):
    """recursive_dec_to_bin_converter"""
    if n == 0:
        return ""
    else:
        result = n % 2
        result_str = str(recursive_dec_to_bin_converter(n//2)) + str(result)
        return result_str


print(recursive_dec_to_bin_converter(12))
