
from django.urls import path
from EEE import views


app_name = "EEE"


from EEE.views import StudentReg


urlpatterns = [
    path('home', views.home, name = "home"),
    path('products', views.products, name = "products"),
    path('service', views.service, name = "service"),
    path('aboutus', views.aboutus, name = "aboutus"),
    path('contactus', views.contactus, name = "contactus"),

    path('studentreg', StudentReg.as_view(), name = 'studentreg'),

# for class based views
     path('student',views.student, name = 'student'),
    path('form', views.form,name  = 'form'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/form', views.update, name = 'update'),

    path('',views.rit, name = ''),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),


# for templates eee

    path('about', views.about, name = 'about'),
    path('blog_single', views.blog_single, name = 'blog_single'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('index', views.index, name = 'index'),
    path('portfolio', views.portfolio, name = 'portfolio'),  

   #for user login and log out
   path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
 
]
