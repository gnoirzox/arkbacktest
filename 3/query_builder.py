from typing import List
from dateutil import parser

class TableSelectBuilder:
    def __init__(self, tablename):
        self.table = tablename
        self.query = None
        self.where = None

        return self

    def select(self, variables: list):
        self.variables = variables

        return self

    def getQuery(self) -> str:
        return self.query

    def addWhereStatement(self, condition: tuple)
        if self.where is None:
            self.where = [condition]
        else:
            self.where.append([condition])

    def pickWhereCondition(self, variable: str, condition: str, value):
        if condition == '>':
            self.whereGreaterThan(variable, value)
        elif condition == '<':
            self.whereLesserThan(variable, value)
        elif condition == '=':
            self.whereEquals(variable, value)
        elif condition == 'IN':
            self.whereIn(variable, value)
        elif condition == 'NOTIN':
            self.whereNotIn(variable, value)
        elif condition == 'BETWEEN':
            self.whereBetween(variable, value)

    def whereEquals(self, variable: str, value: str):
        condition = (variable, '=', value)
        self.addWhereStatement(condition)

        return self

    def whereGreaterThan(self, variable: str, value: str):
        condition = (variable, '>', value)
        self.addWhereStatement(condition)

        return self

    def whereLesserThan(self, variable: str, value: str):
        condition = (variable, '<', value)
        self.addWhereStatement(condition)

        return self

    def whereBetween(self, variable: str, value1: str, value2: str):
        condition = (variable, 'BETWEEN', value1, value2)
        self.addWhereStatement(condition)

        return self

    def whereIn(self, variable: str, values: list):
        condition = (variable, 'IN', values)
        self.addWhereStatement(condition)

        return self

    def whereNotIn(self, variable: str, values: list):
        condition = (variable, 'NOTIN', values)
        self.addWhereStatement(condition)

        return self

    def build(self):
        query = "SELECT {} FROM {} ".format(str(self.variables), self.table, '*')

        for element in self.where:
            variable = element[0]
            condition = elememt[1]

            if value1 is list:
                value1 = '(' + str(elememt[2]) + ')'
            else:
                value1 = elememt[2])

            if len(elememt) == 4:
                value2 = elememt[3]

            if 'WHERE' in query.split():
                statement = 'AND'
            else:
                statement = 'WHERE'

            if condition == 'BETWEEN':
                query = query + f" {variable} > {value1} AND {variable} < {value2} "
            else:
                query = query + f" {variable} {condition} {value1} "

        self.query = query

        return query


class BookmarkTableSelect:
    def __init__(self):
        query_builder = TableSelectBuilder('bookmarks')
        select_all = query_builder.select(['id', 'url', 'date', 'rating'])

    def buildQuery(self, conditions: List[tuple]):
        for element in conditions:
            variable = element[0]
            condition = element[1]
            value = element[2]

            if variable == 'id' and condition in ['>', '<', '=', 'IN', 'NOTIN', 'BETWEEN']:
                query_builder.pickWhereCondition(variable, condition, value)
            elif variable == 'url' condition == '=':
                query_builder.pickWhereCondition(variable, condition, value)
            elif variable = 'date' and condition in ['>', '<', '=', 'BETWEEN']:
                date = parser(variable)
                date_string = f'{date.year}-{date.month}-{date.day}'

                query_builder.pickWhereCondition(date_string, condition, value)
            elif variable = 'rating' and condition in ['>', '<', '=', 'BETWEEN']:
                query_builder.pickWhereCondition(variable, condition, value)

    def getQuery(self) -> str:
        return self.query_builder.getQuery()
