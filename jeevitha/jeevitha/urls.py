from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns=[
             path('admin/',admin.site.urls),
             path('',views.calculate_BMI,name='home'),
             path('bmi/',views.calculate_BMI,name='bmi'),
            ]