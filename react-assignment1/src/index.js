import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import './index.css'

function MyApp() {
    return (
      <div>
        <h1>Hello, React!</h1>
      </div>
    );  
}

ReactDOM.render(<MyApp />, document.getElementById('root'))