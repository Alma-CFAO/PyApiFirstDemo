# coding: utf-8

from django.db.models import (
    Model
)
from django.forms.models import \
    model_to_dict as \
    django_model_to_dict


def model_to_dict(instance, expand=""):
    """Convert model and sub models in expand to dict."""
    if expand is None:
        expand = ""

    to_expand = expand.split(',')
    if expand != '' and not isinstance(to_expand, list):
        to_expand = [to_expand]

    for idx, entry in enumerate(to_expand):
        to_expand[idx] = entry.split('.')

    to_expand_first_words = [elem[0] for elem in to_expand]

    instance_dict = django_model_to_dict(instance)

    for key in instance_dict.keys():
        value = instance_dict[key]
        key_indices = [  # indices of expands started by key
            idx for idx, elem in enumerate(
                to_expand_first_words
            ) if elem == key
        ]
        related_sub_expands = [  # navigate through each expand path starting by key
            val[1:] for idx, val in enumerate(to_expand) if idx in key_indices
        ]

        # may be a foreignkey field as django_model_to_dict convert foreignkey as int value
        if isinstance(value, int):
            instance_value = getattr(instance, key)

            # is a model and is in expand
            if (
                isinstance(instance_value, Model) and  # is django model instance
                key in to_expand_first_words  # asked to be expanded
            ):
                instance_dict[key] = model_to_dict(
                    instance_value,
                    expand=",".join(
                        related_sub_expands[0]
                    )
                )

        if isinstance(value, list):
            if key in to_expand_first_words:  # asked to be expanded
                for idx, sub_value in enumerate(value):
                    if isinstance(sub_value, Model):  # is django model instance
                        instance_dict[key][idx] = model_to_dict(
                            sub_value,
                            expand=",".join(
                                related_sub_expands[0]
                            )
                        )
            else:
                for idx, sub_value in enumerate(value):
                    if isinstance(sub_value, Model):  # is django model instance
                        instance_dict[key][idx] = sub_value.id

    return instance_dict
