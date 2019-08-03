import pdfkit

options = { 'encoding': "UTF-8" }  
# pdfkit.from_url(r'http://localhost:8080/123.html', 'article3.pdf', options=options)
pdfkit.from_url(r'www.baidu.com', 'article3.pdf', options=options)


# pdfkit.from_string('This is a Picture <img src="http://192.168.0.34:8080/pic/165bdfeec62b21fc" /> <img src="http://pic1.win4000.com/pic/a/be/daa075518e.jpg" />', '123.pdf')

# http://localhost:8080/pic/165bdfeec62b21fc
