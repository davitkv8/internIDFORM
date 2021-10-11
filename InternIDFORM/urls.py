from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userslist/', UsersListView.as_view(), name="users-list")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

