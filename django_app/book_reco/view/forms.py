from django import forms


GENRE_CHOICES = (
    ("本", "本"),
    ("CD", "CD"),
    ("DVD", "DVD"),
    ("PCソフト・周辺機器", "PCソフト・周辺機器"),
    ("洋書", "洋書"),
    ("ゲーム", "ゲーム"),
    ("雑誌", "雑誌")
)


class DocumentForm(forms.Form):
    """
    検索ワードを保存する

    Attributes
    ----------
    keyword : str
        検索ワード
    """
    keyword = forms.CharField(
        label='keyword',
        max_length=50,
        required=True,
    )

    genre = forms.ChoiceField(
        label='genre',
        widget=forms.Select,
        choices=GENRE_CHOICES,
        initial='本'
    )
