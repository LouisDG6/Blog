"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"subject": "Study Abroad Adventure", "details": "Euro-Trip"})
        Blog.create({"subject": "Foreign English Teacher", "details": "Time in China"})
        Blog.create({"subject": "General Assembly", "details": "Software Engineering Immersive"})
        
