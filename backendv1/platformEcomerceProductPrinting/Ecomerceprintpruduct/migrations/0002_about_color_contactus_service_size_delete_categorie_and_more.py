# Generated by Django 4.0.4 on 2022-05-31 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecomerceprintpruduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Tel', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('desription', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('info', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Panier',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('T-shirt', 'T-shirt'), ('Sweat', 'Sweat'), ('pulls', 'pulls')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/image/logotab3lia.png', null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='inStock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='numReviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uplodedebydesigner',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='slides',
            name='backgrounds',
            field=models.CharField(blank=True, default='bg-[#78cbc0]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='slides',
            name='contectHeader',
            field=models.TextField(blank=True, default="Ajoutez une appli d'impression ?? la demande ?? votre boutique en ligne", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='slides',
            name='contectParagraphe',
            field=models.TextField(blank=True, default='Upto 40%/ off', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='slides',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='slides',
            name='src',
            field=models.ImageField(blank=True, default='/imageslide/logotab3lia.png', null=True, upload_to='imageslide/'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='colorr', to='Ecomerceprintpruduct.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='sizee', to='Ecomerceprintpruduct.size'),
        ),
    ]
