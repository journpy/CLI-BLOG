from blog import WriteBlog, ReadBlog, UpdateBlog
import logging


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    is_running = True
    while is_running:
        mode = input("""\nEnter <n> to create a new blogpost, <r> to read an 
                     existing blog, <u> to update a blog or <q> to quit: """)
    
        match(mode):
            case 'q':
                is_running = False
            case 'n':
                title: str = input('Enter blog title: ')  
                author: str = input('Enter author\'s name: ')
                content: str =  input('Enter blog entry: ')  
                if title and author and content:       
                    blog = WriteBlog(title, author, content)
                    print(blog.save_blog_to_file())
                    logging.info(f'SUCCESS:{title} blog successfully created and saved.\n')
                else:
                    logging.warning('WARNING:Enter all blog information.')
            case 'r':
                print(ReadBlog().read_blog())
            case 'u':
                update_blog = UpdateBlog('')
                print(update_blog.update_blog())
            case _:
                logging.warning('WARNING: Enter a valid mode.\n')
