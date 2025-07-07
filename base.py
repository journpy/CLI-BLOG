from abc import ABC, abstractmethod
from datetime import datetime


class BaseWriteBlog(ABC):
    """Abstract Base Class"""
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
        self.date_created: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    @abstractmethod
    def save_blog_to_file(self):
        """Save blog to file."""
        pass


class BaseReadBlog(ABC):
    
    @abstractmethod
    def read_blog(self):
        """Read Blog"""
        pass


class BaseUpdateBlog(ABC):
    def __init__(self, file: str):
        self.file = file

    @abstractmethod
    def update_blog(self):
        """Update blog post."""
        pass

class BaseDeleteBlog(ABC):
    def __init__(self, file: str):
        self.file = file

    @abstractmethod
    def delete_blog(self):
        """Delete a Blog file"""
        pass






        