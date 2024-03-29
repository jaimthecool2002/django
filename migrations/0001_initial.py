# Generated by Django 5.0 on 2024-02-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_investment', models.IntegerField()),
                ('name_of_doctor', models.CharField(max_length=255)),
                ('tm_name', models.CharField(max_length=255)),
                ('hq_name', models.CharField(max_length=255)),
                ('month_of_investment', models.CharField(choices=[('', '-- Select Option --'), ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
                ('amount_invested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_renew', models.CharField(choices=[('', '-- Select Option --'), ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
                ('roi_of_last_year', models.DecimalField(decimal_places=2, max_digits=10)),
                ('january_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('february_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('march_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('april_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('may_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('june_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('july_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('august_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('september_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('october_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('november_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('december_roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('times_of_roi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('', '-- Select Option --'), ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
            ],
        ),
    ]
