from django.urls import path
from .views import index, form_save, work_with_product

app_name = 'new_app'

urlpatterns = [
        path('',index, name='index'),
        path('form_save/', form_save, name='form_save'),
        path('work/', work_with_product,name = 'work_with_product')



]