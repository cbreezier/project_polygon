import webapp2
import jinja2
import cgi
import re
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True,
    trim_blocks=True)


class GitHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('git.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([('/git',GitHandler)], debug=True)