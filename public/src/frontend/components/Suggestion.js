import React from 'react'

const suggestionStyle = {
  border: '1px solid #CAD3C8',
  padding: '10px',
  width: '80%',
  color: '#2C3A47'
}

const Suggestion = ({ name }) => <div style={suggestionStyle}>{name}</div>

export default Suggestion
