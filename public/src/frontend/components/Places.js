import React from 'react'

const Places = ({
  name,
  rating,
  address,
  price,
  numReviews,
  isSelected,
  isRewards,
  rewardsPercent,
  isEfficient
}) => {
  const placesStyle = {
    padding: '0 10px',
    border: '1px solid #CAD3C8',
    boxSizing: 'border-box',
    width: '480px',
    float: 'left',
    marginRight: '5%',
    marginBottom: '20px',
    backgroundColor: isSelected ? '#CAD3C8' : 'white'
  }
  console.log(name)
  return (
    <div style={placesStyle}>
      <div>
        <b>
          <p style={{ float: 'left' }}>{name}</p>
        </b>
        <p style={{ float: 'right' }}>
          {numReviews} Reviews: {rating} stars
        </p>
      </div>
      <div style={{ clear: 'both' }}>
        <i>
          <p style={{ float: 'left' }}>{address}</p>
        </i>
        <p style={{ float: 'right' }}>{price}</p>
      </div>
      <i>
        <p style={{ clear: 'both', color: '#2d3436' }}>
          {isRewards &&
            'Earn ' +
              (Math.round(rewardsPercent * 100) / 100).toFixed(2) +
              '% higher rewards on your credit card for eating here.'}
        </p>
        <p style={{ clear: 'both', color: '#CAD3C8' }}>
          {isEfficient &&
            'This restaurant will best use your (and your party\'s) rewards points'}
        </p>
      </i>
    </div>
  )
}

export default Places
