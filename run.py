__author__ = 'donal'
__project__ = 'ribcage'


from app import create_app

# app = create_app('development')
app = create_app('production')

if __name__ == '__main__':
    app.run()