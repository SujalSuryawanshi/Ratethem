from django.db import migrations

def add_bollywood_actors(apps, schema_editor):
    Human = apps.get_model('ratings', 'Human')  # Get the Human model
    Category = apps.get_model('ratings', 'Category')  # Get the Category model

    # Ensure the "Actor" category exists or create it
    actor_category, created= Category.objects.get_or_create(name="Actor")

    actors = [
        ("Amitabh Bachchan", "Veteran actor, known for his roles in Bollywood classics."),
        ("Shah Rukh Khan", "King of Bollywood, known for his romantic roles."),
        ("Salman Khan", "Popular actor known for his action-packed roles."),
        ("Aamir Khan", "Known for his versatile roles in Bollywood."),
        ("Ranbir Kapoor", "Famous actor, known for his performances in both romantic and dramatic roles."),
        ("Ranveer Singh", "Known for his energetic performances and diverse roles."),
        ("Hrithik Roshan", "Actor known for his dancing skills and acting versatility."),
        ("Akshay Kumar", "Known for his action and comic roles in Bollywood."),
        ("Ajay Devgn", "Actor known for his roles in action and drama films."),
        ("Vicky Kaushal", "Known for his performance in films like 'Uri' and 'Sanju'."),
        ("Varun Dhawan", "Popular for his roles in romantic and comedy films."),
        ("Rajinikanth", "Legendary actor from Tamil cinema, often referred to as 'Thalaivar'."),
        ("Kareena Kapoor", "One of the most successful Bollywood actresses."),
        ("Deepika Padukone", "Famous Bollywood actress, known for her diverse roles."),
        ("Priyanka Chopra", "Internationally known actress and former Miss World."),
        ("Alia Bhatt", "One of the youngest and most talented actresses in Bollywood."),
        ("Katrina Kaif", "Known for her dance and action sequences in Bollywood."),
        ("Shraddha Kapoor", "Popular actress known for her roles in romantic and musical films."),
        ("Jacqueline Fernandez", "Sri Lankan actress known for her performances in Bollywood."),
        ("Sonakshi Sinha", "Known for her roles in action films and her debut with Salman Khan."),
        ("Anushka Sharma", "Bollywood actress and producer, known for her roles in both commercial and content-driven films."),
        ("Taapsee Pannu", "Known for her strong performances in films like 'Pink' and 'Badla'."),
        ("Sonam Kapoor", "Actress and fashion icon known for her roles in commercial films."),
        ("Kriti Sanon", "Known for her roles in romantic and drama films."),
        ("Madhuri Dixit", "Bollywood icon known for her dance moves and acting prowess."),
        ("Rani Mukerji", "One of the most popular and respected actresses in Bollywood."),
        ("Kajol", "Known for her on-screen chemistry with Shah Rukh Khan and her successful career."),
        ("Sridevi", "Late legendary actress, known for her versatility and iconic performances."),
        ("Jaya Bachchan", "Veteran actress and politician, known for her roles in Bollywood classics."),
        ("Kangana Ranaut", "Bollywood's most versatile actress known for her roles in 'Queen' and 'Tanu Weds Manu'."),
        ("Madhubala", "Iconic actress of Bollywood known for her beauty and acting talent."),
        ("Nargis Dutt", "Famous actress of the 1940s and 50s, best known for her role in 'Mother India'."),
        ("Hema Malini", "Known as the 'Dream Girl' of Bollywood for her acting and dance skills."),
        ("Waheeda Rehman", "Known for her roles in iconic films like 'Guide' and 'Pyaasa'."),
        ("Rekha", "One of Bollywood's most iconic actresses, known for her performances and beauty."),
    ]

    # Insert actors into the database
    for name, bio in actors:
        Human.objects.create(
            name=name,
            bio=bio,
            category=actor_category,  # Reference the Actor category
        )

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_add_famous_politicians'),  # Update with your previous migration file
    ]

    operations = [
        migrations.RunPython(add_bollywood_actors),
    ]
