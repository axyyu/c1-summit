import React from 'react'

const suggestionStyle = {
  border: '1px solid #C4C4C4',
  padding: '10px',
  width: '80%'
}

const Suggestion = ({ name }) => <div style={suggestionStyle}>{name}</div>

export default Suggestion
