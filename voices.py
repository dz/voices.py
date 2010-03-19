import sys, getopt, urlparse, cgi, socket
from subprocess import call
from wsgiref.util import setup_testing_defaults, request_uri
from wsgiref.simple_server import make_server

voices = ["alex", "bruce", "fred", "junior", "ralph", "agnes", "kathy", "princess","vicki", "victoria", "albert", "bad news" , "bahh", "bells", "boing","bubbles", "cellos", "deranged", "good news", "hysterical", "pipe organ", "trinoids", "whisper", "zarvox"]

def voices_server(environ, start_response):
    setup_testing_defaults(environ)
    start_response('200 OK', [('Content-type', 'text/html')])
    qs = cgi.parse_qs(urlparse.urlparse(request_uri(environ, True)).query or "")
    voice, message = (qs.get('v') and qs['v'][0] or "",qs.get('m') and qs['m'][0] or "")
    response_message = ""
    if voice and message: 
        call(['say', '-v', '%s' % voice, '%s' % message])
        response_message = "<i>Say command sent.</i><br /><br />"
    return """%s<form action="" method="get">Voice: <select name="v">%s</select><br/><br />
            message:<br/><textarea style="height: 100px; width:400px;" name="m">%s</textarea>
            <input type="submit" value="speak" /></form>
            """ % (response_message, ''.join(['<option valu="%s" %s>%s</option>\n' % (voice, (voice==v and "selected" or ""), v.title()) for v in voices]), message)
            
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg, "for help use --help"
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            print "Usage: python voices.py x.x.x.x:port\n"
            sys.exit(0)
    if len(args) > 1: 
        print "incorrect usage. for help use --help"
        sys.exit(2)
    if len(args) == 1:
        ip, port = args[0].split(':')
    else:
        print "Explicit IP and port not entered.  Attempted to autodiscover IP address."
        ip, port = (socket.gethostbyname(socket.gethostname()), 8888)
    httpd = make_server(ip, int(port), voices_server)
    print "Serving on %s:%s" % (ip, port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    main()
