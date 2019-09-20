from django.db import models
from django.utils import timezone

"""まず主役のモデルを作成する"""
class Category(models.Model):
    """カテゴリー"""
    name = models.CharField('カテゴリー', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ブログの記事"""

    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """ブログのコメント"""

    name = models.CharField('名前', max_length=30, default='匿名')
    text = models.TextField('コメント')
    post = models.ForeignKey(Post, verbose_name='紐ずく記事', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
