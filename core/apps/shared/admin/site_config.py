from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from core.apps.shared.models.site_config import SiteConfig 


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def changelist_view(self, request, extra_context=None):
        config, created = SiteConfig.objects.get_or_create(
            defaults=dict(
                email_host="smtp.gmail.com",
                email_host_password="",
                bot_token="",
                channel_username="@channel",
                manager="https://t.me/manager",
            )
        )
        url = reverse("admin:shared_siteconfig_change", args=[config.id])
        return HttpResponseRedirect(url)