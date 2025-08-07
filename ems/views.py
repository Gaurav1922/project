from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Record
from django.contrib import messages
from django.db.models import Q
from .forms import SearchForm
from django.core.paginator import Paginator

"""
@login_required(login_url='my-login')
def department_filter(request):
    department = request.GET.get('department')
    employees = Record.objects.none()

    if department:
        employees = Record.filter(department__iexact=department)

    context = {
        'department': department,
        'employees': employees,
    }

    return render(request,'department_filter.html', context)
"""

"""@login_required(login_url='my-login')
def it_employees_view(request, id):
    form = DepartmentFilterForm(request.GET)
    record = Record.objects.all()
    record = Record.objects.get(id=id)

    if form.is_valid():
        department = form.cleaned_data.get('department')
        if department:
            record = Record.filter=Q(department__iexact=department)
        else:
            record = Record.objects.all()
    employees = Record.objects.filter(department_name__iexact='IT')

    context={
        'form':form,
        'record':record,
        'employees': employees,
    }
    return render(request,'ems/it_employees.html', context)"""


# search 

@login_required(login_url='my-login')
def search_employees(request):
    form = SearchForm(request.GET)
    query = None
    results = []
    employees = []
    count = 0
    if form.is_valid():
        query = form.cleaned_data['query']
    
        results = Record.objects.filter(Q(designation__icontains=query) | Q(name__icontains=query) | Q(emp_id__icontains=query) | Q(address__icontains=query) | Q(department__icontains=query)
        )
        count = results.count()
    
    context = {
        'form': form,
        'query': query,
        'results': results,
        'employees': employees,
        'count' : count,
    }
    return render(request, 'ems/search_employees.html', context)

#- Home 

def home(request):
    
    return render(request, 'ems/index.html')


#- REgister

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully registered")
            return redirect("my-login")
    
    context = {'form':form}

    return render(request,'ems/register.html', context=context)

# Login a user

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    context = {'form':form}

    return render(request, 'ems/my-login.html', context=context)      

# Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()
    # set up pagination 
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get('page')
    records = p.get_page(page)

    context = {
        'my_records': my_records,
        'records': records,
        }

    return render(request, 'ems/dashboard.html', context=context)


# Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record was created")
            return redirect("dashboard")
    

    

    context = {'form': form}

    return render(request, 'ems/create-record.html',context=context)


# update a record

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Record was updated successfully")
            return redirect("dashboard")
    
    context = {'form':form}

    return render(request, 'ems/update-record.html', context=context)

# Read/ view a singular record

@login_required(login_url='my-login')
def single_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request,'ems/view-record.html', context=context)

# Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()
    messages.success(request, "Record was deleted successfully")
    return redirect("dashboard")

# Count 

@login_required(login_url='my-login')
def employee_count_record(request):
    total_employees = Record.objects.count()
    context = {
        'total_employees': total_employees,
        }

    return render(request,'ems/employee_count.html', context)

# Search 
"""
@login_required(login_url='my-login')
def dashboard_view(request):
    form = EmployeeSearchForm(request.GET or None)
    results = Record.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_field')
        if search_query:
            results = results.filter(
            Q(emp_id__icontains=search_query) | 
            Q(name__icontains=search_query) |  
            Q(designation__icontains=search_query) |
            Q(city__icontains=search_query)
        )

    context = {
        'form':form,
        'results': results,
    }
    return render(request,'ems/search_results.html', context)
"""
# Department

@login_required(login_url='my-login')
def department(request):
    return render(request,'ems/department.html' )


# Employee 

@login_required(login_url='my_login')
def employee(request):
    total_employees = Record.objects.count()

    context = {
        'total_employees': total_employees
        }

    return render(request,'ems/employee.html', context)

"""
# Search by department

@login_required(login_url='my-login')
def department_count(request):
    employees = Record.objects.filter(department=department)
    context= {
        'employees': employees,

    }
    return render(request, 'ems/department_count.html', context)
"""




















# LOGOUT

def user_logout(request):

    auth.logout(request)
    messages.success(request, "Logout success")
    return redirect("my-login")
