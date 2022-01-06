from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'bookBus/main.html', context)

def booking(request):
    context = {}
    return render(request, 'bookBus/booking.html', context)
