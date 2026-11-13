from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_ON_MAIN_PAGE = 5


def published_posts():
    """Вернуть посты, доступные для просмотра.

    Учитываются флаги публикации поста и категории, а также дата поста.
    Связанные автор, категория и локация загружаются одним запросом.
    """
    return Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    """Показать пять последних доступных публикаций."""
    post_list = published_posts()[:POSTS_ON_MAIN_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    """Показать доступную публикацию или вернуть ошибку 404."""
    post = get_object_or_404(published_posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Показать посты опубликованной категории или вернуть ошибку 404."""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True,
    )
    post_list = published_posts().filter(category=category)
    return render(request, 'blog/category.html', {
        'category': category, 'post_list': post_list,
    })
