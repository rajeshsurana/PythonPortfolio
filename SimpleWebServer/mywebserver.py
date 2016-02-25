from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
  
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'>Create New Restaurant</a></br>"
                for restaurant in restaurants:
                    output +="<p>"
                    output += restaurant.name+"<br/>"
                    output += '''<a href='/restaurant/%s/edit'>Edit</a><br/>''' % restaurant.id
                    output += "<a href='/restaurant/%s/delete'>Delete</a>" % restaurant.id
                    output += "</p>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Create New Restaurant</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name="restaurantName" type="text" placeholder="Enter name of restaurant"><input type="submit" value="Submit"></form>'''
                output += "<br/>&nbsp;<br/><a href='/restaurants'> View Restaurants </a>"
                output += "</body><html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/edit'):
                restaurantID = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=int(restaurantID)).one()
                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += restaurantQuery.name + "<br/>"
                    output += '''<form method='POST' enctype='multipart/form-data' action='%s'><input name="restaurantName" type="text" placeholder="%s"><input type="submit" value="Rename"></form>'''% (self.path, restaurantQuery.name)
                    output += "<br/><a href='/restaurants'> View Restaurants </a>" 
                    output += "</body><html>"
                    self.wfile.write(output)
                    print output
                    return

            if self.path.endswith('/delete'):
                restaurantID = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=int(restaurantID)).one()
                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h2>Are you sure you want to delete?</h2>"
                    output += restaurantQuery.name + "<br/>"
                    output += '''<form method='POST' enctype='multipart/form-data' action='%s'><input type="submit" value="Detete"></form>'''% self.path
                    output += "<br/><a href='/restaurants'> View Restaurants </a>" 
                    output += "</body><html>"
                    self.wfile.write(output)
                    print output
                    return

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(message)
                print message
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):

        if self.path.endswith('/delete'):
            try:
                restaurantID = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()
                if restaurantQuery:
                    session.delete(restaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header("Content-type", "text/html")
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
                    return
            except:
                self.send_error(404, 'Invalid Request')

        if self.path.endswith('/edit'):
            try:
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('restaurantName')
                    restaurantNewName = Restaurant(name=messagecontent[0])
                    restaurantID = self.path.split("/")[2]
                    restaurantQuery = session.query(Restaurant).filter_by(id=int(restaurantID)).one()
                    if restaurantQuery:
                        restaurantQuery.name = messagecontent[0]
                        session.add(restaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header("Content-type", "text/html")
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
                        return
            except:
                self.send_error(404, 'Invalid Request')

        if self.path.endswith('/restaurants/new'):
            try:
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('restaurantName')
                    restaurant = Restaurant(name=messagecontent[0])
                    session.add(restaurant)
                    session.commit()
                output = ""
                output += "<html><body>"
                output += "<h1>Create New Restaurant</h1>"
                output += "<p><div style='background-color:lightgreen;display: inline-block'>Successfully added restaurant: %s</div></p>" % messagecontent[0]
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name="restaurantName" type="text" placeholder="Enter name of restaurant"><input type="submit" value="Submit"></form>'''
                output += "<br/>&nbsp;<br/><a href='/restaurants'> View Restaurants </a>"
                output += "</body></html>"
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(output)
                print output 
            except:
                self.send_error(404, 'Invalid Request')

        if self.path.endswith("/hello"):
            try:
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                output = ""
                output += "<html><body>"
                output += " <h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
            except:
                self.send_error(404, 'Invalid Request')


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
