import sqlite3
import base64
import webbrowser

# Extra
import urllib.parse

conn = sqlite3.connect('week10.db')
c = conn.cursor()

userId = input("Enter user ID (1/24): ")


query = 'SELECT * FROM LAB10 WHERE id = ' + userId

for user in c.execute(query):
    decodedUrl = str(base64.b64decode( user[1] ))
    decodedUrl = decodedUrl[2:-1]
    webbrowser.open_new( decodedUrl )

# Ask the user for more information about the city
#  asks the user for name of the city and the country and updates
name        = input("What's your name: ")
cityName    = input("What's the name of that city: ")
countryName = input("What's the name of that country: ")

query = "UPDATE LAB10 SET City= '"+ cityName +"', Country = '"+ countryName +"', Student='"+ name +"' WHERE id="+ userId +""
c.execute(query)

conn.commit()



# Get all the Cities and Countries from the URLs
# Extra
# sql = 'SELECT * FROM LAB10'
# c.execute( sql )
# rows = c.fetchall()

# for user in rows:
#     decodedUrl = str(base64.b64decode( user[1] ))
#     decodedUrl = decodedUrl[2:-1]

#     cityCountry = decodedUrl[decodedUrl.index('place/') + 6:] # cut city and country
#     cityCountry = cityCountry[0 : cityCountry.index('/') ]    # finish cutting
#     cityCountry = urllib.parse.unquote(cityCountry)  # decoding URL
#     cityCountry = cityCountry.replace('+','')       # replace + for space
#     cityCountry = cityCountry.split(',')
#     print( cityCountry )

#     query = "UPDATE LAB10 SET City= '"+ str(cityCountry[0]) +"', Country = '"+ str(cityCountry[ len(cityCountry) - 1]) +"' WHERE id="+ str(user[0]) +""
#     c.execute(query)


# conn.commit()


# conn.close()




