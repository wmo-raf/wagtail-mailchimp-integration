# Generated by Django 4.2.1 on 2024-02-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_mailinglistsubscribepage_success_redirect_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglistsubscribepage',
            name='thank_you_text',
            field=models.TextField(blank=True, default='You have been successfully added to our mailing list. Thank you!', help_text='Message to show on successful submission', null=True, verbose_name='Thank you text'),
        ),
    ]
