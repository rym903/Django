"""m_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings

import m_tool.views as m_tool_view


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'login/', m_tool_view.CustomLoginView.as_view()),
    path(r'worker_list/', m_tool_view.WorkerListView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(r'__debug__/',include(debug_toolbar.urls)),
        ]
