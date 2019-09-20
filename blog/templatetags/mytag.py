from django import template #filterやtagを登録するためのモジュール

register = template.Library() #filterやtagを登録するための初期化処理

"""自作テンプレートを作成する準備：以下のように書くこと(形で覚える)"""
@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータを一部置き換える"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
