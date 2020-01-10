import React from 'react'

const Places = ({name, rating, price, address}) => {

    return(
        <div>                        
            <button>
                <div>
                    {name}
                    {rating}
                    {price}
                    {address}
                </div>
            </button>
        </div>
  )
}

export default Places
