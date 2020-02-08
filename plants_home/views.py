from django.shortcuts import render, redirect
from .models import Gallery, Home_header_image, Page_images, Product
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from users .forms import CustomUserCreationForm
from plants_home .forms import Contact_usCreate

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

# Create your views here.
def server_505(request):

    return render(request, "505.html")

def eror_404(request):

    return render(request,"404.html")


def index(request):
    img = Gallery.objects.all()

    return render(request, "home/index.html", {'img':img})

def our_story(request):
    gal = Home_header_image.objects.all()

    image_info = Page_images.objects.all().filter(page_name = 'our_story')


    return render(request, "about/our_story.html",{'gal':gal, 'image_info':image_info})

def product(request):
    pro = Product.objects.all()

    return render(request, "home/products.html", {'pro':pro})

def prod_single(request,id):

    prod_detail = Product.objects.get(id=id)

    product_info = Product.objects.all().filter(id=id)
    print("hello ")
    print(prod_detail)


    return render(request,"home/product-single.html", {'product_info':product_info})

def follow(request):
    
    return render(request, "about/follow_us.html")


def revolutions(request):
    a = 'the_revolutions'
    page = Page_images.objects.all().filter( page_name = a)
    
    return render(request, "about/the_revolutions.html", {'page':page})
def zero_carbon(request):
    return render(request, "about/zero_carbon.html")

def aeroponics(request):

    return render(request, "options/aeroponics.html")

def aquaponics(request):

    return render(request, "options/aquaponics.html")

def biophilic(request):

    return render(request,"options/biophilic_design.html")

def green_roof(request):
    return render(request,"options/green_roofs.html")

def hydroponics(request):
    return render(request, "options/hyroponics.html")

def solar_hydro(request):
    return render(request, "options/solar_hydro.html")

def vertical_farming(request):
    return render(request, "options/vertical_farming.html")

def agritech(request):
    return render(request, "solutions/agritech_inn.html")

def circular(request):
    return render(request, "solutions/circular_eco.html")

def climate_change(request):
    return render(request, "solutions/climate_change.html")

def crop_prod(request):
    return render(request, "solutions/crop_prod.html")

def green_tech(request):
    return render(request, "solutions/green_tech_job.html")

def social_impact(request):
    return render(request, "solutions/social_impact.html")

def vf_eco(request):
    return render(request, "solutions/vf_eco.html")

def login(request):
    return render(request, "account/login.html")

def signup(request):
    return render(request, "account/signup.html")

def contact_us(request):

    upload = Contact_usCreate()
    if request.method == 'POST':
        upload = Contact_usCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('successfull')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")
    else:
        return render(request, 'home/contact_us.html')
    return render(request, 'home/contact_us.html')

def successfull(request):
    return render(request, "home/successfull.html")

def footer(request):
    return render(request, 'home/footer.html')