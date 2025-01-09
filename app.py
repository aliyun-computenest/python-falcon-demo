import os
import falcon
from wsgiref import simple_server

class HelloWorldResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Hello, World!'

# Create the Falcon application
app = falcon.App()

# Add a route to the application
hello_world = HelloWorldResource()
app.add_route('/', hello_world)

if __name__ == '__main__':
    # Get port from environment variable or default to 80
    port = int(os.environ.get('PORT', 80))

    # Create and start the server
    with simple_server.make_server('', port, app) as httpd:
        print(f'Serving on port {port}...')
        httpd.serve_forever()
