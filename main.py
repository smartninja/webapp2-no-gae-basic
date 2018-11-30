import webapp2
from paste import httpserver


# handlers
class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello, SmartNinja!')


# URLs
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)


# run the server
def main():
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
