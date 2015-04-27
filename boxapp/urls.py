from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boxapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')),
    #url(r'accounts/register/$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),
    (r'^accounts/', include('registration.urls')),
)
