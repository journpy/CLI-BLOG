from base import BaseWriteBlog, BaseReadBlog, BaseUpdateBlog, BaseDeleteBlog
from datetime import datetime
from typing import List, Any
import logging
import os


logging.basicConfig(level='INFO')

class WriteBlog(BaseWriteBlog):
    """Model a Blog Post"""
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
        self.date_created: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        #self.comments: str = ''
        self.DIR: str = 'blogs'
        self.EXT: str = '.txt'
        super().__init__(title, author, content)

    def save_blog_to_file(self) ->Any:
        file = input('Enter File name: ')
        with open(self.DIR + '/' + file + self.EXT, 'w') as file_object:
            lines: List[str] = ['Title: %s'%self.title, 'Author: %s'%self.author, 'Body: %s'%self.content, 'Date/Time: %s'%self.date_created]
            for line in lines:
                file_object.write('%s\n'%line)
        return f'{self.title} successfully created and saved.\n'
               
        
class ReadBlog(BaseReadBlog):
    """Read a Blog"""
    @classmethod
    def read_blog(cls) ->Any:
        file = input('\nEnter File name with extension: ')
        try:
            with open(file, 'r+') as file_object:
                logging.info('Blog read successful.\n')
                return file_object.read()
        except FileNotFoundError:
            return f'\nThe requested file {file} wasn\'t found on our system.'
        

class UpdateBlog(BaseUpdateBlog):
    """Update a Blog."""
    def __init__(self, file):
        self.file = file
        self.date_updated = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        super().__init__(file)

    def update_blog(self) ->Any:
        self.file = input('Enter the name of the file you want to update with extension: ')
        if os.path.exists(self.file):
            if os.path.isfile(self.file):   
                with open(self.file, 'a') as file_object:
                    post = input('Enter post to update blog: ')
                    file_object.writelines(f'\n{self.date_updated}\n{post}\n')
                    return 'Blog update successful'
            else:
                return 'Enter the correct file name'
        else:
            return 'File %s does not exist.' % self.file
        
    
class DeleteBlog(BaseDeleteBlog):
    """Delete a blog"""
    def __init__(self, file):
        self.file = file
    
    def delete_blog(self):
        try:
            os.remove(self.file)
        except FileNotFoundError:
            return 'The requested blog - %s does not exist.' % self.file
        else:
            logging.info('%s successfully deleted.' % self.file)
            return ''

        
           

       

