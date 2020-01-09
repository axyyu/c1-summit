import React from 'react'
import '../../styles/styles.css'
import Search from './search.js'
import Suggestion from './Suggestion.js'
import GoogleMap from './GoogleMap.js'

const searchBar = {
  marginTop: '100px',
  marginBottom: '100px'
};

const map = {
  display: 'inline-block',
  marginRight: '40px'
}

function App() {
    return (
      <div style={{ textAlign:"center" }}>
         <Search style={{searchBar}} placeholder='Who are you going with?'/>
         <Search style={{searchBar}} placeholder='What are you feeling?' />
         <div style={{margin:'auto'}}>
          <GoogleMap />
         </div>
      </div>  
    );
}

export default App
