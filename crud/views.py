
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from crud.models import Student

class StudentCreate (CreateView):
    model = Student
    template_name = "add.html"
    fields = "__all__"
    success_url = "list/"

class StudentListView (ListView):
    template_name = "student-list.html"
    model = Student
    def get_queryset(self):
        qs = Student.objects.all()
        return qs

class StudentUpdate(UpdateView):
    model = Student
    template_name = "add.html"
    fields = "__all__"
    success_url = "/list"

class StudentDelete(DeleteView):
    model = Student
    template_name = "confirm-delete.html"
    success_url = "/list"

