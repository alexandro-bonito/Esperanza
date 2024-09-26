# Generated by Django 4.2.13 on 2024-09-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esperanza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='couleur',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='pays',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='esperanza.pays'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix_partenaire',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
