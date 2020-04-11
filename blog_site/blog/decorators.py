from django.core.exceptions import PermissionDenied
from blog.models import Post
from django.shortcuts import get_object_or_404

def user_is_post_owner(function):
    def wrap(request, *args, **kwargs):
        post =  get_object_or_404(Post,pk=kwargs['pk'])
        if post.post_owner == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap