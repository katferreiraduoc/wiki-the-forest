from django.db import migrations

def insertar_roles(apps, schema_editor):
    Rol = apps.get_model('core', 'Rol')
    Rol.objects.get_or_create(id=1, nombre='Usuario')
    Rol.objects.get_or_create(id=2, nombre='Administrador')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insertar_roles),
    ]
