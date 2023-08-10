
from django.contrib import admin
from django.urls import path
from admins import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),





    
    path('',views.home,name=''),
    path('about', views.about),
    path('contact', views.contact),
    path('logout', LogoutView.as_view(template_name='logout.html')),
    
    path('afterlogin', views.afterlogin),
        path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
        path('admin-dashboard', views.admin_dashboard,name='admin-dashboard'),

        path('admin-view-customer', views.admin_view_customer,name='admin-view-customer'),
        path('update-customer/<int:pk>', views.update_customer,name='update-customer'),
        path('delete-customer/<int:pk>', views.delete_customer,name='delete-customer'),

        path('admin-category', views.admin_category,name='admin-category'),
        path('admin-view-category', views.admin_view_category,name='admin-view-category'),
        path('admin-add-category', views.admin_add_category,name='admin-add-category'),
        path('admin-update-category', views.admin_update_category,name='admin-update-category'),
        path('update-category/<int:pk>', views.update_category,name='update-category'),
        path('admin-delete-category', views.admin_delete_category,name='admin-delete-category'),
        path('delete-category/<int:pk>', views.delete_category,name='delete-category'),

        path('admin-policy', views.admin_policy,name='admin-policy'),
        path('admin-view-policy', views.admin_view_policy,name='admin-view-policy'),
        path('admin-add-policy', views.admin_add_policy,name='admin-add-policy'),
        path('admin-update-policy', views.admin_update_policy,name='admin-update-policy'),
        path('update-policy/<int:pk>', views.update_policy,name='update-policy'),
        path('admin-delete-policy', views.admin_delete_policy,name='admin-delete-policy'),
         path('delete-policy/<int:pk>/', views.delete_policy, name='delete-policy'),
        path('admin-view-policy-holder', views.admin_view_policy_holder,name='admin-view-policy-holder'),
        path('admin-view-approved-policy-holder', views.admin_view_approved_policy_holder,name='admin-view-approved-policy-holder'),
        path('approve-request/<int:pk>', views.approve_request,name='approve-request'),
        path('admin-view-disapproved-policy-holder', views.admin_view_disapproved_policy_holder,name='admin-view-disapproved-policy-holder'),
        path('reject-request/<int:pk>', views.disapprove_request,name='reject-request'),
        path('admin-view-waiting-policy-holder', views.admin_view_waiting_policy_holder,name='admin-view-waiting-policy-holder'),
    
        path('admin-question', views.admin_question,name='admin-question'),
        path('update-question/<int:pk>', views.update_question,name='update-question'),
]