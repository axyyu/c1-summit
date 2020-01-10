import React from 'react'

const placesStyle = {
  padding: '0 10px',
  border: '1px solid #CAD3C8',
  boxSizing: 'border-box',
  width: '95%',
  float: 'left',
  marginRight: '5%',
  marginBottom: '20px'
}

const Places = ({ name, rating, address, price }) => (
  <div style={placesStyle}>
    <div>
      <b>
        <p style={{ float: 'left' }}>{name}</p>
      </b>
      <p style={{ float: 'right' }}>{rating}</p>
    </div>
    <div style={{ clear: 'both' }}>
      <i>
        <p style={{ float: 'left' }}>{address}</p>
      </i>
      <p style={{ float: 'right' }}>{price}</p>
    </div>
  </div>
)

export default Places
