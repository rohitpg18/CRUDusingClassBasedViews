from django.urls import path
from crud.views import StudentCreate , StudentListView , StudentUpdate ,StudentDelete , simple_upload

urlpatterns = [
    path ("", StudentCreate.as_view()),
    path ("list/", StudentListView.as_view(), name = "list"),
    path ("update/<pk>/", StudentUpdate.as_view()),
    path ("delete/<pk>/" , StudentDelete.as_view()),
    path ("upload/", simple_upload)

]
