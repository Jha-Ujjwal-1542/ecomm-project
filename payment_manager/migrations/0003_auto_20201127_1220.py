# Generated by Django 3.1.1 on 2020-11-27 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0003_cartitem'),
        ('payment_manager', '0002_invoice_invoicedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceDetails',
            new_name='InvoiceDetail',
        ),
    ]
