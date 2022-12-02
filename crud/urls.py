from django.urls import path
from crud.views import StudentCreate , StudentListView , StudentUpdate , StudentDelete

urlpatterns = [
    path ("", StudentCreate.as_view()),
    path ("list/", StudentListView.as_view()),
    path ("update/<pk>/", StudentUpdate.as_view()),
    path ("delete/<pk>/" , StudentDelete.as_view())

]
