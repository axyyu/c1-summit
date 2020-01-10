import React, { useState } from 'react'
import { sin, cos, atan2, sqrt } from 'mathjs'
import GoogleMap from './components/GoogleMap'
import Places from './components/Places'
import Direction from './components/Direction'
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
  const friends = ['Emily', 'Rachel', 'Christina', 'Willie', 'Eddie', 'Felix']
  let results = require('./test.json')
  console.log(results)
  const [restaurants, setRestaurants] = useState(results.places)
  const [selectedRestaurant, setSelectedRestaurant] = useState(restaurants[0])

  const refine = () => {

  }

  const distance = (r) => {
        let lon1 = currLocation.lng
        let lat1 = currLocation.lat
        let lon2 = r.longitude
        let lat2 = r.latitude
        let pi = 3.14159265358979323846264338327950
        let R = 6378.137; //Radius of earth in KM 
        let dLat = lat2 * pi / 180.0 - lat1 * pi / 180.0
        let dLon = lon2 * pi / 180.0 - lon1 * pi / 180.0
        let a = sin(dLat/2.0) * sin(dLat/2.0) + cos(lat1 * pi / 180.0) * cos(lat2 * pi / 180.0) * sin(dLon/2.0) * sin(dLon/2.0)
        let c = 2.0 * atan2(sqrt(a), sqrt(1-a))
        let d = R * c
        return d * 1000.0 * 0.000621371; //miles
  }

  console.log(selectedRestaurant.name)
    const onChange = field => {
        console.log('calling change')
        let select = field
        console.log(select)
        let myData = []
        if (select === 'rating') {
        setRestaurants(restaurants.sort((a, b) => {
            if (a.rating < b.rating)
                return 1;
            else if (a.rating > b.rating)   
                return -1;
            return 0;
        }))
            console.log(restaurants)
        } else if (select === 'distance') {
            setRestaurants(restaurants.sort((a, b) => {
                if (distance(a) > distance(b))
                    return 1;
                else if (a.price_level < b.price_level)
                    return -1;
                return 0;
            }))
                console.log(restaurants)
        } else if (select === 'price') {
            setRestaurants(restaurants.sort((a, b) => {
                if (a.price_level > b.price_level)
                    return 1;
                else if (a.price_level < b.price_level)
                    return -1;
                return 0;
            }))
                console.log(restaurants)
        }
    }

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
                Sort: <Sort onChange={value => onChange(value)}/>
              </div>
              <div style={{ display: 'inline-block', verticalAlign: 'bottom' }}>
                Filter: <Filter />
              </div>
              {/* <div style={{display:'inline-block', marginLeft:'20px', verticalAlign:'bottom'}}></div><button onClick={() => this.forceUpdate()}>Submit</button> */}
            </div>
          </div>
          <div
            style={{
              marginTop: '40px',
              display: 'block',
              position: 'absolute'
            }}
          >
            {restaurants.map(restaurant => (
              <div onClick={() => {setSelectedRestaurant(restaurant)}}>
                <Places
                  name={restaurant.name}
                  rating={restaurant.rating}
                  address={restaurant.formatted_address}
                  price={restaurant.price_level}
                  numReviews={restaurant.user_ratings_total}
                  isSelected={
                    restaurant.name == selectedRestaurant.name ? true : false
                  }
                  cuisine={restaurant.cuisine}
                />
              </div>
            ))}
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
