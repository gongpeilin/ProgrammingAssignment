# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu ,Booking
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView   
from django.views.generic.detail import DetailView
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

#utilize the CreateView class to create a view for the Booking model
class BookCreateView(CreateView):
    model = Booking
    fields = '__all__'
    template_name = 'book.html'
    success_url = '/book/success/'

class BookUpdateView(UpdateView):
    model = Booking
    fields = '__all__'
    template_name = 'book.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

# Delete the booking info
class BookDeleteView(DeleteView):
    model = Booking
    template_name = 'bookConfirmDel.html'
    success_url = '/book/delete/success/'

# Add your code here to create new views

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {'menu_item':menu_item})

def success(request):
    latest_booking = Booking.objects.latest('id')
    return render(request, 'bookConfirm.html', {'booking': latest_booking})

#  New add on 30.11.24
def disaply_booking_item(request, pk=None):
    if pk:
        booking_item = Booking.objects.get(pk=pk)
    else:
        booking_item = ""
    return render(request, 'bookConfirm.html', {'booking':booking_item})

def display_booking_Cancelinfo(request):
    return render(request, 'bookConfirmDelInfo.html')