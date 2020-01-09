import React, { useState } from 'react'
import Search from './components/search.js'
import FriendCard from './components/FriendCard'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

const SearchPage = () => {
  const testList = ['Friend One', 'Friend Two', 'Friend Three']
  const [members, setMembers] = useState([])
  return (
    <div style={{ margin: '30px 100px' }}>
      <button style={{ float: 'right', width: '100px' }}>
        Next{' '}
        <FontAwesomeIcon icon={faChevronRight} style={{ float: 'right' }} />
      </button>
      <h1>Find food with friends</h1>
      <div style={{ width: '80%' }}>
        <Search
          placeholder='What are you feeling?'
          resultsList={testList}
          members={members}
          setMembers={setMembers}
        />
        <Search
          placeholder={
            members.length > 0
              ? members.map(name => {
                  return `${name}`
                })
              : 'Who are you going with?'
          }
          resultsList={testList}
        />
        <div>
          {testList.map(friend => (
            <FriendCard
              name={friend}
              members={members}
              setMembers={setMembers}
            />
          ))}
        </div>
      </div>
    </div>
  )
}
export default SearchPage
