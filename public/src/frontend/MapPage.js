import React, { useState } from 'react'
import GoogleMap from './components/GoogleMap'
import Drop from './components/Drop'
import Places from './components/Places'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons'

const drop = {
  display: 'inline-block',
  marginLeft: '30px',
  marginTop: '30px'
}

const sort = ['Rating', 'Distance', 'Category', 'Price']
const filter = ['Rating', 'Distance', 'Category', 'Price', 'Availability']
//const [location, setLocation] = useState()

const MapPage = () => {
  const restaurants = [
    {
      name: "McDonald's",
      rating: '4.5/5',
      address: '7937 Tysons Corner Center',
      price: '$',
      location: { latitude: 47.444, longitude: -122.176 }
    },
    {
      name: 'Chick-Fil-A',
      rating: '4/5',
      address: '8461 Leesburg Pike Ste B',
      price: '$',
      location: { latitude: 47.444, longitude: -122.176 }
    }
  ]
  const friends = ['Emily', 'Rachel', 'Christina', 'Willie', 'Eddie', 'Felix']
  return (
    <div style={drop}>
      <div className='resultListView'>
        <a href='/'>
          <button style={{ width: '100px' }}>
            &nbsp;&nbsp;&nbsp;&nbsp; Back
            <FontAwesomeIcon icon={faChevronLeft} style={{ float: 'left' }} />
          </button>
        </a>
        <Drop title='Sort By' list={sort} />
        <Drop title='Filter' list={filter} />
        <div>
          {restaurants.map(restaurant => (
            <Places
              name={restaurant.name}
              rating={restaurant.rating}
              address={restaurant.address}
              price={restaurant.price}
            />
          ))}
        </div>

        <div className='resultMap' style={{ marginLeft: '500px' }}>
          <GoogleMap
            style={{ margin: 'auto' }}
            friends={friends}
            restaurants={restaurants}
          />
        </div>
      </div>
    </div>
  )
}

export default MapPage
