"""
Existing doctests don't work...
"""
def test():
    import doctest
    doctest.testfile("existing_doctests.txt", verbose=1)


if __name__ == "__main__":
    test()
