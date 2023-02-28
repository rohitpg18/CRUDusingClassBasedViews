
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from crud.models import Student
from .resources import StudentResources
from tablib import Dataset
from django.shortcuts import render, redirect

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

def simple_upload (request):
    if request.method == 'POST':
        student_resource = StudentResources()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        return redirect ("list")
    return render (request, 'upload.html')

from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from crud.models import Student


class LoginView(View):

    template_name = 'login.html'
    form_class = AuthenticationForm
    student_list = Student.objects.all()

    # def get(self, request):

    #     form = self.form_class()
    #     context = {
    #         'form' : form
    #     }
    #     return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('list')
        
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)


def LogoutView(request):
    logout(request)
    return redirect('LoginView')

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         print('Hello')
#         return redirect('HomeView')






