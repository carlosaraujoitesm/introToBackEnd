
"""
Webapp2 is a lightweight Python web framework compatible with Google App Engine's webapp. webapp2 is a
simple. it follows the simplicity of webapp, but improves it in some ways: it adds better URI routing 
and exception handling, 
a full featured response object and a more flexible dispatching mechanism.
"""
import webapp2
import cgi

form = """
<form method="post"> 
      What is your birthday?
      <br>

      <label>  Month
          <input type="text" name="month" value="%(month)s">
      </label>

      <label>Day
          <input type="text" name="day" value="%(day)s">
      </label>

      <label> Year
          <input type="text" name="year" value="%(year)s">
      </label>
      <div style="color: red">%(error)s</div>
      <br>
      <br>
      <input type="submit">
</form> 
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(),m) for m in months)  

class IndexPageHandler(webapp2.RequestHandler):
  
  def write_form(self,error="",month="",day="",year=""):
      self.response.out.write(form % {"error": error,
                                      "month": month,
                                      "day": day,
                                      "year": year})
  
  def get(self):
      self.write_form()

  def post(self):



      user_month = self.request.get('month')
      user_day =   self.request.get('day')
      user_year =  self.request.get('year')

      month = self.valid_month(user_month)
      day = self.valid_day(user_day)
      year = self.valid_year(user_year)

      if not(month and day and year):
        self.write_form("That does not seem valid",self.escape_html(user_month),self.escape_html(user_day),self.escape_html(user_year))
      else:
         self.response.out.write("Thanks that's totally valid function!!!")

  def valid_day(self,day):

    if day and day.isdigit():
      day = int(day)
      if day > 0 and day <= 31:
        return day
   
  def valid_month(self,month):

    if month:
      short_month = month[:3].lower()
      return month_abbvs.get(short_month)


  def valid_year(self,year):

    if year and year.isdigit():
      year = int(year)
      if year > 1900 and year <= 2020:
        return year

  def escape_html(self,s):
    return cgi.escape(s,quote = True)
    for(i,o) in (("&","&amp;"),
                 (">","&gt;"),
                 ("<","&lt;"),
                 ("","&quot;")) :
       s = s.replace(i,o)
    return s
    
    
app = webapp2.WSGIApplication([('/', IndexPageHandler)],
                              debug=True)
