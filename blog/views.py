from django.db.models import Q,Count
from django.shortcuts import get_object_or_404,redirect
from django.views import generic
from .models import Post, Category, Comment
from .forms import CommentCreateForm

class IndexView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        """データの順番の入れ替えは order_by を使用.引数はフィールド名を指定"""
        queryset = Post.objects.order_by('-created_at') #全データを最新順にして取得
        keyword = self.request.GET.get('keyword') #検索フォームの入力内容取得
        if keyword:
            """
            __icontainsでkeywordを含むかどうかという指定になる
            Q を使用することで，OR検索ができる
            """
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        """
        category = get_object_or_404(Category,pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        """
        category_pk = self.kwargs['pk']
        """カテゴリーのプライマリーキーと一致するカテゴリーを抽出"""
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk) #__pkでプライマリーキー取得
        return queryset

class DetailView(generic.DetailView):
    model = Post

class CommentView(generic.CreateView):
    model = Comment
    #fields = (name,text)
    form_class = CommentCreateForm

    """
    フォームの入力内容のチェックに合格したら呼び出される
    コメントと記事の紐付けを行う
    """
    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False) #コメント保存の直前のデータ
        comment.post = get_object_or_404(Post,pk=post_pk) #post属性を指定．つまり記事の指定
        comment.save() #ここでDBに保存
        return redirect('blog:detail',pk=post_pk)
