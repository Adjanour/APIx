from django.conf.urls import url
from EmployeeApp import views
from django.urls import path
from .views import departmentApi
from .views import employeeApi

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
    url(r'^department',views.departmentApi),
    path('departments/<int:id>', departmentApi, name='department_api'),

    url(r'^employee$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),

    url(r'^employee/SaveFile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)