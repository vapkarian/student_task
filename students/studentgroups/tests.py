import unittest
from studentgroups.models import Group, Student
from django.test.client import Client


class GroupTestCase(unittest.TestCase):
    def test(self):
        client = Client()
        client.login(username='Admin', password='Gfhjkm')
        print 'Success login'
        g = Group(title='TestGroup')
        g.save()
        s = Student(full_name='Tester',group=g)
        s.save()
        print 'Student %s created in group %s' % (s,g)
        client.logout()
        print 'Success logout'
