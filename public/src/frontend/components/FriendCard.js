import React from 'react'

const friendCardStyle = {
  padding: '10px',
  border: '1px solid black',
  width: '20%',
  float: 'left',
  margin: '0 2.5%',
  textAlign: 'center'
}

const FriendCard = ({ name }) => (
  <div style={friendCardStyle}>
    <p>{name}</p>
    <button>Add to Group</button>
  </div>
)

export default FriendCard
