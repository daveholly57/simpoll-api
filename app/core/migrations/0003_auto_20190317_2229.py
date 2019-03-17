# Generated by Django 2.1.7 on 2019-03-17 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190316_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.age'),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.education'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ethnicity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.ethnicity'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='income',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.income'),
        ),
        migrations.AlterField(
            model_name='user',
            name='politicalideology',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.polideology'),
        ),
        migrations.AlterField(
            model_name='user',
            name='politics',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.politics'),
        ),
        migrations.AlterField(
            model_name='user',
            name='race',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.race'),
        ),
        migrations.AlterField(
            model_name='user',
            name='religion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.religion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usregion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.usregion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usstate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.usstates'),
        ),
    ]
