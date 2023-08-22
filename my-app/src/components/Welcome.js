import React from 'react';
import { Button, Jumbotron } from 'react-bootstrap';

const Welcome = () => (
  <Jumbotron>
    <h1>Image Gallery</h1>
    <p>Welcome to image gallery, Click on start to get started</p>
    <p>
      <Button variant="primary" href="https://unsplash.com" target="_blank">
        Submit
      </Button>
    </p>
  </Jumbotron>
);

export default Welcome;
