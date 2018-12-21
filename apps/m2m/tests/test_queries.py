import pytest
from graphene.test import Client
from mixer.backend.django import mixer

from apps.m2m.schema import schema

pytestmark = pytest.mark.django_db


class TestQuery:
    def test_m2m(self, snapshot):
        group1 = mixer.blend('m2m.Group', name='G1')
        student = mixer.blend('m2m.Student')

        group1.students.add(student)

        client = Client(schema)

        pytest.set_trace()

        result = client.execute("""
            query {
              groups(students_In: [%s]) {
                id
              }
            }
        """ % student.id)

        assert 'errors' not in result
        snapshot.assert_match(result)
