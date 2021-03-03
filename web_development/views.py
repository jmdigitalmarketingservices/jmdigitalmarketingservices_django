from django.shortcuts import render

# Create your views here.


def view(request):

    return render(request, "web_development/index.html")
