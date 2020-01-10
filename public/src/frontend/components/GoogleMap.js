import React, { useState } from 'react'
import './App.js'
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react'

class GoogleMap extends React.Component {
  constructor(props) {
    super(props)

    // const displayFriends = () => {
    //   return friends.map((person, index) => {
    //     return <Marker key={index} id={index} position={{
    //      lat: person.latitude,
    //      lng: person.longitude
    //    }}
    //    onClick={() => console.log("You clicked me!")} /> //display which friend once clicked
    //   })
    // }

    // const displayRestaurant = () => {
    //     return <Marker position={{
    //        lat: restaurants[0].latitude,
    //        lng: restaurants[0].longitude
    //      }}
    //      onClick={() => console.log("You clicked me!")} /> //replace with some function
    //   }

    const mapStyle = {
      width: '50%',
      height: '50%'
    }

    const [location, setLocation] = useState(restaurants[0].location)
    const initialCenter = { lat: 47.444, lng: -122.176 }

    return (
      <div style={{ textAlign: 'right' }}>
        <Map
          google={this.props.google}
          zoom={8}
          style={mapStyle}
          initialCenter={initialCenter} //change default center to first suggested location
        >
          <Marker key='tester' id='1' position={initialCenter} />
          {this.displayFriends()}
          {this.displayRestaurant()}
        </Map>
      </div>
    )
  }
}

export default GoogleMap
