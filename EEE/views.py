from django.shortcuts import render

from django.contrib.auth.decorators import login_required 



# Create your views here.

def home(request):
    stu = "kayal"
    names = ['karthick', 'raju', 'praveen']
    context = {'stu': stu, 'names': names}

    return render(request, 'home.html', context)

def products(request):
    return render(request, 'products.html')

def service(request):
    return render(request, 'service.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def about(request):
    return render(request, 'EEE/about.html')

def blog_single(request):
    return render(request, 'EEE/blog-single.html')

def blog(request):
    return render(request, 'EEE/blog.html')

@login_required(login_url = 'EEE:login')
def contact(request):
    return render(request, 'EEE/contact.html')

def index(request):
    return render(request, 'EEE/index.html')

def portfolio(request):
    return render(request, 'EEE/portfolio.html')

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from EEE.models import Student
 
class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

from django.shortcuts import render, redirect, get_object_or_404

from .models import Student
from .forms import StudentForm

def student(request):
    stu = Student.objects.all()
    context = {'stu': stu}
    return render(request, 'student.html', context)


def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'detail.html', context)


def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('EEE:form')

	context = {'form':form, 'data':data}
	return render(request,'update.html', context )


def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('EEE:form')
	return render(request,'delete.html', context )


def form(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EEE:student')  

    context = {'stu': stu, 'form': form}
    return render(request, 'form.html', context)

def rit(request):
	return render(request,'rit.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a*b
	context = {'c': c }
	return render(request,'get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a*b
	context = {'c': c }
	return render(request,'post.html',context)
from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# # from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages 
# #from django.contrib import authenticate, login, logout
# from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.decorators import login_required 


# def register(request):
	
# 	form = CreateUserForm()

# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			user = form.cleaned_data.get('username')
# 			messages.success(request, 'Your Account has been created for '+ user)
# 			return redirect('EEE:login')


# 	context = { 'form': form }
# 	return render (request, 'register.html', context)


# def login_reg(request):

# 	if request.method =='POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		user = authenticate(request, username = username, password = password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect('EEE:home')
# 		else:
# 			messages.info(request, "Username Or password is incorrect.")
# 	context = {}
# 	return render (request, 'login.html', context)

# def logoutuser(request):
# 	logout(request)
# 	return redirect('EEE:login')





# re-workfrom django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 







def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('EEE:login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('EEE:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('EEE:login')
