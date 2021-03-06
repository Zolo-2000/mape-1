from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *

from django.views.generic import TemplateView

urlpatterns = [
	url(r'^map/$', TemplateView.as_view(template_name='showcase/map.html'), name='map'),
    url(r'^events/$', EventListView.as_view(), name='event_list'),
    url(r'^event/add/$', login_required(EventCreateView.as_view()), name='event_create'),
    url(r'^event/(?P<pk>\d+)/update/$', login_required(EventUpdateView.as_view()), name='event_update'),
    url(r'^event/(?P<pk>\d+)/$', login_required(EventDetailView.as_view()), name='event_detail'),
    url(r'^event/add/comment/$', login_required(add_event_comment), name='add_event_comment'),
    url(r'^event/(?P<pk>\d+)/like/$', login_required(event_like), name='event_like'),
    url(r'^event/(?P<pk>\d+)/attend/$', login_required(event_attend), name='event_attend'),
    url(r'^event/(?P<pk>\d+)/maybe_attend/$', login_required(event_maybe_attend), name='event_maybe_attend'),
    url(r'^event/(?P<pk>\d+)/not_attend/$', login_required(event_not_attend), name='event_not_attend'),

    url(r'^localities/$', LocalityListView.as_view(), name='locality_list'),
    url(r'^locality/add/$', login_required(LocalityCreateView.as_view()), name='locality_create'),
    url(r'^locality/(?P<pk>\d+)/update/$', login_required(LocalityUpdateView.as_view()), name='locality_update'),
    url(r'^locality/(?P<pk>\d+)/$', LocalityDetailView.as_view(), name='locality_detail'),
    url(r'^locality/add/comment/$', login_required(add_locality_comment), name='add_locality_comment'),

    url(r'^subscriber/add/$', login_required(add_subscriber), name='subscriber_create'),
    url(r'^send-invitation/(?P<event>\d+)/$', login_required(send_invitation), name='send_invitation'),
    #url(r'^user/change-avatar/$', change_user_avatar),
]