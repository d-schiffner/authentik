# Generated by Django 3.1.1 on 2020-09-25 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_flows", "0013_auto_20200924_1605"),
        (
            "passbook_stages_password",
            "0003_passwordstage_failed_attempts_before_cancel",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="passwordstage",
            old_name="change_flow",
            new_name="configure_flow",
        ),
        migrations.AlterField(
            model_name="passwordstage",
            name="configure_flow",
            field=models.ForeignKey(
                blank=True,
                help_text="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="passbook_flows.flow",
            ),
        ),
    ]
