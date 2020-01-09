import React from 'react'

const friendCardStyle = {
  padding: '10px',
  border: '1px solid #CAD3C8',
  boxSizing: 'border-box',
  width: '20%',
  float: 'left',
  marginRight: '5%',
  textAlign: 'center'
}

const FriendCard = ({ name, members, setMembers }) => (
  <div style={friendCardStyle}>
    <p>{name}</p>
    <button
      style={{ backgroundColor: '#58B19F', marginBottom: '15px' }}
      onClick={() => setMembers([...members, name])}
    >
      Add to Group
    </button>
  </div>
)

export default FriendCard
