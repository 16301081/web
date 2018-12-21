from django import template
from likes.models import LikeCount, LikeRecord

register = template.Library()

@register.simple_tag
def get_like_count(obj):
    like_count, created = LikeCount.objects.get_or_create(content_type=obj)
    return like_count.liked_num

@register.simple_tag()
def get_like_status(obj,user):

    content_type = LikeRecord.objects.filter(content_type=obj,user=user)
    if content_type.exists():
        return 'active'
    else:
        return ''