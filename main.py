import webapp2


# handlers
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello, SmartNinja!')


# URLs
app = webapp2.WSGIApplication([
    webapp2.Route('/', HelloWebapp2),
], debug=True)


# run the server
def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
