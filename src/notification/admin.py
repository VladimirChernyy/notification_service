from django.contrib import admin

from .models import Mailing, Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ('operator_code',)


admin.site.register(Mailing)
admin.site.register(Message)
