import React from 'react'
import '../../styles/styles.css'
import Search from './Search.js'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

function App() {
  return (
    <div style={{ textAlign: 'center' }}>
      <div>Next</div> <FontAwesomeIcon icon={faChevronRight} />
      <Search placeholder='Who are you going with?' />
      <Search placeholder='What are you feeling?' />
    </div>
  )
}

export default App
