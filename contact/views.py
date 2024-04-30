from django.shortcuts import render

# Create your views here.


def index(requests):
    return render(requests,
                  'contact/index.html')
    