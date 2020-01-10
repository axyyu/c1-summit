import React from 'react'

const Places = ({name, rating, price, address}) => {

    const button = {
        backgroudColor: '#CAD3C8',
        borderColor: '#000000',
    }

    return(
        <div>                        
            <button className='button places'>
                <div>
                    <div>{name}</div>
                    <div>{rating}</div>
                    <div>{price}</div>
                    <div>{address}</div>
                </div>
            </button>
        </div>
  )
}

export default Places
