from django.shortcuts import render
from forms import UserForm

def index(request):
    c = {"welcome_msg":"WELCOME!"}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            c['saved'] = True
        else:
            c['error'] = True
    else:
        form = UserForm()
    c['form'] = form
    return render(request,'tunapanda/index.html',c)


