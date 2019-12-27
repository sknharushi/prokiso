from django_filters import filters
from django_filters import FilterSet
from .models import Item

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class ItemFilter(FilterSet):
    # lookup_expr 検索条件を指定する
    name = filters.CharFilter(label='品物', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
        ),
        field_labels={
            'name': '品物名',

        },
        label='並び順'
    )
    class Meta:
        model = Item
        fields = ('name', 'type', 'memo',)