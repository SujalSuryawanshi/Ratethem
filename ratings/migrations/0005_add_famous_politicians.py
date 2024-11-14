# ratings/migrations/0005_add_famous_politicians.py

from django.db import migrations

def add_famous_politicians(apps, schema_editor):
    Human = apps.get_model('ratings', 'Human')  # Ensure to use the correct app label
    
    politicians = [
        ("Jawaharlal Nehru", "Politician", "Former Prime Minister of India"),
        ("Sardar Vallabhbhai Patel", "Politician", "First Deputy Prime Minister of India"),
        ("Indira Gandhi", "Politician", "First and only female Prime Minister of India"),
        ("Mahatma Gandhi", "Politician", "Leader of the Indian independence movement"),
        ("Subhas Chandra Bose", "Politician", "Leader of the Indian National Army"),
        ("Dr. B.R. Ambedkar", "Politician", "Architect of the Indian Constitution"),
        ("Rajendra Prasad", "Politician", "First President of India"),
        ("Lal Bahadur Shastri", "Politician", "Second Prime Minister of India"),
        ("Atal Bihari Vajpayee", "Politician", "Former Prime Minister of India"),
        ("Vishwanath Pratap Singh", "Politician", "Former Prime Minister of India"),
        ("Manmohan Singh", "Politician", "Former Prime Minister of India"),
        ("Rajiv Gandhi", "Politician", "Former Prime Minister of India"),
        ("H. D. Deve Gowda", "Politician", "Former Prime Minister of India"),
        ("Narasimha Rao", "Politician", "Former Prime Minister of India"),
        ("K. Kamaraj", "Politician", "Indian Congress leader and former Chief Minister of Tamil Nadu"),
        ("Narendra Modi", "Politician", "Prime Minister of India"),
        ("Amit Shah", "Politician", "Home Minister of India and BJP leader"),
        ("Rahul Gandhi", "Politician", "Congress Party leader"),
        ("Sonia Gandhi", "Politician", "Congress Party President"),
        ("Arvind Kejriwal", "Politician", "Chief Minister of Delhi, Aam Aadmi Party"),
        ("Mayawati", "Politician", "Leader of Bahujan Samaj Party"),
        ("Mulayam Singh Yadav", "Politician", "Founder of Samajwadi Party"),
        ("Nitish Kumar", "Politician", "Chief Minister of Bihar, Janata Dal (United)"),
        ("Mamta Banerjee", "Politician", "Chief Minister of West Bengal, Trinamool Congress"),
        ("Sharad Pawar", "Politician", "Leader of Nationalist Congress Party"),
        ("Omar Abdullah", "Politician", "Leader of National Conference"),
        ("Tejashwi Yadav", "Politician", "Leader of Rashtriya Janata Dal"),
        ("K. Chandrashekar Rao", "Politician", "Chief Minister of Telangana, Telangana Rashtra Samithi"),
        ("Jayalalithaa", "Politician", "Former Chief Minister of Tamil Nadu"),
        ("Karunanidhi", "Politician", "Former Chief Minister of Tamil Nadu"),
        ("Bal Thackeray", "Politician", "Founder of Shiv Sena (Maharashtra)"),
        ("Prakash Singh Badal", "Politician", "Former Chief Minister of Punjab, Shiromani Akali Dal"),
        ("Biju Patnaik", "Politician", "Former Chief Minister of Odisha"),
        ("Lalu Prasad Yadav", "Politician", "Leader of Rashtriya Janata Dal"),
        ("Sushma Swaraj", "Politician", "Former External Affairs Minister"),
        ("Vasundhara Raje", "Politician", "Former Chief Minister of Rajasthan"),
        ("Rajnath Singh", "Politician", "Defence Minister of India and senior BJP leader"),
        ("P. Chidambaram", "Politician", "Senior Congress leader and former Finance Minister"),
        ("Shashi Tharoor", "Politician", "Congress leader and MP"),
    ]
    
    # Insert politicians into the database
    for name, occupation, bio in politicians:
        Human.objects.create(
            name=name,
            bio=bio,
            occupation=occupation,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),  # Make sure to reference the correct migration
    ]

    operations = [
        migrations.RunPython(add_famous_politicians),
    ]
