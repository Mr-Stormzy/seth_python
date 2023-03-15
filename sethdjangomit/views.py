from django.shortcuts import render


def indexpage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def menupage(request):
    return render(request, 'menu.html')

def servicepage(request):
    return render(request, 'service.html')

def teampage(request):
    return render(request, 'team.html')

def testimonialpage(request):
    return render(request, 'testimonial.html')
