from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import *
from django.conf import settings
from . import forms
# Register your models here.

class AnswerHelpfulAdmin(admin.ModelAdmin):
    list_display = ("vote","answer" ,"user")
    list_filter = ('vote',)
    search_fields = ['answer', "user"]

class QuestionHelpfulAdmin(admin.ModelAdmin):
    list_display = ("vote","question" ,"user")
    list_filter = ('vote',)
    search_fields = ['question', "user"]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer","question" ,"helpful", "not_helpful")
    list_filter = ('helpful', "not_helpful")
    search_fields = ['answer', "question"]
    readonly_fields = ('helpful',"not_helpful")

class CategoryAdmin(OrderedModelAdmin):
    list_display = ("name", 'move_up_down_links', "slug" ,"description")
    search_fields = ['name', "description"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment","question" ,"user", "post_time")
    list_filter = ('question', "post_time")
    search_fields = ['comment', "question"]

class QuestionAdmin(OrderedModelAdmin):
    list_display = ("question", "move_up_down_links", "category" ,"slug", "helpful", "not_helpful")
    list_filter = ('helpful', "not_helpful", "category")
    search_fields = ["question"]
    readonly_fields = ('helpful',"not_helpful")

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)

# if category enabled
if "no_category" not in settings.FAQ_SETTINGS:
    admin.site.register(Category,CategoryAdmin)


# if comments are enabled
if "no_comments" not in settings.FAQ_SETTINGS:
    admin.site.register(FAQComment,CommentAdmin)

# if votes are enabled
if "no_votes" not in settings.FAQ_SETTINGS:
    # if answer votes are enabled
    if "no_answer_votes" not in settings.FAQ_SETTINGS:
        admin.site.register(AnswerHelpful,AnswerHelpfulAdmin)

    # if question votes are enabled
    if "no_question_votes" not in settings.FAQ_SETTINGS:
        admin.site.register(QuestionHelpful,QuestionHelpfulAdmin)