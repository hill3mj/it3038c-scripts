var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

var server = http.createServer(function(req, res){

    if(req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(err,body){
        res.writeHead(200, {"Content-Type": "text/html"})
        res.end(body)

        })

    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        days = os.uptime() / 86400 
        hours = os.uptime() % 86400 / 3600
        minutes = os.uptime() % 86400 % 3600 / 60
        seconds = os.uptime() % 86400 % 3600 % 60   
        
        html=`
            <!DOCTYPE html>
            <html>
            <head>
            <title> Node JS Response </title>
            </head>
            <body>
            <p> Hostname: ${myHostName}</p>
            <p> IP: ${ip.address()}</p>
            <p> Server Uptime: Days: ${parseInt(days)}, Hours: ${parseInt(hours)}, Minutes: ${parseInt(minutes)}, Seconds: ${parseInt(seconds)}
            <p> Total Memory: ${os.totalmem() / 1000000} MB</p>
            <p> Free Memory: ${os.freemem() / 1000000} MB</p>
            <p> Number of CPUs: ${os.cpus().length}</p>
            </body>
            </html>
            
            
            `
            res.writeHead(200, {"Content-Type":"text/html"})
            res.end(html)
    }

    else{
        res.writehead(404, {"Content-Type": "text/plain"})
        res.end(`404 File Not Found at ${req.url}`)

    }
})
server.listen(3000)

console.log("Server listening on port 3000")