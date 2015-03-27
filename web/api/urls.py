# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^$", "api.views.index"),
    url(r"^tasks/create/file/$", "api.views.tasks_create_file"),
    url(r"^tasks/create/url/$", "api.views.tasks_create_url"),
    url(r"^tasks/search/md5/(?P<md5>([a-fA-F\d]{32}))/$", "api.views.tasks_search"),
    url(r"^tasks/search/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", "api.views.tasks_search"),
    url(r"^tasks/list/$", "api.views.tasks_list"),
    url(r"^tasks/list/(?P<limit>\d+)/$", "api.views.tasks_list"),
    url(r"^tasks/list/(?P<limit>\d+)/(?P<offset>\d+)/$", "api.views.tasks_list"),
    url(r"^tasks/view/(?P<task_id>\d+)/$", "api.views.tasks_view"),
    url(r"^tasks/reschedule/(?P<task_id>\d+)/$", "api.views.tasks_reschedule"),
    url(r"^tasks/delete/(?P<task_id>\d+)/$", "api.views.tasks_delete"),
    url(r"^tasks/status/(?P<task_id>\d+)/$", "api.views.tasks_status"),
    url(r"^tasks/get/report/(?P<task_id>\d+)/$", "api.views.tasks_report"),
    url(r"^tasks/get/report/(?P<task_id>\d+)/(?P<report_format>\w+)/$", "api.views.tasks_report"),
    url(r"^tasks/get/iocs/(?P<task_id>\d+)/$", "api.views.tasks_iocs"),
    url(r"^tasks/get/iocs/(?P<task_id>\d+)/(?P<detail>detailed)/$", "api.views.tasks_iocs"),
    url(r"^tasks/get/screenshot/(?P<task_id>\d+)/$", "api.views.tasks_screenshot"),
    url(r"^tasks/get/screenshot/(?P<task_id>\d+)/(?P<screenshot>\d{1,4})/$", "api.views.tasks_screenshot"),
    url(r"^tasks/get/procmemory/(?P<task_id>\d+)/$", "api.views.tasks_procmemory"),
    url(r"^tasks/get/procmemory/(?P<task_id>\d+)/(?P<pid>\d{1,5})/$", "api.views.tasks_procmemory"),
    url(r"^tasks/get/fullmemory/(?P<task_id>\d+)/$", "api.views.tasks_fullmemory"),
    url(r"^tasks/get/pcap/(?P<task_id>\d+)/$", "api.views.tasks_pcap"),
    url(r"^files/view/md5/(?P<md5>([a-fA-F\d]{32}))/$", "api.views.files_view"),
    url(r"^files/view/sha256/(?P<sha256>([a-fA-F\d]{64}))/$", "api.views.files_view"),
    url(r"^files/view/id/(?P<sample_id>\d+)/$", "api.views.files_view"),
    url(r"^files/get/(?P<stype>md5)/(?P<value>([a-fA-F\d]{32}))/$", "api.views.get_files"),
    url(r"^files/get/(?P<stype>sha256)/(?P<value>([a-fA-F\d]{64}))/$", "api.views.get_files"),
    url(r"^files/get/(?P<stype>task)/(?P<value>\d+)/$", "api.views.get_files"),
    url(r"^machines/list/$", "api.views.machines_list"),
    url(r"^machines/view/(?P<name>[\w$-/:-?{-~!^_`\[\]]+)/$", "api.views.machines_view"),
    url(r"^cuckoo/status/$", "api.views.cuckoo_status"),
)