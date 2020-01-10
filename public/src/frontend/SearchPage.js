import React, { useState, useEffect } from 'react'
import Search from './components/search.js'
import FriendCard from './components/FriendCard'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight, faTimes } from '@fortawesome/free-solid-svg-icons'

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

const outputGeneration = (ArrayofIDS) => {
    fetch('http://127.0.0.1:5000/api/location', {
        method: "POST",
        body: JSON.stringify({ "user_ids": ArrayofIDS })
    }).then((res) => {
        res.json()
    }
    ).then((content) => {
        return content
    }
    )
}

/***
 * peopleArray = JSON.stringify({'people': ['Anna', 'ty']})
 * */

const SearchPage = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [users, setUsers] = useState([])
  const [members, setMembers] = useState([])
  const [memberIDs, setMemberIDs] = useState([])

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
    <div style={{ margin: '30px 100px' }}>
      <a href='results'>
        <button style={{ float: 'right', width: '100px', zIndex: '1' }}>
          Next{' '}
          <FontAwesomeIcon icon={faChevronRight} style={{ float: 'right' }} />
        </button>
      </a>
      <div style={{ width: '80%' }}>
        <h1 style={{ color: '#6D214F' }}>Find food with friends</h1>
        <h4>Who are you going with?</h4>
        {members.map(name => (
          <Tag text={name} id={memberIDs[members.indexOf(name)]} />
        ))}
        <Search
          placeholder='Add group members...'
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
  )
}

export default SearchPage
