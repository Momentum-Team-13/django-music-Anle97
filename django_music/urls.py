from cgitb import html
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from albums import views as albums_views
from django_music import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include ('debug_toolbar.urls')),

    path('', albums_views.list_albums, name='list_albums'),

    path('albums/new', albums_views.add_album, name='add_album'),

    path('albums/<int:pk>/', albums_views.album_details, name='album_details'),

    path('albums/<int:pk>/edit/', albums_views.edit_album, name='edit_album'),

    # path('albums/<int:pk>/delete/', albums_views.delete_album, name='delete_album'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns