#変数を色々定義
from django.db import models
from django.core import validators

class Item(models.Model):
    #　落としたor拾った　二次元配列
    Type_CHOICES = ( (1, '落とした'),(2, '拾った'), )
    #選択肢
    type = models.IntegerField(
        verbose_name='落とした？or拾った？',
        choices=Type_CHOICES,
        default=1
    )


    # ３０文字までの文字枠
    name = models.CharField(
        verbose_name='品目',
        max_length=30,
    )
    image = models.ImageField(
        verbose_name='画像',
        upload_to='uploads/%Y/%m/%d',
        blank=True,
        null=True,
        default='images.png',
    )
    #文章枠
    memo = models.TextField(
        verbose_name='備考 (詳細情報や何処で見つけた、何処に届けた届けたなど)',
        max_length=300,
        blank=True,
        null=True,
    )
    #生成時刻　現在時刻を自動で
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'