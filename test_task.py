import pytest


class TestList:
    @pytest.mark.parametrize("init,expected", [([1, 2], [1, 2, 3]), ([], [3]), ([3, 3], [3, 3, 3])])
    def test_append(self, init, expected):
        init.append(3)
        assert init == expected

    def test_remove(self):
        init = [1, 3, 3]
        init.remove(3)
        assert init == [1, 3]
        init.remove(3)
        assert init == [1]
        try:
            init.remove(3)
        except ValueError:
            pass
        assert init == [1]

    def test_count(self):
        init = [2, 3, 4, 3, 4, 2, 3, 1]
        assert init.count(2) == 2
        assert init.count(3) == 3
        assert init.count(1) == 1


class TestSet:
    @pytest.mark.parametrize("init,expected", [({1, 2}, {1, 2, 3}), (set(), {3}), ({3, 3}, {3})])
    def test_add(self, init, expected):
        init.add(3)
        assert init == expected

    def test_remove(self):
        init = {1, 3, 3}
        init.remove(3)
        assert init == {1}
        try:
            init.remove(3)
        except KeyError:
            pass
        assert init == {1}

    def test_operations(self):
        set1 = {1, 2, 3}
        set2 = {2, 3, 4}
        assert set1.union(set2) == {1, 2, 3, 4}
        assert set1.difference(set2) == {1}
        assert set1.intersection(set2) == {2, 3}