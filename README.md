# genczml

generate CZML from track and windy traj forecast like so:

genczml -t 20210925-Stiwoll-Stallhofen.gpx  -T trajectory__2021-09-25T05_00_00.gpx >20210925-Stiwoll-Stallhofen.czml

upload result to a webserver with CORS headers enabled:


https://static.mah.priv.at/cors/20210925-Stiwoll-Stallhofen.czml


run like so:

https://static.mah.priv.at/apps/flightview2/?=&source=https%3A%2F%2Fstatic.mah.priv.at%2Fcors%2F20210925-Stiwoll-Stallhofen.czml&view=15.21038771704882%2C47.11010758194734%2C725.2675419217751%2C142.3832256828982%2C-17.93372195941751%2C0.00001394508617578102&multiplier=11&startAt=212.54794962202868&imagery=0&terrain=3&autostart=true


status: undocumented and terminally ugly. You have been warned.
