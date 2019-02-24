import uuid
import datetime
from database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter Post Content: ")
        date = input("Enter Date or leave blank for today's date")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_db()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mon(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mon(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})

        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
