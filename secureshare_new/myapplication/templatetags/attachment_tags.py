from django import template

register = template.Library()

@register.assignment_tag
def get_reports(folder):
    return folder.report_set.all()
