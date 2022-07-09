# Generated by Django 4.0.4 on 2022-07-08 11:11

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_charity', models.BooleanField(default=False)),
                ('is_donor', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('Afganistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bonaire', 'Bonaire'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('British Indian Ocean Ter', 'British Indian Ocean Ter'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Canary Islands', 'Canary Islands'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Channel Islands', 'Channel Islands'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos Island', 'Cocos Island'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote DIvoire', 'Cote DIvoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curaco', 'Curacao'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French Southern Ter', 'French Southern Ter'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Hawaii', 'Hawaii'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('Indonesia', 'Indonesia'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea North', 'Korea North'), ('Korea Sout', 'Korea South'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malaysia', 'Malaysia'), ('Malawi', 'Malawi'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Midway Islands', 'Midway Islands'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Nambia', 'Nambia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherland Antilles', 'Netherland Antilles'), ('Netherlands', 'Netherlands (Holland, Europe)'), ('Nevis', 'Nevis'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau Island', 'Palau Island'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Phillipines', 'Philippines'), ('Pitcairn Island', 'Pitcairn Island'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Republic of Montenegro', 'Republic of Montenegro'), ('Republic of Serbia', 'Republic of Serbia'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('St Barthelemy', 'St Barthelemy'), ('St Eustatius', 'St Eustatius'), ('St Helena', 'St Helena'), ('St Kitts-Nevis', 'St Kitts-Nevis'), ('St Lucia', 'St Lucia'), ('St Maarten', 'St Maarten'), ('St Pierre & Miquelon', 'St Pierre & Miquelon'), ('St Vincent & Grenadines', 'St Vincent & Grenadines'), ('Saipan', 'Saipan'), ('Samoa', 'Samoa'), ('Samoa American', 'Samoa American'), ('San Marino', 'San Marino'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tahiti', 'Tahiti'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos Is', 'Turks & Caicos Is'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('United Arab Erimates', 'United Arab Emirates'), ('United States of America', 'United States of America'), ('Uraguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City State', 'Vatican City State'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (Brit)', 'Virgin Islands (Brit)'), ('Virgin Islands (USA)', 'Virgin Islands (USA)'), ('Wake Island', 'Wake Island'), ('Wallis & Futana Is', 'Wallis & Futana Is'), ('Yemen', 'Yemen'), ('Zaire', 'Zaire'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50)),
                ('description', models.TextField(max_length=700)),
                ('charity_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='charity_image')),
                ('date_formed', models.DateTimeField(auto_now_add=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('target_amount', models.IntegerField(choices=[(100000, '$100,000'), (200000, '$200,000'), (300000, '$300,000'), (400000, '$400,000'), (500000, '$500,000'), (700000, '$700,000'), (600000, '$600,000'), (800000, '$800,000'), (900000, '$900,000'), (1000000, '$1M+')], null=True)),
                ('deadline', models.DateTimeField(auto_now_add=True)),
                ('mission', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adp.charity')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=30)),
                ('country', models.CharField(choices=[('Afganistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bonaire', 'Bonaire'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('British Indian Ocean Ter', 'British Indian Ocean Ter'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Canary Islands', 'Canary Islands'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Channel Islands', 'Channel Islands'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos Island', 'Cocos Island'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote DIvoire', 'Cote DIvoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curaco', 'Curacao'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French Southern Ter', 'French Southern Ter'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Hawaii', 'Hawaii'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('Indonesia', 'Indonesia'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea North', 'Korea North'), ('Korea Sout', 'Korea South'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malaysia', 'Malaysia'), ('Malawi', 'Malawi'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Midway Islands', 'Midway Islands'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Nambia', 'Nambia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherland Antilles', 'Netherland Antilles'), ('Netherlands', 'Netherlands (Holland, Europe)'), ('Nevis', 'Nevis'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau Island', 'Palau Island'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Phillipines', 'Philippines'), ('Pitcairn Island', 'Pitcairn Island'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Republic of Montenegro', 'Republic of Montenegro'), ('Republic of Serbia', 'Republic of Serbia'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('St Barthelemy', 'St Barthelemy'), ('St Eustatius', 'St Eustatius'), ('St Helena', 'St Helena'), ('St Kitts-Nevis', 'St Kitts-Nevis'), ('St Lucia', 'St Lucia'), ('St Maarten', 'St Maarten'), ('St Pierre & Miquelon', 'St Pierre & Miquelon'), ('St Vincent & Grenadines', 'St Vincent & Grenadines'), ('Saipan', 'Saipan'), ('Samoa', 'Samoa'), ('Samoa American', 'Samoa American'), ('San Marino', 'San Marino'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tahiti', 'Tahiti'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos Is', 'Turks & Caicos Is'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('United Arab Erimates', 'United Arab Emirates'), ('United States of America', 'United States of America'), ('Uraguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City State', 'Vatican City State'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (Brit)', 'Virgin Islands (Brit)'), ('Virgin Islands (USA)', 'Virgin Islands (USA)'), ('Wake Island', 'Wake Island'), ('Wallis & Futana Is', 'Wallis & Futana Is'), ('Yemen', 'Yemen'), ('Zaire', 'Zaire'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50)),
                ('bio', models.TextField(max_length=700)),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png', max_length=255, verbose_name='image')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_raised', models.IntegerField()),
                ('date_donated', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(default='Paypal', max_length=30)),
                ('donation_frequency', models.CharField(choices=[('Once', 'Once'), ('Monthly', 'Monthly'), ('Annualy', 'Annualy')], max_length=30)),
                ('comment', models.TextField()),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adp.charity')),
                ('donor_id', models.ManyToManyField(blank=True, to='adp.donor')),
            ],
        ),
        migrations.AddField(
            model_name='charity',
            name='donor',
            field=models.ManyToManyField(blank=True, to='adp.donor'),
        ),
        migrations.AddField(
            model_name='charity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('Afganistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bonaire', 'Bonaire'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('British Indian Ocean Ter', 'British Indian Ocean Ter'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Canary Islands', 'Canary Islands'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Channel Islands', 'Channel Islands'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos Island', 'Cocos Island'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote DIvoire', 'Cote DIvoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curaco', 'Curacao'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French Southern Ter', 'French Southern Ter'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Hawaii', 'Hawaii'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('Indonesia', 'Indonesia'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea North', 'Korea North'), ('Korea Sout', 'Korea South'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malaysia', 'Malaysia'), ('Malawi', 'Malawi'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Midway Islands', 'Midway Islands'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Nambia', 'Nambia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherland Antilles', 'Netherland Antilles'), ('Netherlands', 'Netherlands (Holland, Europe)'), ('Nevis', 'Nevis'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau Island', 'Palau Island'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Phillipines', 'Philippines'), ('Pitcairn Island', 'Pitcairn Island'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Republic of Montenegro', 'Republic of Montenegro'), ('Republic of Serbia', 'Republic of Serbia'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('St Barthelemy', 'St Barthelemy'), ('St Eustatius', 'St Eustatius'), ('St Helena', 'St Helena'), ('St Kitts-Nevis', 'St Kitts-Nevis'), ('St Lucia', 'St Lucia'), ('St Maarten', 'St Maarten'), ('St Pierre & Miquelon', 'St Pierre & Miquelon'), ('St Vincent & Grenadines', 'St Vincent & Grenadines'), ('Saipan', 'Saipan'), ('Samoa', 'Samoa'), ('Samoa American', 'Samoa American'), ('San Marino', 'San Marino'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tahiti', 'Tahiti'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos Is', 'Turks & Caicos Is'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('United Arab Erimates', 'United Arab Emirates'), ('United States of America', 'United States of America'), ('Uraguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City State', 'Vatican City State'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (Brit)', 'Virgin Islands (Brit)'), ('Virgin Islands (USA)', 'Virgin Islands (USA)'), ('Wake Island', 'Wake Island'), ('Wallis & Futana Is', 'Wallis & Futana Is'), ('Yemen', 'Yemen'), ('Zaire', 'Zaire'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50)),
                ('donation_received', models.CharField(max_length=100)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adp.charity')),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('payment_method', models.CharField(default='Paypal', max_length=30)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adp.charity')),
            ],
        ),
    ]
