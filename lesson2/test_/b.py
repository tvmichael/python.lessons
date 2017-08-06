import itertools

def rle(iterable):
    '''Applise run-length ...'''
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)

def test_rle():
    print(list(rle('mississippi')))

def test_assert_rle():
    s = 'mississippi'
    tmp = set(ch for ch, _count in rle(s))
    print(tmp)
    assert tmp == set(s[:-1] + s[1])
    print(set(s[:-1] + s[1]))
    assert not list(rle(''))


test_assert_rle()