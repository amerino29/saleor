# Generated by Django 3.0.5 on 2020-04-15 09:43

from django.db import migrations


def change_extension_permission_to_plugin_permission(apps, schema_editor):
    permission = apps.get_model("auth", "Permission")
    users = apps.get_model("account", "User")

    plugin_permission = permission.objects.filter(
        codename="manage_plugins", content_type__app_label="plugins"
    ).first()
    extension_permission = permission.objects.filter(
        codename="manage_plugins", content_type__app_label="extensions"
    ).first()
    users = users.objects.filter(
        user_permissions__content_type__app_label="extensions",
        user_permissions__codename="manage_plugins",
    )

    if not plugin_permission or not extension_permission:
        return

    for user in users:
        user.user_permissions.remove(extension_permission)
        user.user_permissions.add(plugin_permission)


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0039_auto_20200221_0257"),
        ("plugins", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(change_extension_permission_to_plugin_permission),
    ]
