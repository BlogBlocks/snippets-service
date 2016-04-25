# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from django_mysql.models.functions import AsType, ColumnAdd


def migrate_aboutaccounts_snippets(apps, schema_editor):
    """Migrate existing snippets that used about:accounts link filtering."""
    Snippet = apps.get_model('base', 'Snippet')
    Snippet.objects.update(
        client_options=ColumnAdd(
            'client_options',
            {
                'version_lower_bound': AsType('any', 'CHAR'),
                'version_upper_bound': AsType('any', 'CHAR')
            })
    )


def noop(apps, schema_editor):
    # nothing needed to go back in time.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20160419_1316'),
    ]

    operations = [
        migrations.RunPython(migrate_aboutaccounts_snippets, noop),
    ]
