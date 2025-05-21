from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope




class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        tags_set = set()
        for form in self.forms:
            if self._should_delete_form(form):
                continue
            if not form.cleaned_data:
                continue
            tag_name = form.cleaned_data.get('tag')
            article = form.cleaned_data.get('article')
            if not self._should_delete_form(form):
                if not tag_name:
                    raise ValidationError('Тег является обязательным полем!')
                if not article:
                    raise ValidationError(
                        'Статья является обязательным полем!')
            if form.cleaned_data.get('is_main'):
                main_count += 1
            if tag_name in tags_set:
                raise ValidationError(f'Тег "{tag_name}" уже существует!')
            tags_set.add(tag_name)
        if main_count > 1:
            raise ValidationError('Основной тэг может быть только один!')
        elif main_count == 0:
            raise ValidationError(
                'Необходимо установить хоть один тэг как основной!')

        return super().clean()
class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 1

@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass