from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('customer', views.customer,name='customer'),
    path('customersignup', views.customersignup,name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='adminlogin.html'),name='customerlogin'),
    path('customer-dashboard', views.customer_dashboard,name='customer-dashboard'),

    path('apply-policy', views.apply_policy,name='apply-policy'),
    path('apply/<int:pk>', views.apply,name='apply'),

    path('history', views.history,name='history'),
    
    path('ask-question', views.ask_question,name='ask-question'),
    path('question-history', views.question_history,name='question-history'),

    



    


]

