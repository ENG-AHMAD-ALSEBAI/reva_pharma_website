# Generated by Django 5.0.4 on 2025-02-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_pro_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pro_Therapeutic_Category',
            field=models.CharField(blank=True, choices=[('Analgesic', 'Analgesic Antipyretic and Muscle-Relaxants'), ('Antibiotics', 'Antibiotics'), ('Anti_Cold', 'Anti Cold and Cough'), ('Antifungal', 'Antifungal'), ('Antifungal_Antiprotozoal', 'Antifungal Antiprotozoal'), ('Bronchodilator', 'Bronchodilator'), ('Corticosteroids', 'Corticosteroids'), ('Vitamin', 'Vitamin Supplement'), ('NSAID', 'Nonsteroidal anti-inflammatory drugs'), ('Cardiovascular', 'Cardiovascular Drugs'), ('Antihistamines', 'Antihistamines'), ('Antiseptics', 'Antiseptics'), ('Fluid_Electrolyte', 'Fluid & Electrolyte replacement'), ('Gynecology', 'Gynecology and Genitourinary'), ('Gastrointestinal', 'Gastrointestinal Drugs'), ('Hemorrhoids', 'Hemorrhoids Medication'), ('Anti_diabetic', 'Anti-diabetic drugs'), ('Benicillins', 'Benicillins')], max_length=50, null=True, verbose_name='Therapeutic Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_type',
            field=models.CharField(choices=[('Oral Suspension', 'Oral Suspension'), ('Capsule', 'Capsule'), ('tablets', 'Tablets'), ('Syrup', 'Syrup'), ('Suppositories', 'Suppositories'), ('Oral Drops', 'Oral Drops'), ('Dry Syrup', 'Dry Syrup')], max_length=50, verbose_name='Product Type'),
        ),
    ]
