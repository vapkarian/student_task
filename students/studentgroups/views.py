from django.template.response import TemplateResponse
from django.http import Http404
from models import *

def group_list(request):
    lst = []
    groups = Group.objects.all()
    students = Student.objects.all()
    for g in groups:
        id = g.id
        title = g.title
        praepostor = g.praepostor
        count = 0
        for s in students:
            if s.group == g:
                count+=1
        lst.append({'id':id,'title':title,'count':count,'praepostor':praepostor})
    return TemplateResponse(request,'group_list.html',{'groups':lst})

def group_detail(request,pk):
    lst = []
    try:
        group = Group.objects.get(id=pk)
    except:
        raise Http404()
    students = Student.objects.all()
    for s in students:
        if s.group == group:
            lst.append({'id':s.id,'full_name':s.full_name,'birthday':s.birthday,
                        'student_number':s.student_number,
                        'last_action':s.history.all()[0]})
    return TemplateResponse(request,'group_detail.html',
                            {'group':group,'students':lst})
