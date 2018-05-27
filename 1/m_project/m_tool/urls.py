from django.conf.urls import path
from django.contrib import admin

import manager.views as manager_view

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'^worker_list/', manager_view.WorkerListView.as_view()),
    ]
