import React, { useState } from 'react'
import './App.js'
import Suggestion from './Suggestion'

const searchBar = {
  marginTop: '50px',
  marginBottom: '30px',
  width: '500px'
}

const Search = ({ placeholder, resultsList }) => {
  const searchBar = {
    marginTop: '50px',
    marginBottom: '30px'
  }

  const input = {
    width: '100%',
    padding: '10px',
    outline: 'none',
    border: '1px solid #2C3A47',
    fontSize: '1em'
  }

  const [active, setActive] = useState(false)

  return (
    <div style={searchBar}>
      <form>
        <input
          style={input}
          type='text'
          name='search'
          autocomplete='off'
          placeholder={placeholder}
          onFocus={() => setActive(true)}
          onBlur={() => setActive(false)}
        ></input>
        {active && (
          <div>
            {resultsList.map(item => {
              return <Suggestion name={item} />
            })}
          </div>
        )}
      </form>
    </div>
  )
}

export default Search
