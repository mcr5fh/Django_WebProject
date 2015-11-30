from django import template

register = template.Library()

@register.assignment_tag
def get_attachments(report):
    return report.attachment_set.all()
