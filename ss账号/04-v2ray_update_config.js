const fs = require('fs')
const Hjson = require('hjson')
var http = require('http');
const https = require('https');
const xpath = require('xpath')
const dom = require('xmldom').DOMParser

// 用于请求的选项
var options = {
   host: 'https://free.ishadowx.biz/',
   port: '8080',
   path: '/index.html'
};


https.get(options.host, (res) => {
   res.on('data', (d) => {
      const html = d.toString()
      let doc = new dom().parseFromString(html)

      const cards = xpath.select('//div[@class="hover-text"]', doc)
      const servers = []
      cards.forEach(item => {
         let el = {}
         const address = xpath.select('./h4[1]/span/text()', item).toString().trim()
         const port = xpath.select('./h4[2]/span/text()', item).toString().trim()
         const password = xpath.select('./h4[3]/span/text()', item).toString().trim()
         const method = xpath.select('./h4[4]/text()', item).toString().trim().substring(7)

         el = {
            address, port: parseInt(port), password, method
         }
         servers.push(el)
      })

      fs.readFile('/usr/local/etc/v2ray/config.json', (err, data) => {
         if (!err) {
            const config = Hjson.parse(data.toString())
            console.log(config.outbounds)
            config.outbounds[0].servers = servers
            const outbounds = [{
               "protocol": "shadowsocks",
               "settings": {
                  servers
               }

            }]
            config.outbounds = outbounds
            const data1 = JSON.stringify(config)
            fs.writeFile('/Users/jack/config.json', data1, (e) => console.log(e))
         } else {
            console.log('读取文件异常！')
         }
      })

   });

}).on('error', (e) => {
   console.error(e);
});



