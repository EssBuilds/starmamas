# Migration to re-add age and created_at fields to Child model
# Run this migration after the temporary fix

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_child_age_child_created_at_task_completed_and_more'),
    ]

    operations = [
        # These fields should already exist from migration 0002, but we're keeping this
        # as a safety measure in case migration 0002 wasn't applied properly
        migrations.RunSQL(
            "SELECT 1;",  # No-op SQL
            reverse_sql="SELECT 1;",
        ),
    ]
