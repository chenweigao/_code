const http = require('http')
const urlModule = require('url')

const server = http.createServer()

server.on('request', function (req, res) {
    // const url = req.url
    const {
        pathname: url,
        query
    } = urlModule.parse(req.url, true)
    //解析出pathname 和 query

    if (url === '/getscript') {
        var data = {
            name: 'sxjiadsj',
            age: '18',
            dender: 'femal'
        }

        // var scriptStr = 'show()'
        var scriptStr = `${query.callback}(${JSON.stringify(data)})`
        res.end(scriptStr)
    } else {
        res.end('404')
    }
})

server.listen(3000, function () {
    console.log('listening at http://localhost:3000')
})