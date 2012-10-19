import os
import webapp2
import jinja2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        values = {}
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(values))


app = webapp2.WSGIApplication([('/', MainPage)],  debug=True)
