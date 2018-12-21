from django.shortcuts import render,redirect
from .models import LikeCount,LikeRecord
from account_app.models import Weibo, MyUser
from django.http import JsonResponse
# Create your views here.

def SuccessResponse(liked_num):
    data ={}
    data['status'] = 'SUCCESS'
    data['liked_num'] = liked_num
    return JsonResponse(data)

def ErrorResponse(message):
    data={}
    data['status'] = 'ERROR'
    data['message'] = message
    return JsonResponse(data)


def like_change(request):
    user = request.user

    obj_id = request.GET.get('obj_id')
    obj_id = Weibo.objects.get(id = obj_id)
    if request.GET.get('is_like') == 'true':

       like_record,created= LikeRecord.objects.get_or_create(content_type=obj_id,user=user)
       if created:
           like_count, created = LikeCount.objects.get_or_create(content_type=obj_id)
           like_count.liked_num +=1
           like_count.save()
           return SuccessResponse(like_count.liked_num)
       else:
           return ErrorResponse('you were liked')
    else:
        if LikeRecord.objects.filter(content_type=obj_id,user=user).exists():
            like_record= LikeRecord.objects.get(content_type=obj_id, user=user)
            like_record.delete()
            like_count, created = LikeCount.objects.get_or_create(content_type=obj_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return SuccessResponse(like_count.liked_num)
            else:
                return ErrorResponse('data error')
        else:
            return ErrorResponse('you were not liked')
