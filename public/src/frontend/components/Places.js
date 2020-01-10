import React from 'react'

const Places = ({ name, rating, price, address }) => {
  return (
    <div>
      <button>
        <div>
          {name}
          {rating}
          {price}
          {address}
        </div>
  )
}

export default Places
