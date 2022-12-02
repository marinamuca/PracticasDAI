const express = require('express')
const app = express()
const port = 3000

const callback =  (req, res) => {
  res.send('Hello World!')
}
app.use(express.static('public'));
app.get('/', callback)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})