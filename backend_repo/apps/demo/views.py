# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from apps.demo.models import Post, Comment
from django.db.models import Count
from rest_framework import status


@api_view(['GET'])
def posts_with_comments(request):
   
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Adjust the page size as needed
    posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-timestamp')
    paginated_posts = paginator.paginate_queryset(posts, request)

    response_data = []
    for post in paginated_posts:
        comments = post.comments.order_by('-timestamp')[:3]
        response_data.append({
            'id': post.id,
            'text': post.text,
            'timestamp': post.timestamp,
            'author_username': post.author.username,
            'comment_count': post.comment_count,
            'comments': [
                {
                    'text': comment.text,
                    'timestamp': comment.timestamp,
                    'author_username': comment.author.username,
                }
                for comment in comments
            ],
        })

    return paginator.get_paginated_response(response_data)
