from django.contrib import admin
from . import models
import conversations

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass