# From File /app/
from app import route,pages,app

# route. ( GET POST PUT DELETE )
## 
route.GET ( "/"     , pages.home     )
route.POST( "/"     , pages.home     )
## 
route.GET ( "/login" , pages.login    )
route.POST( "/login" , pages.login    )



# Run App 
app.run(port=8010)
