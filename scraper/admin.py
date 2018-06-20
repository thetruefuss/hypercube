from django.contrib import admin

from .models import Book, ContactUs


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    date_hierarchy = 'created'
admin.site.register(Book, BookAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    date_hierarchy = 'timestamp'
admin.site.register(ContactUs, ContactUsAdmin)
