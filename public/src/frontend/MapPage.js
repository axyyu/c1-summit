import React, { useState } from 'react'
import GoogleMap from './components/GoogleMap'
import Drop from './components/Drop'
import Places from './components/Places'
import Direction from './components/Direction'
import Select from 'react-dropdown-select'
import Tree from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'
import Sort from './components/Sort'
import Filter from './components/Filter'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons'
import { geolocated } from 'react-geolocated'

const drop = {
  display: 'inline-block',
  marginLeft: '30px',
}

const button = {
  backgroudColor: '#CAD3C8',
  borderColor: '#000000'
}

const sort = ['Rating', 'Distance', 'Category', 'Price']
const filter = ['Rating', 'Distance', 'Category', 'Price', 'Availability']
//const [location, setLocation] = useState()

const MapPage = ({
  coords,
  isGeolocationAvailable,
  isGeolocationEnabled,
  positionError
}) => {
  const currLocation =
    !isGeolocationAvailable || !isGeolocationEnabled || !coords
      ? { lat: 47.444, lng: -122.176 }
      : { lat: coords.latitude, lng: coords.longitude }
  const restaurants = [
    {
      name: "McDonald's",
      rating: '4.5/5',
      address: '7937 Tysons Corner Center',
      price: '$',
      location: { latitude: 38.9175726, longitude: -77.2377628 },
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
  const [selectedRestaurant, setSelectedRestaurant] = useState(restaurants[0])

  console.log(selectedRestaurant.name)

  return (
    <div>
      <div >
        <div style={{marginLeft:'30px', marginTop:'30px'}} className='resultListView'>
          <div style={drop} className='resultHeader' style={{ marginBottom: '20px', display:'inline-block' }}>
            {' '}
            <a href='/'>
              <button style={{ width: '100px', marginRight:'70px', marginBottom:'20px'}}>
                &nbsp;&nbsp;&nbsp;&nbsp; Back
                <FontAwesomeIcon
                  icon={faChevronLeft}
                  style={{ float: 'left' }}
                />
              </button>
            </a>
            <div style={{display:'inline-block'}}>
                <div style={{display:'inline-block'}}>Sort: <Sort /></div>
                <div style={{display:'inline-block', verticalAlign:'bottom'}}>Filter: <Filter /></div>
            </div>
          </div>
          <div style={{ marginTop: '40px', display:'block', position:'absolute' }}>
            {restaurants.map(restaurant => (
              <div onClick={() => setSelectedRestaurant(restaurant)}>
                <Places
                  name={restaurant.name}
                  rating={restaurant.rating}
                  address={restaurant.address}
                  price={restaurant.price}
                  numReviews={restaurant.numReviews}
                  isSelected={
                    restaurant.name == selectedRestaurant.name ? true : false
                  }
                />
              </div>
            ))}
          </div>
          <div
            className='resultMap'
            style={{ marginLeft: '500px', textAlign: 'center', display: 'block', marginTop:'40px'}}
          >
            <GoogleMap
              style={{ margin: 'auto', position:'relative'}}
              friends={friends}
              restaurants={restaurants}
              selectedRestaurant={selectedRestaurant}
              currLocation={currLocation}
            />
            <div style={{display:'block', verticalAlign:'bottom', marginLeft:'200px', marginTop:'400px', position:'absolute'}}>
            <Direction
              style={{
                textAlign: 'center',
                verticalAlign:'bottom'
              }}
              restaurant={selectedRestaurant}
            />
          </div>
          </div>
          
        </div>
      </div>
    </div>
  )
}

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false
  },
  userDecisionTimeout: 5000
})(MapPage)
