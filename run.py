from blog import WriteBlog, ReadBlog, UpdateBlog, DeleteBlog
import logging


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    is_running = True
    while is_running:
        mode = input("""\n
                     Enter <c> to create a new blogpost, <r> to read an 
                     existing blog, <u> to update a blog, <d> to delete a blog 
                     or <q> to quit: """)
    
        match(mode):
            case 'q':
                is_running = False
            case 'c':
                title: str = input('Enter blog title: ')  
                author: str = input('Enter author\'s name: ')
                content: str =  input('Enter blog entry: ')  
                if title and author and content:       
                    blog = WriteBlog(title, author, content)
                    print(blog.save_blog_to_file())
                else:
                    logging.error('Enter all blog information.')
            case 'r':
                print(ReadBlog().read_blog())
            case 'u':
                update_blog = UpdateBlog('')
                print(update_blog.update_blog())
            case 'd':
                file: str = input('Enter the blog you want to delete: ')
                delete_blog = DeleteBlog(file)
                confirmation = input('This is a destructive action. Are you ' \
                'sure you want to delete %s? Enter y to proceed or n to ' \
                'terminate: ' % file)
                if confirmation == 'y' or confirmation == 'Y':
                    print(delete_blog.delete_blog())
                else:
                    pass
                
            case _:
                logging.warning('WARNING: Enter a valid mode.\n')
