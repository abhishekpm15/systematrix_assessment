from django.shortcuts import render

def button_view(request):
    return render(request, 'button_template.html')
