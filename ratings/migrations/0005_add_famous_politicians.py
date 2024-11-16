from django.db import migrations

def add_famous_politicians(apps, schema_editor):
    # Get the models dynamically to support historical migrations
    Human = apps.get_model('ratings', 'Human')
    Category = apps.get_model('ratings', 'Category')

    # Ensure the "Politician" category exists
    politician_category, created = Category.objects.get_or_create(name="Politician")

    politicians = [
        ("Jawaharlal Nehru", "Former Prime Minister of India"),
        ("Sardar Vallabhbhai Patel", "First Deputy Prime Minister of India"),
        ("Indira Gandhi", "First and only female Prime Minister of India"),
        ("Mahatma Gandhi", "Leader of the Indian independence movement"),
        ("Subhas Chandra Bose", "Leader of the Indian National Army"),
        ("Dr. B.R. Ambedkar", "Architect of the Indian Constitution"),
        ("Rajendra Prasad", "First President of India"),
        ("Lal Bahadur Shastri", "Second Prime Minister of India"),
        ("Atal Bihari Vajpayee", "Former Prime Minister of India"),
        ("Vishwanath Pratap Singh", "Former Prime Minister of India"),
        ("Manmohan Singh", "Former Prime Minister of India"),
        ("Rajiv Gandhi", "Former Prime Minister of India"),
        ("H. D. Deve Gowda", "Former Prime Minister of India"),
        ("Narasimha Rao", "Former Prime Minister of India"),
        ("K. Kamaraj", "Indian Congress leader and former Chief Minister of Tamil Nadu"),
        ("Narendra Modi", "Prime Minister of India"),
        ("Amit Shah", "Home Minister of India and BJP leader"),
        ("Rahul Gandhi", "Congress Party leader"),
        ("Sonia Gandhi", "Congress Party President"),
        ("Arvind Kejriwal", "Chief Minister of Delhi, Aam Aadmi Party"),
        ("Mayawati", "Leader of Bahujan Samaj Party"),
        ("Mulayam Singh Yadav", "Founder of Samajwadi Party"),
        ("Nitish Kumar", "Chief Minister of Bihar, Janata Dal (United)"),
        ("Mamta Banerjee", "Chief Minister of West Bengal, Trinamool Congress"),
        ("Sharad Pawar", "Leader of Nationalist Congress Party"),
        ("Omar Abdullah", "Leader of National Conference"),
        ("Tejashwi Yadav", "Leader of Rashtriya Janata Dal"),
        ("K. Chandrashekar Rao", "Chief Minister of Telangana, Telangana Rashtra Samithi"),
        ("Jayalalithaa", "Former Chief Minister of Tamil Nadu"),
        ("Karunanidhi", "Former Chief Minister of Tamil Nadu"),
        ("Bal Thackeray", "Founder of Shiv Sena (Maharashtra)"),
        ("Prakash Singh Badal", "Former Chief Minister of Punjab, Shiromani Akali Dal"),
        ("Biju Patnaik", "Former Chief Minister of Odisha"),
        ("Lalu Prasad Yadav", "Leader of Rashtriya Janata Dal"),
        ("Sushma Swaraj", "Former External Affairs Minister"),
        ("Vasundhara Raje", "Former Chief Minister of Rajasthan"),
        ("Rajnath Singh", "Defence Minister of India and senior BJP leader"),
        ("P. Chidambaram", "Senior Congress leader and former Finance Minister"),
        ("Shashi Tharoor", "Congress leader and MP"),
    ]
    
    # Insert politicians into the database
    for name, bio in politicians:
        Human.objects.create(
            name=name,
            bio=bio,
            category=politician_category,  # Assign the Category instance here
        )

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),  # Update this if your latest migration has a different name
    ]

    operations = [
        migrations.RunPython(add_famous_politicians),
    ]
