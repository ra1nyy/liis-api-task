from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/workspaces/', include('workspace.urls')),
    path('api/v1/booking/', include('booking.urls')),
    path('api/v1/account/', include('account.urls')),
]
