import React, { useState } from 'react'
import Search from './components/search.js'
import FriendCard from './components/FriendCard'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

const SearchPage = () => {
  const friendList = ['Friend One', 'Friend Two', 'Friend Three']
  return (
    <div style={{ margin: '30px 100px' }}>
      <button style={{ float: 'right', width: '100px' }}>
        Next{' '}
        <FontAwesomeIcon icon={faChevronRight} style={{ float: 'right' }} />
      </button>
      <h1>Find food with friends</h1>
      <div style={{ width: '80%' }}>
        <Search placeholder='What are you feeling?' resultsList={friendList} />
        <Search
          placeholder='Who are you going with?'
          resultsList={friendList}
        />
        <div>
          {friendList.map(friend => (
            <FriendCard name={friend} />
          ))}
        </div>
      </div>
    </div>
  )
}
export default SearchPage
