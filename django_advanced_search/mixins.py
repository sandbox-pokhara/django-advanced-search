from django_advanced_search.tokens import get_tokens


class AdvancedSearchMixin:
    def get_search_results(self, request, queryset, search_term):
        if not hasattr(self, "advanced_search_fields"):
            return super().get_search_results(request, queryset, search_term)

        token, advanced_tokens = get_tokens(search_term)
        queryset, use_distinct = super().get_search_results(
            request, queryset, token
        )

        filter_query = {}
        for t in advanced_tokens:
            if (
                t["type"] == "equal"
                and t["key"] in self.advanced_search_fields
            ):
                filter_query[t["key"]] = t["value"]
        try:
            # TODO: validate filter_query before calling fiter()
            queryset = queryset.filter(**filter_query)
        except ValueError:
            # catches ValueError when value of integer field fitler
            # contains characters
            pass
        return queryset, use_distinct
