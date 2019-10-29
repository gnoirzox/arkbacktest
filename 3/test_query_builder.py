from unittest import TestCase
from query_builder import TableSelectBuilder


class TestQueryBuilder(TestCase):
    def test_query_builder(self):
        self.assertEqual(
            TableSelectBuilder('bookmarks').select(['id', 'url', 'date', 'rating'])\
                .whereEquals('url', 'http://hello.world').whereIn('id', [13, 42, 8, 7])\
                .whereBetween('date', '2016-01-01', '2019-01-01').whereGreaterThan('rating', 3).build(),
            "SELECT id, url, date, rating FROM bookmarks WHERE url = 'http://hello.world' "
            "AND id IN (13, 42, 8, 7) AND date > '2016-01-01' AND date < '2019-01-01' "
            "AND rating > 3")
