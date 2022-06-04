from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def index(request):
    form = PersonForm()

    context = {
        'form':form,

    }
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
            }
            return render(request, 'index.html', context)
        # в этом случае else возвращает в контекст ошибку и сохраненную форму
    return render(request, 'index.html', context)

def new_person(request):

    return render(request, 'index.html')

def form_save(request):
    if request.method == 'POST':

        title = request.POST.get('login')
        name = request.POST.get('name')
        password = request.POST.get('password')
        avatar = request.POST.get('avatar')

        print(title,name)
        for i in Person.objects.all():
            if title == i.login:
                err1 = 'login уже занят'
                return render(request, 'index.html', {'err1': err1})
        

        if Person.objects.create(nik_name=name,login=title, password=password,avatar=avatar):
            return redirect('new_app:index.html')

