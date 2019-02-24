from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        self.user = input("Enter your author name")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome Back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mon(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter a title: ")
        description = input("Enter a blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mon()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to Read(R) or write(W) blogs?")
        if read_or_write == 'R':
            self._list_blogs(self.user)
            self._view_blogs()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you!")

    def _list_blogs(self, name):
        blogs = Database.find(collection='blogs',
                              query={'author': name})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mon(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
