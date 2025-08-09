import django_filters

from core.apps.cars.models import Car


class CarFilter(django_filters.FilterSet):
    start_year = django_filters.CharFilter(method='filter_by_year_range')
    start_month = django_filters.CharFilter(method='filter_by_month_range')
    end_year = django_filters.CharFilter(method='filter_by_year_range')
    end_month = django_filters.CharFilter(method='filter_by_month_range')
    max_miliage = django_filters.NumberFilter(method='filter_by_miliga_range')
    min_miliage = django_filters.NumberFilter(method='filter_by_miliga_range')
    max_price = django_filters.NumberFilter(method='filter_by_price_range')
    min_price = django_filters.NumberFilter(method='filter_by_price_range')
    ordering = django_filters.CharFilter(method='filter_order_queryset')

    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'generation', 'fuel_type', 'body_type', 'transmission', 'color', 'region',
        ]
    
    def filter_by_year_range(self, queryset, name, value):
        start = self.data.get('start_year')
        end = self.data.get('end_year')
        if start and end:
            return queryset.filter(year__gte=start, year__lte=end)
        return queryset

    def filter_by_month_range(self, queryset, name, value):
        start = self.data.get('start_month')
        end = self.data.get('end_month')
        if start and end:
            return queryset.filter(month__gte=start, month__lte=end)
        return queryset
    
    def filter_by_miliga_range(self, queryset, name, value):
        min = self.data.get('min_miliage')
        max = self.data.get('max_miliage')
        if min and max:
            return queryset.filter(miliage__range=(min, max))
        return queryset

    def filter_by_price_range(self, queryset, name, value):
        min = self.data.get('min_price')
        max = self.data.get('max_price')
        if min and max:
            return queryset.filter(price__range=(min, max))
        return queryset
    
    def filter_order_queryset(self, queryset, name, value):
        if value == 'updated_at':
            return queryset.order_by('updated_at')
        elif value == 'max_miliage':
            return queryset.order_by('-miliage')
        elif value == 'min_miliage':
            return queryset.order_by('miliage')
        elif value == 'max_price':
            return queryset.order_by('-price')
        elif value == 'min_price':
            return queryset.order_by('price')
        elif value == 'max_year':
            return queryset.order_by('-year')
        elif value == 'min_year':
            return queryset.order_by('year')
        else:
            return queryset.order_by('updated_at')