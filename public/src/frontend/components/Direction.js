import React from 'react'

const Direction = ({restaurant}) => {
    const link = 'https://www.google.com/maps/search/?api=1&query=' + restaurant.location.latitude + ',' + restaurant.location.longitude
    console.log(link)

    return (
        <div>
            <a href={link}>
                <button style={{textAlign:'center'}}>Take me there!</button>
            </a>
        </div>
    );
}

export default Direction