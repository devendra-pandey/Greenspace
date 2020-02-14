from django.shortcuts import render, redirect
from .models import Gallery, Home_header_image, Page_images, Product , Category
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from users .forms import CustomUserCreationForm
from plants_home .forms import Contact_usCreate
from django.core.mail import send_mail , BadHeaderError , EmailMessage
from django.template.loader import get_template


# Create your views here.
def server_505(request):

    return render(request, "505.html")

def eror_404(request):

    return render(request,"404.html")


def index(request):
    img = Home_header_image.objects.all()

    return render(request, "home/index.html", {'img':img})

def our_story(request):
    gal = Home_header_image.objects.all().filter(page_name = 'our_story')

    image_info = Page_images.objects.all().filter(page_name = 'our_story')

    context = {
        "gal": gal,
        "image_info":image_info

    }
    return render(request, "about/our_story.html",context)

def product(request):

    filter_category = request.GET.get('filter_category')
    category_id = request.GET.get('category_id')
    print("hey its working")
    print(filter_category)

    cat = Category.objects.all()

    category = Category.objects.filter(name=filter_category)

    
    print(category_id)


    pro = Product.objects.all()

    # pro1 = Product.objects.all().filter(category =category_id)
    context = {
        "cat": cat,
        "pro":pro,
        "category":category,
        # "pro1":pro1,

    }

    return render(request, "home/products.html", context)

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
    gal = Home_header_image.objects.all().filter(page_name = 'circular_economy')

    image_info = Page_images.objects.all().filter(page_name = 'circular_economy')

    return render(request, "solutions/circular_eco.html",{'gal':gal, 'image_info':image_info})

def climate_change(request):
    return render(request, "solutions/climate_change.html")

def crop_prod(request):
    return render(request, "solutions/crop_prod.html")

def green_tech(request):
    return render(request, "solutions/green_tech_job.html")

def social_impact(request):
    return render(request, "solutions/social_impact.html")

def vf_eco(request):

    gal = Home_header_image.objects.all().filter(page_name = 'vf_eco')

    image_info = Page_images.objects.all().filter(page_name = 'vf_eco')

    return render(request, "solutions/vf_eco.html",{'gal':gal, 'image_info':image_info})

def login(request):
    return render(request, "account/login.html")


def signup(request):
    return render(request, "account/signup.html")


@login_required
def contact_us(request):

    upload = Contact_usCreate()
    if request.method == 'POST':
        upload = Contact_usCreate(request.POST, request.FILES)
        if upload.is_valid():
            name = request.POST.get('name')
            email_id = request.POST.get('email_id')
            subject = request.POST.get('subject')
            contact_number = request.POST.get('contact_number')
            description = request.POST.get('description')


            template = get_template('home/contact_template.html')
            context = {
                'name': name,
                'email_id': email_id,
                'subject':subject,
                'contact_number': contact_number,
                'description': description,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Greenspace" +'',
                ['greenspace173@gmail.com'],
                headers = {'Reply-To': email_id }
            )
            email.send()
            
            upload.save() 
            return redirect('successfull')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")
    else:
        return render(request, 'home/contact_us.html')
    
    context = {
        "Contact_usCreate": Contact_usCreate,
    }
    return render(request, 'home/contact_us.html', context)


def successfull(request):
    return render(request, "home/successfull.html")

def footer(request):
    return render(request, 'home/footer.html')

@login_required
def profile(request):

    return render(request, 'home/profile.html')


@login_required
def cart(request):

    return render(request, 'home/cart.html')         