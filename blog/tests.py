# _*_ coding:utf-8 _*_

# from django.contrib import admin
# from django.urls import path
# from blog.views import *
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import staticfiles
# from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',IndexView.as_view()),
#     path('post/',PostView.as_view()),
#     path('article/<int:id>/',ArticleView.as_view()),
#     path('<str:urltype>/<str:type>/<int:page>/',ListView.as_view()),
# ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

print(settings.STATICFILES_DIRS)

