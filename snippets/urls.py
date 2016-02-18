from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.views.static import serve as static_serve


def robots_txt(request):
    permission = 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow'
    return HttpResponse('User-agent: *\n{0}: /'.format(permission),
                        mimetype='text/plain')

urlpatterns = [
    url(r'', include('snippets.base.urls')),
    url(r'^robots\.txt$', robots_txt)
]


if settings.ENABLE_ADMIN:
    urlpatterns += [
        url(r'^admin/', include('smuggler.urls')),
        url(r'^admin/', include(admin.site.urls)),
    ]
    admin.site.site_header = 'Snippets Administration'
    admin.site.site_title = 'Mozilla Snippets'


if settings.SAML_ENABLE:
    urlpatterns += [
        url(r'^saml2/', include('snippets.saml.urls'))
        ]


# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Use custom serve function that adds necessary headers.
    def serve_media(*args, **kwargs):
        response = static_serve(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve_media, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + staticfiles_urlpatterns()
