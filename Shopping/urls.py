"""
URL configuration for Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from apis.views import StateViewSet,CityViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/mystate', StateViewSet)
router.register(r'api/city',CityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("apis.urls")),
    path('',include("AdminDashboard.urls")),
    path('',include("AdminCategory.urls")),
    path('',include("Adminsubcategory.urls")),
    path('',include("AdminProduct.urls")),
    path('',include("Location.urls")),
    path('',include("Home.urls")),
    path('',include("Product.urls")),
    path('',include("Authentication.urls")),
    path('',include("Cart.urls")),
    path('',include("Checkout.urls")),
    path('',include("Item.urls")),
    path('',include("Email.urls")),
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
