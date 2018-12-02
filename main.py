import webapp2


# handlers
class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello, SmartNinja!')


# URLs
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)


# run the localhost server
localhost = True  # change to False before deploying to Google Cloud (GAE)
if localhost:
    def main():
        from paste import httpserver
        httpserver.serve(app, host='localhost', port='8080')


    if __name__ == '__main__':
        main()
