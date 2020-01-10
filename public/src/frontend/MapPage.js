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
  marginLeft: '30px'
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
  positionError,
  setShowMap,
  resultPlaces
}) => {
  const currLocation =
    !isGeolocationAvailable || !isGeolocationEnabled || !coords
      ? { lat: 38.9188781, lng: -77.2221362 }
      : { lat: coords.latitude, lng: coords.longitude }
  const restaurants = [
    {
      name: 'Doyle',
      formatted_address: '1500 New Hampshire Ave NW, Washington, DC 20036',
      latitude: 38.910362,
      longitude: -77.043081,
      price_level: 3,
      rating: 4.1,
      user_ratings_total: 147,
      cuisine: 'cocktailbars'
    }
  ]
  const friends = ['Emily', 'Rachel', 'Christina', 'Willie', 'Eddie', 'Felix']
  const [selectedRestaurant, setSelectedRestaurant] = useState(restaurants[0])

  return (
    <div style={{ backgroundColor: 'white' }}>
      <div>
        <div
          style={{ marginLeft: '30px', marginTop: '30px' }}
          className='resultListView'
        >
          <div
            style={drop}
            className='resultHeader'
            style={{ marginBottom: '20px', display: 'inline-block' }}
          >
            {' '}
            <button
              onClick={() => setShowMap(false)}
              style={{
                width: '100px',
                marginRight: '70px',
                marginBottom: '20px'
              }}
            >
              &nbsp;&nbsp;&nbsp;&nbsp; Back
              <FontAwesomeIcon icon={faChevronLeft} style={{ float: 'left' }} />
            </button>
            <div style={{ display: 'inline-block' }}>
              <div style={{ display: 'inline-block' }}>
                Sort: <Sort />
              </div>
              <div style={{ display: 'inline-block', verticalAlign: 'bottom' }}>
                Filter: <Filter />
              </div>
            </div>
          </div>
          <div
            style={{
              marginTop: '40px',
              display: 'block',
              position: 'absolute'
            }}
          >
            {resultPlaces.map(restaurant => {
              return (
                <div onClick={() => setSelectedRestaurant(restaurant)}>
                  <Places
                    name={restaurant.name}
                    rating={restaurant.rating}
                    address={restaurant.formatted_address}
                    price={restaurant.price_level}
                    numReviews={restaurant.user_ratings_total}
                    isSelected={
                      restaurant.name == selectedRestaurant.name ? true : false
                    }
                    isRewards={
                      restaurant.rating > 4.4 &&
                      restaurant.user_ratings_total > 1050
                    }
                    rewardsPercent={Math.sqrt(restaurant.rating)}
                    cuisine={restaurant.cuisine}
                  />
                </div>
              )
            })}
          </div>
          <div
            className='resultMap'
            style={{
              marginLeft: '500px',
              textAlign: 'center',
              display: 'block',
              marginTop: '40px'
            }}
          >
            <GoogleMap
              style={{ margin: 'auto', position: 'relative' }}
              friends={friends}
              restaurants={restaurants}
              selectedRestaurant={selectedRestaurant}
              currLocation={currLocation}
            />
            <div
              style={{
                display: 'block',
                verticalAlign: 'bottom',
                marginLeft: '200px',
                marginTop: '400px',
                position: 'absolute'
              }}
            >
              <Direction
                style={{
                  textAlign: 'center',
                  verticalAlign: 'bottom'
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
