const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

app.get('/', async (req, res) => {
  const url = req.query.url;
  if (!url) {
    res.status(400).send('Missing "url" query parameter');
    return;
  }

  try {
    const response = await axios.get(url+'&__a=1&__d=dis');
    res.send(response.data.graphql.shortcode_media.video_url);
  } catch (error) {
    res.status(500).send(`Error fetching URL: ${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
