import web

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        print "Hello, world!"

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()