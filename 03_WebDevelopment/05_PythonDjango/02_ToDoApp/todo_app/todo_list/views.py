from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_name = "Maximiliano Ponce Marquez"
    context = {'name': my_name}
    return render(request, 'about.html', context)