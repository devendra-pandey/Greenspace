from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('server_505/',views.server_505),
    path('eror_404/', views.eror_404),
    path('our_story/', views.our_story),
    path('follow/', views.follow),
    path('revolutions/', views.revolutions),
    path('zero_carbon/', views.zero_carbon),
    path('product/', views.product),
    path('prod_single/<int:id>', views.prod_single),
    path('aeroponics/', views.aeroponics),
    path('aquaponics/', views.aquaponics),
    path('biophilic/', views.biophilic),
    path('green_roof/', views.green_roof),
    path('hydroponics/', views.hydroponics),
    path('solar_hydro/',views.solar_hydro),
    path('vertical_farming/',views.vertical_farming),

    path('agritech/', views.agritech),
    path('circular/', views.circular),
    path('climate_change/', views.climate_change),
    path('crop_prod/',views.crop_prod),
    path('green_tech/', views.green_tech),
    path('social_impact/', views.social_impact),
    path('vf_eco/', views.vf_eco),
    path('contact_us/', views.contact_us),
    path('successfull/', views.successfull , name= 'successfull'),
    path('footer/', views.footer)


    # path('login/', views.login, name='login'),
    # path('signup/', views.signup),


    ]