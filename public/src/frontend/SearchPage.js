import React, { useState, useEffect } from 'react'
import Search from './components/search.js'
import FriendCard from './components/FriendCard'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight, faTimes } from '@fortawesome/free-solid-svg-icons'
import MapPage from './MapPage'

const tagStyle = {
  padding: '5px 0'
}

const retreivingData = () => {
  fetch('http://127.0.0.1:5000/api/users', {})
    .then(res => {
      res.json()
    })
    .then(content => {
      return content
    })
}

const SearchPage = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [users, setUsers] = useState([])
  const [members, setMembers] = useState([])
  const [memberIDs, setMemberIDs] = useState([])
  const [showMap, setShowMap] = useState(false)
  const [loadingMap, setLoadingMap] = useState(false)
  const [results, setResults] = useState([])

  const outputGeneration = users => {
    fetch('http://127.0.0.1:5000/api/location', {
      method: 'post',
      body: JSON.stringify(users),
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      }
    })
      .then(res => {
        console.log(res)
        return res.json()
      })
      .then(content => {
        console.log(content)
        // const jsonData = JSON.parse(content)

        setResults(content)
        setLoadingMap(false)
      })
  }

  useEffect(() => {
    async function fetchData() {
      setIsLoading(true)
      const fetcher = await fetch('http://127.0.0.1:5000/api/users')
      const response = await fetcher.json()
      const arr = Object.keys(response).map(key => [key, response[key]])
      setUsers(arr)
      console.log(arr)
      setIsLoading(false)
    }
    fetchData()
  }, [])

  const Tag = ({ text, id }) => (
    <div style={tagStyle}>
      {text}{' '}
      <FontAwesomeIcon
        icon={faTimes}
        style={{ float: 'right', color: '#B33771', cursor: 'pointer' }}
        onClick={() => {
          setMembers(members.filter(item => item !== text))
          setMemberIDs(memberIDs.filter(item => item !== id))
        }}
      />
    </div>
  )

  return (
    <div>
      {loadingMap ? (
        <div>Loading</div>
      ) : showMap ? (
        <MapPage setShowMap={setShowMap} resultPlaces={results} />
      ) : (
        <div style={{ margin: '30px 100px' }}>
          <button
            style={{ float: 'right', width: '100px', zIndex: '1' }}
            onClick={() => {
              setShowMap(true)
              setLoadingMap(true)
              console.log(memberIDs)
              outputGeneration({ user_ids: memberIDs })
            }}
          >
            Next{' '}
            <FontAwesomeIcon icon={faChevronRight} style={{ float: 'right' }} />
          </button>

          <div style={{ width: '80%' }}>
            <h1 style={{ color: '#6D214F' }}>Find food with friends</h1>
            <h4>Who are you going with?</h4>
            {members.map(name => (
              <Tag text={name} id={memberIDs[members.indexOf(name)]} />
            ))}
            <Search
              placeholder='Search for group members...'
              resultsList={users}
              members={members}
              setMembers={setMembers}
              memberIDs={memberIDs}
              setMemberIDs={setMemberIDs}
            />
            <h4>Suggested Friends</h4>
            <div>
              {users
                .filter(user => !memberIDs.includes(user[0]))
                .map(user => (
                  <FriendCard
                    name={user[1].first + ' ' + user[1].last}
                    id={user[0]}
                    members={members}
                    setMembers={setMembers}
                    memberIDs={memberIDs}
                    setMemberIDs={setMemberIDs}
                  />
                ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default SearchPage
