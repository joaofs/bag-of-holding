from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('',

    # Organization Routes

    url(r'^organizations/add/$', views.organization_add, name='organization.add'),
    url(r'^organizations/(?P<organization_id>\d+)/$', views.organization_detail, name='organization.detail'),

	# Application Routes
    url(r'^applications/$', views.application_list, name='application.list'),
    url(r'^applications/add/$', views.application_add, name='application.add'),

    url(r'^applications/(?P<application_id>\d+)/$', views.application_overview, name='application.overview'),
    url(r'^applications/(?P<application_id>\d+)/engagements/$', views.application_engagements, name='application.engagements'),
    url(r'^applications/(?P<application_id>\d+)/environments/$', views.application_environments, name='application.environments'),
    url(r'^applications/(?P<application_id>\d+)/people/$', views.application_people, name='application.people'),
    url(r'^applications/(?P<application_id>\d+)/settings/$', views.application_settings_general, name='application.settings.general'),
    url(r'^applications/(?P<application_id>\d+)/settings/metadata/$', views.application_settings_metadata, name='application.settings.metadata'),
    url(r'^applications/(?P<application_id>\d+)/settings/services/$', views.application_settings_services, name='application.settings.services'),
    url(r'^applications/(?P<application_id>\d+)/settings/danger/$', views.application_settings_danger, name='application.settings.danger'),

    url(r'^applications/(?P<application_id>\d+)/delete/$', views.application_delete, name='application.delete'),



    # Environment Routes
    url(r'^applications/(?P<application_id>\d+)/environments/add/$', views.environment_add, name='environment.add'),
    url(r'^environments/(?P<environment_id>\d+)/$', views.environment_detail, name='environment.detail'),
    url(r'^environments/(?P<environment_id>\d+)/locations/add/$', views.environment_location_add, name='environment.location.add'),


    # Engagement Routes
    url(r'^applications/(?P<application_id>\d+)/engagements/add/$', views.engagement_add, name='engagement.add'),
    url(r'^engagements/(?P<engagement_id>\d+)/$', views.engagement_detail, name='engagement.detail'),
    url(r'^engagements/(?P<engagement_id>\d+)/edit/$', views.engagement_edit, name='engagement.edit'),
    url(r'^engagements/(?P<engagement_id>\d+)/delete/$', views.engagement_delete, name='engagement.delete'),
    url(r'^engagements/(?P<engagement_id>\d+)/comments/add/$', views.engagement_comment_add, name='engagement.comment.add'),

    # Activity Routes
    url(r'^engagements/(?P<engagement_id>\d+)/activities/add/$', views.activity_add, name='activity.add'),
    url(r'^activities/(?P<activity_id>\d+)/$', views.activity_detail, name='activity.detail'),
    url(r'^activities/(?P<activity_id>\d+)/edit/$', views.activity_edit, name='activity.edit'),
    url(r'^activities/(?P<activity_id>\d+)/delete/$', views.activity_delete, name='activity.delete'),
    url(r'^activities/(?P<activity_id>\d+)/comments/add/$', views.activity_comment_add, name='activity.comment.add'),

    # People Routes
    url(r'^people/$', views.people_list, name='people.list'),
    url(r'^people/add/$', views.people_add, name='people.add'),
    url(r'^people/(?P<person_id>\d+)/$', views.people_detail, name='people.detail'),
)
