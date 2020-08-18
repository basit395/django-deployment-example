from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('home/', views.index, name='home'),

    path('customers/', views.customerslist, name='customerslist'),
    path('customer/new/', views.customernew, name='customernew'),
    path('customer/<pk>/', views.customerDetailView.as_view(), name='customerdetail'),
    path('customer/update/<pk>/', views.customerUpdateView.as_view(), name='customerupdate'),

    path('opportunity/new/', views.opportunitynew, name='newopportunity'),
    path('opportunityc/new/<pk>', views.opportunitycnew, name='newopportunityc'),
    path('opportunity/<pk>/', views.opportunitydetail, name='opportunitydetail'),
    path('opportunity/', views.opportunitylist, name='opportunitylist'),
    path('opportunity/update/<pk>/', views.opportunityUpdateView.as_view(), name='opportunityupdate'),
    path('opportunity/proposal/<pk>/', views.proposalopp, name='proposal'),
    path('opportunity/document/<pk>/', views.documentopp, name='document'),
    path('opportunity/negotiation/<pk>/', views.negotiationopp, name='negotiation'),

    path('staff/', views.stafflist, name='stafflist'),
    path('staff/new/', views.CreatestaffView.as_view(), name='staffnew'),
    path('staff/<pk>/', views.staffDetailView.as_view(), name='staffdetail'),

    path('suggestion/', views.suggestionlist, name='suggestion'),
    path('suggestion/new/', views.suggestionnew, name='suggestionnew'),
    path('suggestion/<pk>/', views.suggestionDetailView.as_view(), name='suggestiondetail'),
    path('suggestion/update/<pk>/', views.suggestionUpdateView.as_view(), name='suggestionupdate'),
    path('suggestion/completion/<pk>/', views.completedsugg, name='completed'),

    path('order/', views.orderlist, name='order'),
    path('order/post/', views.orderpostlist, name='orderpost'),
    path('order/new/', views.ordernew, name='ordernew'),
    path('order/<pk>/', views.orderDetailView.as_view(), name='orderdetail'),
    path('order/update/<pk>/', views.orderUpdateView.as_view(), name='orderupdate'),
    path('order/changetopost/<pk>/', views.changetopost, name='changetopost'),
    path('order/cancel/<pk>/', views.cancelorder, name='cancel'),
    path('order/open/<pk>/', views.openorder, name='open'),
    path('order/held/<pk>/', views.heldorder, name='held'),
    path('ordero/new/<pk>', views.orderonew, name='newordero'),
    path('orderdouble/new/<pk>/<pk1>', views.orderdouble, name='orderdouble'),
    #
    path('service/', views.servicelist, name='servicelist'),
    path('service/new/', views.CreateserviceView.as_view(), name='servicenew'),
    path('service/<pk>/', views.serviceDetailView.as_view(), name='servicedetail'),



    ]
