# Generated by Django 2.0.9 on 2019-01-22 14:05

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='external URL', required=True))])), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('do_list', wagtail.core.blocks.StructBlock([('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('dont_list', wagtail.core.blocks.StructBlock([('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('inset_text', wagtailnhsukfrontend.blocks.InsetTextBlock()), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('labeled_title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtailnhsukfrontend.blocks.WarningCalloutBlock())]),
            preserve_default=False,
        ),
    ]