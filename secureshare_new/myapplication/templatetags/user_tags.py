from django import template

register = template.Library()

@register.assignment_tag
def get_users(group):
    return group.user_set.all()
