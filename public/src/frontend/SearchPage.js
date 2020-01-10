import React, { useState } from 'react'
import Search from './components/search.js'
import FriendCard from './components/FriendCard'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight, faTimes } from '@fortawesome/free-solid-svg-icons'

const tagStyle = {
  padding: '5px 0'
}

const SearchPage = () => {
  const testList = [
    'Emily Lu',
    'Christina Lu',
    'Rachel Lu',
    'Eddie Tu',
    'Willie Xia',
    'Andrew Wang',
    'Felix Hu'
  ]
  const [members, setMembers] = useState([])
  const Tag = ({ text }) => (
    <div style={tagStyle}>
      {text}{' '}
      <FontAwesomeIcon
        icon={faTimes}
        style={{ float: 'right', color: '#B33771', cursor: 'pointer' }}
        onClick={() => setMembers(members.filter(item => item !== text))}
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
        <h4>What are you feeling?</h4>
        <Search
          placeholder='Add options...'
          resultsList={testList}
          members={members}
          setMembers={setMembers}
        />
        <h4>Who are you going with?</h4>
        {members.map(name => (
          <Tag text={name} />
        ))}
        <Search
          placeholder='Add group members...'
          resultsList={testList}
          members={members}
          setMembers={setMembers}
        />
        <h4>Suggested Friends</h4>
        <div>
          {testList
            .filter(name => !members.includes(name))
            .map(friend => (
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
