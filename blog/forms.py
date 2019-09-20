from django import forms
from .models import Comment

"""ModelFormは入力欄を自動生成する．Formは自身で入力欄を定義"""
class CommentCreateForm(forms.ModelForm):

    """__init__を上書き．つまり初期化処理を上書き"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control' #CSSを適用するための処理

    class Meta:
        model = Comment #対象とするモデル
        fields = ('name','text') #フィールドの指定，全ての場合はall.特定のものにしたい場合は('title','text')など
