from  rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from app.views import PassportViewSet
router=DefaultRouter()
router.register(r'passports',PassportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
