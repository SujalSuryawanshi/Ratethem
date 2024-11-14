# ratings/migrations/0006_add_bollywood_actors.py

from django.db import migrations

def add_bollywood_actors(apps, schema_editor):
    Human = apps.get_model('ratings', 'Human')  # Use your correct app label
    
    actors = [
        ("Amitabh Bachchan", "Actor", "Veteran actor, known for his roles in Bollywood classics."),
        ("Shah Rukh Khan", "Actor", "King of Bollywood, known for his romantic roles."),
        ("Salman Khan", "Actor", "Popular actor known for his action-packed roles."),
        ("Aamir Khan", "Actor", "Known for his versatile roles in Bollywood."),
        ("Ranbir Kapoor", "Actor", "Famous actor, known for his performances in both romantic and dramatic roles."),
        ("Ranveer Singh", "Actor", "Known for his energetic performances and diverse roles."),
        ("Hrithik Roshan", "Actor", "Actor known for his dancing skills and acting versatility."),
        ("Akshay Kumar", "Actor", "Known for his action and comic roles in Bollywood."),
        ("Ajay Devgn", "Actor", "Actor known for his roles in action and drama films."),
        ("Vicky Kaushal", "Actor", "Known for his performance in films like 'Uri' and 'Sanju'."),
        ("Varun Dhawan", "Actor", "Popular for his roles in romantic and comedy films."),
        ("Rajinikanth", "Actor", "Legendary actor from Tamil cinema, often referred to as 'Thalaivar'."),
        ("Kareena Kapoor", "Actor", "One of the most successful Bollywood actresses."),
        ("Deepika Padukone", "Actor", "Famous Bollywood actress, known for her diverse roles."),
        ("Priyanka Chopra", "Actor", "Internationally known actress and former Miss World."),
        ("Alia Bhatt", "Actor", "One of the youngest and most talented actresses in Bollywood."),
        ("Katrina Kaif", "Actor", "Known for her dance and action sequences in Bollywood."),
        ("Shraddha Kapoor", "Actor", "Popular actress known for her roles in romantic and musical films."),
        ("Jacqueline Fernandez", "Actor", "Sri Lankan actress known for her performances in Bollywood."),
        ("Sonakshi Sinha", "Actor", "Known for her roles in action films and her debut with Salman Khan."),
        ("Anushka Sharma", "Actor", "Bollywood actress and producer, known for her roles in both commercial and content-driven films."),
        ("Taapsee Pannu", "Actor", "Known for her strong performances in films like 'Pink' and 'Badla'."),
        ("Sonam Kapoor", "Actor", "Actress and fashion icon known for her roles in commercial films."),
        ("Kriti Sanon", "Actor", "Known for her roles in romantic and drama films."),
        ("Madhuri Dixit", "Actor", "Bollywood icon known for her dance moves and acting prowess."),
        ("Rani Mukerji", "Actor", "One of the most popular and respected actresses in Bollywood."),
        ("Kajol", "Actor", "Known for her on-screen chemistry with Shah Rukh Khan and her successful career."),
        ("Sridevi", "Actor", "Late legendary actress, known for her versatility and iconic performances."),
        ("Jaya Bachchan", "Actor", "Veteran actress and politician, known for her roles in Bollywood classics."),
        ("Kangana Ranaut", "Actor", "Bollywood's most versatile actress known for her roles in 'Queen' and 'Tanu Weds Manu'."),
        ("Madhubala", "Actor", "Iconic actress of Bollywood known for her beauty and acting talent."),
        ("Nargis Dutt", "Actor", "Famous actress of the 1940s and 50s, best known for her role in 'Mother India'."),
        ("Hema Malini", "Actor", "Known as the 'Dream Girl' of Bollywood for her acting and dance skills."),
        ("Waheeda Rehman", "Actor", "Known for her roles in iconic films like 'Guide' and 'Pyaasa'."),
        ("Rekha", "Actor", "One of Bollywood's most iconic actresses, known for her performances and beauty."),
    ]
    
    # Insert actors into the database
    for name, occupation, bio in actors:
        Human.objects.create(
            name=name,
            bio=bio,
            occupation=occupation,
        
        )

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_add_famous_politicians'),  # Update with your previous migration file
    ]

    operations = [
        migrations.RunPython(add_bollywood_actors),
    ]
