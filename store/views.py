from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator,PageNotAnInteger
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib import messages



def index(request):
    return HttpResponse("Hello there, e-commerce store font coming here...")


def detail(request):
    return HttpResponse("Hello there, e-commerce store font detail page coming here...")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple Iphone", "lenovo", "Samsung", "Google", "Xiaomi", "Oppo", "Vivo")
    #if request.method == 'GET':
     #   print(request.headers)
      #  return HttpResponse("Hello there, e-commerce electronic font detail page coming here...")
    if request.method == 'GET':
        paginator = Paginator(items, 3)
        pages = request.GET.get('page', 1)
        name = "Sharu"
        messages.info(request, "Customer Successfully Fetched")
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        if not request.session.has_key('customer'):
            request.session['customer'] = name
            print("Session values set")
        #return render(request,'store/list.html', {'items' : items})
        response = render(request,'store/list.html', {'items' : items})
        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print ('Getting Cookie')
            response.set_cookie('visits', value+1)
        else:
            value = 1
            print("Setting Cookie")
            response.set_cookie('visits', 1)
        return response
    elif request.method == 'POST':
        return HttpResponseNotFound("POST method is not allowed")

#Mixin example - Parent
class ElectronicsView(View):
    def get(self, request):
        items = ("Windows PC", "Apple Mac", "Apple Iphone", "lenovo", "Samsung", "Google", "Xiaomi", "Oppo", "Vivo")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        self.process()
        try:
            items=paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})

    def process(self):
            print("We are processing Electronics")

class ElectronicsView2(TemplateView):
    template_name = "store/list.html"
    def get_context_data(self, **kwargs):
        items = ("Windows PC", "Apple Mac", "Apple Iphone", "lenovo", "Samsung", "Google", "Xiaomi", "Oppo", "Vivo")
        context = {'items' : items}
        return context

class ElectronicsView3(ListView):
    template_name = "store/list.html"
    queryset = ("Windows PC", "Apple Mac", "Apple Iphone", "lenovo", "Samsung", "Google", "Xiaomi", "Oppo", "Vivo")
    context_object_name = 'items'
    paginate_by = 2

#Mixin example childs - Inheritance
class ComputersView(ElectronicsView):
    #def process(self):
     #   print("We are processing Computers")
    pass

class MobileView():
    def process(self):
        print("We are processing mobiles")

class EquipmentView(ComputersView, MobileView):
    #def process(self):
      #  print("We are processing equipments")
    pass


def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        print("Error while logging out")
    return HttpResponse("You are logged out")
