def check(test_str):
    import re
    pattern = r'[^\.a-z0-9]'
    if re.search(pattern, test_str):
        print ('Invalid : %r' % (test_str,))
    else:
        print ('Valid   : %r' % (test_str,))

check(test_str='abcde.1')
check(test_str='abcde.1#')
check(test_str='ABCDE.12')
check(test_str='_-/>"!@#12345abcde<')