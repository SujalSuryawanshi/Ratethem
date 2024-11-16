# ratings/migrations/0007_add_indian_historians.py

from django.db import migrations

def add_indian_historians(apps, schema_editor):
    Human = apps.get_model('ratings', 'Human') 
    Category = apps.get_model('ratings', 'Category')
    historian_category, created = Category.objects.get_or_create(name="Historian")
    singer_cat,created=Category.objects.get_or_create(name="Singer")
    historians = [
        ("Romila Thapar", "Historian", "Eminent historian specializing in ancient Indian history."),
        ("Bipin Chandra", "Historian", "Prominent historian known for his works on modern Indian history."),
        ("K.K Aziz", "Historian", "Famous historian known for his works on the history of Pakistan and India."),
        ("Irfan Habib", "Historian", "Renowned historian and Marxist scholar specializing in medieval Indian history."),
        ("S. Irfan Habib", "Historian", "Well-known historian who has written extensively on medieval Indian history."),
        ("A. L. Basham", "Historian", "Famous for his work on Ancient India and a major figure in Indian history studies."),
        ("Sheldon Pollock", "Historian", "Renowned scholar of classical Indian literature and history."),
        ("K.K. Aziz", "Historian", "Known for his book *The Murder of History* focusing on partition history."),
        ("Mushirul Hasan", "Historian", "Famous historian and former director of the National Archives of India."),
        ("Subhas Chandra Bose", "Historian", "A major figure in India's struggle for independence."),
        ("R.C. Majumdar", "Historian", "A prominent historian known for his works on Ancient and Modern Indian History."),
        ("M. A. Ghanem", "Historian", "Noted for his work on colonial history."),
        ("B.N. Puri", "Historian", "One of the famous scholars in Indian history."),
        ("D. D. Kosambi", "Historian", "Renowned scholar in ancient Indian history and a Marxist historian."),
        ("L. K. Jha", "Historian", "Well-known historian and economist."),
        ("A.K. Ramanujan", "Historian", "Famous scholar of classical history and literature."),
        ("Sailendra Nath Sen", "Historian", "Renowned historian known for his works on ancient Indian history."),
    ]
    indian_singers = [
        ("Lata Mangeshkar", "Singer", "Legendary playback singer known as the 'Nightingale of India.'"),
        ("Kishore Kumar", "Singer", "Famous playback singer, actor, and music director."),
        ("Mohammad Rafi", "Singer", "One of the greatest playback singers in the history of Indian cinema."),
        ("Mukesh", "Singer", "Famous playback singer known for his soulful voice."),
        ("Asha Bhosle", "Singer", "Renowned playback singer with a career spanning six decades."),
        ("Sonu Nigam", "Singer", "Famous playback singer and music director."),
        ("Arijit Singh", "Singer", "Modern-day playback singer known for his soulful voice."),
        ("Shreya Ghoshal", "Singer", "Popular playback singer known for her versatile voice."),
        ("Kumar Sanu", "Singer", "Playback singer known for his voice in 90s Bollywood music."),
        ("Alka Yagnik", "Singer", "Famous playback singer known for many hit songs in the 90s."),
        ("Neha Kakkar", "Singer", "Popular playback singer known for her lively and catchy voice."),
        ("Javed Ali", "Singer", "Famous playback singer known for his romantic and soulful songs."),
        ("Udit Narayan", "Singer", "Renowned playback singer famous for 90s Bollywood songs."),
        ("Pankaj Udhas", "Singer", "Famous ghazal singer with a huge fan following."),
        ("Kailasa Kher", "Singer", "Famous for his unique voice and music with Kailasa band."),
        ("Hariharan", "Singer", "Playback singer known for his soulful voice."),
        ("Shaan", "Singer", "Popular playback singer known for his versatility."),
        ("Kavita Krishnamurthy", "Singer", "Playback singer known for her classical training."),
        ("Sadhana Sargam", "Singer", "Playback singer known for her melodious voice."),
        ("Srinivas", "Singer", "Famous playback singer known for his work in Tamil and Telugu."),
        ("Benny Dayal", "Singer", "Famous playback singer known for his peppy voice."),
        ("Pritam Chakraborty", "Singer", "Famous music director and playback singer."),
        ("Shankar Mahadevan", "Singer", "Famous playback singer known for his classical and contemporary styles."),
        ("Suresh Wadkar", "Singer", "Playback singer known for his contributions to Bollywood music."),
        ("Kunal Ganjawala", "Singer", "Famous playback singer with a soulful voice."),
        ("Sushmita Sen", "Singer", "Known for her playback singing and acting career."),
        ("Anuradha Paudwal", "Singer", "Famous playback singer known for devotional and Bollywood songs."),
        ("Sudesh Bhosle", "Singer", "Playback singer known for his mimicry and singing."),
        ("Vani Jairam", "Singer", "Famous playback singer known for classical and devotional songs."),
        ("Manna Dey", "Singer", "One of the greatest playback singers of his time."),
        ("Urmila Matondkar", "Singer", "Famous for her playback singing and Bollywood acting."),
        ("Tulsi Kumar", "Singer", "Famous playback singer known for her melodious voice."),
        ("Shruti Haasan", "Singer", "Playback singer and actress known for her Tamil and Telugu songs."),
        ("Shreya Ghoshal", "Singer", "One of the most celebrated playback singers of India."),
        ("Harshdeep Kaur", "Singer", "Playback singer known for her soulful voice."),
        ("Sunidhi Chauhan", "Singer", "Famous playback singer known for her energetic and versatile voice."),
        ("Nandini Srikar", "Singer", "Playback singer known for her classical and contemporary voice."),
        ("Richa Sharma", "Singer", "Playback singer known for her powerful voice."),
        ("Shaan", "Singer", "Famous for his melodious voice and versatility."),
        ("Adnan Sami", "Singer", "Popular playback singer known for his energetic performances."),
        ("Kailash Kher", "Singer", "Renowned for his unique and soulful voice."),
        ("Zubeen Garg", "Singer", "Famous for his work in Assamese and Hindi film music."),
        ("Jaspreet Singh", "Singer", "Renowned playback singer known for his classical singing."),
        ("Sonu Nigam", "Singer", "One of the most versatile and popular playback singers in India."),
        ("Kavita Krishnamurthy", "Singer", "Playback singer known for her classical and modern music."),
        ("Anup Jalota", "Singer", "Famous bhajan and ghazal singer."),
        ("Ravindra Jain", "Singer", "Known for his devotional and Bollywood songs."),
        ("Mohammed Aziz", "Singer", "Playback singer popular in the 80s and 90s."),
        ("Nitin Mukesh", "Singer", "Playback singer known for his work in Bollywood."),
        ("Daler Mehndi", "Singer", "Famous Punjabi singer known for his energetic music."),
        ("Jasleen Royal", "Singer", "Famous playback singer known for her unique voice and compositions."),
        ("Atif Aslam", "Singer", "Popular Pakistani singer known for his Bollywood hits."),
        ("Himesh Reshammiya", "Singer", "Famous music director and playback singer."),
        ("Papon", "Singer", "Famous for his soulful voice in Bollywood and Assamese music."),
        ("Vishal-Shekhar", "Singer", "Music duo and singers known for their work in Bollywood."),
        ("Babul Supriyo", "Singer", "Famous playback singer known for his Bollywood hits."),
        ("Gurdas Maan", "Singer", "Legendary Punjabi singer and songwriter."),
        ("Amrinder Gill", "Singer", "Famous Punjabi playback singer and actor."),
        ("Asha Bhosle", "Singer", "Playback singer known for her versatility in Bollywood."),
        ("Ghulam Ali", "Singer", "Famous ghazal singer known for his soulful voice."),
        ("Kishore Kumar", "Singer", "One of the most iconic playback singers of India."),
        # Continue adding up to 100 Indian singers...
    ]
    
    # List of Famous International Singers (100)
    international_singers = [
        ("Michael Jackson", "Singer", "Known as the 'King of Pop.'"),
        ("Elvis Presley", "Singer", "The 'King of Rock and Roll.'"),
        ("Adele", "Singer", "Famous British singer known for her soulful voice."),
        ("Beyoncé", "Singer", "One of the world's top singers and performers."),
        ("Whitney Houston", "Singer", "Known for her powerful voice."),
        ("Celine Dion", "Singer", "Renowned for her ballads and powerful voice."),
        ("Ed Sheeran", "Singer", "Popular British singer and songwriter."),
        ("Shakira", "Singer", "Famous Colombian singer known for her dance and unique voice."),
        ("Lady Gaga", "Singer", "Renowned for her pop music and vocal versatility."),
        ("Freddie Mercury", "Singer", "Legendary singer of Queen known for his operatic vocal style."),
        ("Elton John", "Singer", "Renowned British singer, songwriter, and pianist."),
        ("Stevie Wonder", "Singer", "Known for his soulful voice and music."),
        ("Aretha Franklin", "Singer", "The Queen of Soul."),
        ("Mariah Carey", "Singer", "Famous for her powerful and wide vocal range."),
        ("John Lennon", "Singer", "Famous member of The Beatles and solo artist."),
        ("Paul McCartney", "Singer", "Famous member of The Beatles and solo artist."),
        ("Prince", "Singer", "Legendary musician known for his innovative music."),
        ("Billie Eilish", "Singer", "Popular contemporary pop singer known for her unique voice."),
        ("Taylor Swift", "Singer", "Famous for her storytelling lyrics and country-pop crossover."),
        ("Frank Sinatra", "Singer", "One of the most iconic American singers of all time."),
        ("Janet Jackson", "Singer", "Pop and R&B singer known for her music and performance style."),
        ("Bruce Springsteen", "Singer", "Famous for his rock music and storytelling."),
        ("David Bowie", "Singer", "Renowned for his experimental music and innovative style."),
        ("Lady Gaga", "Singer", "Known for her eclectic style and pop hits."),
        ("Ed Sheeran", "Singer", "Singer-songwriter known for his catchy melodies."),
        ("Shawn Mendes", "Singer", "Famous pop singer known for his heartfelt lyrics."),
        ("Ariana Grande", "Singer", "Famous for her powerful voice and pop hits."),
        ("P!nk", "Singer", "Known for her edgy pop songs and powerhouse vocals."),
        ("Usher", "Singer", "R&B singer known for his smooth voice."),
        ("Drake", "Singer", "Popular Canadian rapper and singer."),
        ("The Weeknd", "Singer", "Known for his unique style of R&B and pop music."),
        ("Sam Smith", "Singer", "Known for their soulful ballads."),
        # Continue adding up to 100 international singers...
    ]
    
    # Add Indian Singers to the database
    for name, category, bio in indian_singers:
        Human.objects.create(name=name, category=singer_cat, bio=bio)
    
    # Add International Singers to the database
    for name, category, bio in international_singers:
        Human.objects.create(name=name, category=singer_cat, bio=bio)
    # Insert historians into the database
    for name, category, bio in historians:
        Human.objects.create(
            name=name,
            bio=bio,
            category=historian_category,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '006_add_bollywood_actors'),  # Update with the previous migration file
    ]

    operations = [
        migrations.RunPython(add_indian_historians),
    ]
