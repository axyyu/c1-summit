import React, { useState } from 'react'
import GoogleMap from './components/GoogleMap'
import Drop from './components/Drop'
import Places from './components/Places'
import Direction from './components/Direction'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons'

const drop = {
  display: 'inline-block',
  marginLeft: '30px',
  marginTop: '30px'
}

const button = {
  backgroudColor: '#CAD3C8',
  borderColor: '#000000'
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
      location: { latitude: 47.444, longitude: -122.176 },
      numReviews: 500
    },
    {
      name: 'Chick-Fil-A',
      rating: '4/5',
      address: '8461 Leesburg Pike Ste B',
      price: '$',
      location: { latitude: 47.444, longitude: -122.176 },
      numReviews: 2345
    }
  ]
  const friends = ['Emily', 'Rachel', 'Christina', 'Willie', 'Eddie', 'Felix']
  const [restaurant, setRestaurant] = useState(restaurants[0]);

  return (
    <div>
    <div style={drop}>
      <div className='resultListView'>
        <div className='resultHeader' style={{ marginBottom: '20px' }}>
          {' '}
          <a href='/'>
            <button style={{ width: '100px' }}>
              &nbsp;&nbsp;&nbsp;&nbsp; Back
              <FontAwesomeIcon icon={faChevronLeft} style={{ float: 'left' }} />
            </button>
          </a>
          <div
            style={{
              display: 'inline-block',
              marginLeft: '30px',
              position: 'absolute'
            }}
          >
            <Drop style={{ float: 'top' }} title='Sort By' list={sort} />
          </div>
          <div
            style={{
              display: 'inline-block',
              marginLeft: '170px',
              position: 'absolute'
            }}
          >
            <Drop style={{ float: 'top' }} title='Filter' list={filter} />
          </div>
        </div>
        <div style={{ marginRop: '40px' }}>
          {restaurants.map(restaurant => (
            <Places
              name={restaurant.name}
              rating={restaurant.rating}
              address={restaurant.address}
              price={restaurant.price}
              onClick={() => setRestaurant(restaurant)}
              numReviews={restaurant.numReviews}
            />
          ))}
        </div>

        <div className='resultMap' style={{ marginLeft: '500px', textAlign:'center' }}>
            <GoogleMap
            style={{ margin: 'auto' }}
            friends={friends}
            restaurants={restaurants}
          />
        </div>
      </div>
    </div>
    <div><Direction style={{textAlign:'center', marginTop:'5000px', position:'absolute'}} restaurant={restaurant}/></div>
    </div>
  )
}

export default MapPage
