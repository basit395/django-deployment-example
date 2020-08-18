from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from django.utils import timezone
from django.http import HttpResponseRedirect
import datetime
from datetime import timedelta
from django.shortcuts import redirect
from django.urls import reverse
import random
from django.contrib.auth.models import User
from .models import customer,opportunity,staff,suggestion,order,operationstatus,service
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.db.models import Count , Sum

from .forms import opportunityForm,customerForm,staffForm,suggestionForm,orderForm,serviceForm,opportunitycForm,orderoForm,orderdoubleForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# @permission_required('customer.can_view')
@login_required
def index(request):
    customerslist = customer.objects.all().order_by('-creationdate')

    context = {'customerslist':customerslist}
    return render(request, 'crmapp/index.html',context)

# @permission_required('customer.can_view')
@login_required
def customerslist(request):
    customerslist = customer.objects.all().order_by('-creationdate')

    context = {'customerslist':customerslist}
    return render(request, 'crmapp/index.html',context)


# @permission_required('opportunity.can_add')
def opportunitynew(request):
    if request.method=='POST':
        form = opportunityForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.salesman=request.user
            myform.save()
            return HttpResponseRedirect(reverse('opportunitylist'))
    else:
        form = opportunityForm()
    return render(request, 'crmapp/opportunity_form.html',{'form':form})

def opportunitycnew(request,pk):
    if request.method=='POST':
        form = opportunitycForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.salesman=request.user
            customer1 = get_object_or_404(customer,pk=pk)
            myform.customer=customer1
            myform.save()
            return HttpResponseRedirect(reverse('opportunitylist'))
    else:
        form = opportunitycForm()
    return render(request, 'crmapp/opportunity_form.html',{'form':form})

# @permission_required('customer.can_add')
@login_required
def customernew(request):

    if request.method=='POST':
        form = customerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.creator=request.user
            myform.save()
            return HttpResponseRedirect(reverse('customerslist'))
    else:
        form = customerForm()
    return render(request, 'crmapp/customer_form.html',{'form':form})


class customerUpdateView(UpdateView):
    redirect_field_name = 'repeatitapp/customer_detail.html'
    form_class = customerForm
    model = customer


def opportunitydetail(request,pk):
    opportunitynow = get_object_or_404(opportunity,pk=pk)
    opportunityorders = opportunitynow.opportunity_orders.all()
    mrcsum= opportunityorders.aggregate(Sum('mrc'))
    mrcsum1 = mrcsum['mrc__sum']

    context = {'opportunityorders':opportunityorders,'opportunitynow':opportunitynow,'mrcsum1':mrcsum1}
    return render(request, 'crmapp/opportunity_detail.html',context)

class opportunityUpdateView(UpdateView):
    redirect_field_name = 'repeatitapp/opportunity_detail.html'
    form_class = opportunityForm
    model = opportunity


class customerDetailView(DetailView):
    model = customer

# @permission_required('opportunity.can_change')
@login_required
def opportunitylist(request):
    opportunitylist = opportunity.objects.all().order_by('-creationdate')

    context = {'opportunitylist':opportunitylist}
    return render(request, 'crmapp/opportunitylist.html',context)

# @permission_required('staff.can_change')
@login_required
def stafflist(request):
    stafflist = User.objects.all()

    context = {'stafflist':stafflist}
    return render(request, 'crmapp/stafflist.html',context)


class CreatestaffView(CreateView):
    redirect_field_name = 'crmapp/staff_detail.html'
    form_class = staffForm
    model = staff


class staffDetailView(DetailView):
    model = staff

# @permission_required('suggestion.can_change')
@login_required
def suggestionlist(request):
    suggestionlist = suggestion.objects.all()
    context = {'suggestionlist':suggestionlist}
    return render(request, 'crmapp/suggestionlist.html',context)

class suggestionUpdateView(UpdateView):
    redirect_field_name = 'repeatitapp/suggestion_detail.html'
    form_class = suggestionForm
    model = suggestion

def suggestionnew(request):
    if request.method=='POST':
        form = suggestionForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.requestor=request.user
            myform.save()
            return HttpResponseRedirect(reverse('suggestion'))
    else:
        form = suggestionForm()
    return render(request, 'crmapp/suggestion_form.html',{'form':form})

class suggestionDetailView(DetailView):
    model = suggestion

#Orders


# @permission_required('order.can_change')
@login_required
def orderpostlist(request):
    post = get_object_or_404(operationstatus,pk=8)
    orderpostlist = order.objects.all().filter(status=post).order_by('-creationdate')
    context = {'orderpostlist':orderpostlist}
    return render(request, 'crmapp/orderpostlist.html',context)

# @permission_required('order.can_add')
@login_required
def orderlist(request):
    orderlist = order.objects.all().order_by('-creationdate')
    context = {'orderlist':orderlist}
    return render(request, 'crmapp/orderlist.html',context)


# class CreateorderView(CreateView):
#     redirect_field_name = 'crmapp/order_detail.html'
#     form_class = orderForm
#     model = order

@login_required
def ordernew(request):

    if request.method=='POST':
        form = orderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            oppstatus = get_object_or_404(opportunity,opportunityno=form.cleaned_data['opportunity'].opportunityno )
            print(oppstatus.status)
            if str(oppstatus.status) == 'Document':
                myform = form.save(commit=False)
                myform.operationexecutive=request.user
                myform.save()
                return HttpResponseRedirect(reverse('order'))
            else:
                return render(request, 'crmapp/noorder.html')
    else:
        form = orderForm()
    return render(request, 'crmapp/order_form.html',{'form':form})

#order from opportunity Detail
def orderonew(request,pk):
    if request.method=='POST':
        form = orderoForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.operationexecutive=request.user
            opportunity1 = get_object_or_404(opportunity,pk=pk)
            myform.opportunity=opportunity1
            myform.save()
            return HttpResponseRedirect(reverse('order'))
    else:
        form = orderoForm()
    return render(request, 'crmapp/order_form.html',{'form':form})

#order from order Detail
def orderdouble(request,pk,pk1):
    if request.method=='POST':
        form = orderdoubleForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.operationexecutive=request.user
            opportunity1 = get_object_or_404(opportunity,pk=pk)
            order1 = get_object_or_404(order,pk=pk1)
            myform.opportunity=opportunity1
            myform.accountno=order1.accountno
            myform.service=order1.service
            myform.save()
            return HttpResponseRedirect(reverse('order'))
    else:
        form = orderoForm()
    return render(request, 'crmapp/order_form.html',{'form':form})


class orderDetailView(DetailView):
    model = order

#service start
# @permission_required('service.can_change')
@login_required
def servicelist(request):
    servicelist = service.objects.all().order_by('servicecategory')
    context = {'servicelist':servicelist}
    return render(request, 'crmapp/servicelist.html',context)

class CreateserviceView(CreateView):
    redirect_field_name = 'crmapp/servicelist.html'
    form_class = serviceForm
    model = service

class serviceDetailView(DetailView):
    model = service

#service end

class orderUpdateView(UpdateView):
    redirect_field_name = 'repeatitapp/order_detail.html'
    form_class = orderForm
    model = order

# @permission_required('order.can_change')
@login_required
def changetopost(request,pk):
    orderpost = get_object_or_404(order,pk=pk)
    post = get_object_or_404(operationstatus,pk=8)
    orderpost.status = post
    orderpost.save()
    orderlist = order.objects.all().order_by('-creationdate')
    context = {'orderlist':orderlist}
    return render(request, 'crmapp/orderlist.html',context)

# @permission_required('order.can_change')
@login_required
def cancelorder(request,pk):
    ordernow = get_object_or_404(order,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=7)
    ordernow.status = statusnow
    ordernow.save()
    orderlist = order.objects.all().order_by('-creationdate')
    context = {'orderlist':orderlist}
    return render(request, 'crmapp/orderlist.html',context)

# @permission_required('order.can_change')
@login_required
def openorder(request,pk):
    ordernow = get_object_or_404(order,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=5)
    ordernow.status = statusnow
    ordernow.save()
    orderlist = order.objects.all().order_by('-creationdate')
    context = {'orderlist':orderlist}
    return render(request, 'crmapp/orderlist.html',context)

# @permission_required('order.can_change')
@login_required
def heldorder(request,pk):
    ordernow = get_object_or_404(order,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=6)
    ordernow.status = statusnow
    ordernow.save()
    orderlist = order.objects.all().order_by('-creationdate')
    context = {'orderlist':orderlist}
    return render(request, 'crmapp/orderlist.html',context)

@login_required
def proposalopp(request,pk):
    oppnow = get_object_or_404(opportunity,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=2)
    oppnow.status = statusnow
    oppnow.save()
    opportunitylist = opportunity.objects.all().order_by('-creationdate')
    context = {'opportunitylist':opportunitylist}
    return render(request, 'crmapp/opportunitylist.html',context)

@login_required
def negotiationopp(request,pk):
    oppnow = get_object_or_404(opportunity,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=1)
    oppnow.status = statusnow
    oppnow.save()
    opportunitylist = opportunity.objects.all().order_by('-creationdate')
    context = {'opportunitylist':opportunitylist}
    return render(request, 'crmapp/opportunitylist.html',context)


@login_required
def documentopp(request,pk):
    oppnow = get_object_or_404(opportunity,pk=pk)
    statusnow = get_object_or_404(operationstatus,pk=3)
    opportunitylist = opportunity.objects.all().order_by('-creationdate')
    oppnow.status = statusnow
    oppnow.save()
    context = {'opportunitylist':opportunitylist}
    return render(request, 'crmapp/opportunitylist.html',context)

@login_required
def completedsugg(request,pk):
    suggnow = get_object_or_404(suggestion,pk=pk)
    suggnow.completion = True
    suggnow.save()
    context = {'suggnow':suggnow}
    return render(request, 'crmapp/suggestionlist.html',context)
