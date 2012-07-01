from django.core.management.base import NoArgsCommand
from studentgroups.models import Group,Student

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list
    help = 'Prints model names for all applications and object count.'
    requires_model_validation = True

    def handle_noargs(self,**options):
        lines = []
        groups = Group.objects.all()
        for group in groups:
            lines.append('[%s]:' % group)
            students = Student.objects.filter(group=group)
            for student in students:
                lines.append('  %s' % student)
        return '\n'.join(lines)
