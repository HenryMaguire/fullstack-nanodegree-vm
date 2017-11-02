from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi # common gateway interface
# main(): instantiate our server and tell it which port to listen on

# handlder() : what code to execute based on the type of HTTP request sent to server

# Define webserverHandler class

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # pattern matching for ending of URL path
        try:
            # Look for URL that ends with '/hello'
            if self.path.endswith("/hello"):
                self.send_response(200) # successful GET
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # What will we send back to client?
                output = ""
                output += "<html><body>"
                output += "HELLO!"
                # Send message to client
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/hola"):
                self.send_response(200) # successful GET
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # What will we send back to client?
                output = ""
                output += "<html><body>"
                # Send message to client
                output += "&#161HOLA!"
                # Add post request and header tag
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" %self.path)
            print "404 ERROR"

    def do_POST(self):
        try:
            # successful post
            self.send_response(301)
            self.end_headers()
            # parse html form header (content type) into a main value and dictionary of parameters
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            # check to see if it's a form
            if ctype == 'multipart/form-data':
                # CGI collects all field in a form
                fields=cgi.parse_multipart(self.rfile, pdict)
                # Get value from fields(s) into an array
                messagecontent = fields.get('message')
            output = ''
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            # Add post request and header tag
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>"
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
