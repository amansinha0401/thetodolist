from django.shortcuts import render,redirect
from myapp.models import emp
# Create your views here.

def index(request):
    emps=emp.objects.all()
    context={
        "emp":emps,
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':  # Use 'POST' in uppercase
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emps = emp(
            Name=name,
            email=email,
            adderess=address,
            phone=phone
        )
        emps.save()
        return redirect("index")  

    return render(request, 'index.html')

# views.py
def edit(request):
    emps = emp.objects.all()
    context = {
        "emp": emps,
    }
    return render(request, 'index.html', context)

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Retrieve the employee by ID
        emps = emp.objects.get(id=id)
        emps.Name = name
        emps.email = email
        emps.address = address  # Corrected attribute name
        emps.phone = phone
        emps.save()

        return redirect("index")

    return redirect("index")

def delete(request, id):
    
        # Get the employee by ID and delete it
        emp.objects.filter(id=id).delete()

        # Redirect to the 'index' page after deletion
        return redirect("index")


      