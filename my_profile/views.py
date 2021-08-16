from django.shortcuts import render

def index(request):
    context= {'name': 'SHREY VERMA', 'about':'SOFTWARE DEVELOPER & GRAPHIC EDITING'}
    return render(request, "index.html",  context)

def about(request):
    context = {'name': 'SHREY VERMA', 'skills': ['Python','C++','MySQL','Django'], 'user_id':'shreyv67',
               'email':'shreyv67@gmail.com', 'about':'SOFTWARE DEVELOPER & GRAPHIC EDITING', 'phone': '9839857801', 'profession': 'Software Developer'}
    return render(request, "about.html", context)