import React, { useState } from 'react'
import './App.js'
import Suggestion from './Suggestion'

const searchBar = {
  marginTop: '50px',
  marginBottom: '30px',
  width: '500px'
}

const Search = ({
  placeholder,
  resultsList,
  members,
  setMembers,
  memberIDs,
  setMemberIDs
}) => {
  const searchBar = {
    marginTop: '10px',
    marginBottom: '30px'
  }

  const input = {
    width: '100%',
    padding: '10px',
    outline: 'none',
    border: '1px solid #CAD3C8',
    fontSize: '1em'
  }

  const [active, setActive] = useState(false)
  const [query, setQuery] = useState('')

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
          onChange={e => setQuery(e.target.value)}
        ></input>
        {active && (
          <div>
            {resultsList
              .filter(user => {
                return !members.includes(user[1].first + ' ' + user[1].last)
              })
              .filter(user => {
                return (
                  (user[1].first + ' ' + user[1].last)
                    .toLowerCase()
                    .indexOf(query.toLowerCase()) >= 0
                )
              })
              .slice(0, 5)
              .map(user => {
                return (
                  <div
                    style={{ cursor: 'pointer' }}
                    onMouseDown={() => {
                      setMembers([
                        ...members,
                        user[1].first + ' ' + user[1].last
                      ])
                      setMemberIDs([...memberIDs, user[0]])
                    }}
                  >
                    <Suggestion name={user[1].first + ' ' + user[1].last} />
                  </div>
                )
              })}
          </div>
        )}
      </form>
    </div>
  )
}

export default Search
