# coding: utf-8


def apply_limit_and_offset_on_queryset(
    queryset,
    limit,
    offset
):
    """Apply limit and offset on queryset."""
    if limit is None:
        limit = -1
    else:
        limit = limit
    if offset is None:
        offset = 0
    else:
        offset = offset
    if limit == -1:
        limitted = queryset[offset:]
    else:
        limitted = queryset[offset:offset + limit]
    return limitted
