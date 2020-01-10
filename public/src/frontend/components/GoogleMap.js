import React, { useState } from 'react'
import './App.js'
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react'

class GoogleMap extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      friends: [],
      restaurants: []
    }
  }

  displayFriends = () => {
    return this.state.friends.map((person, index) => {
      return (
        <Marker
          key={index}
          id={index}
          position={{
            lat: person.latitude,
            lng: person.longitude
          }}
          onClick={() => console.log('You clicked me!')}
        />
      ) //display which friend once clicked
    })
  }

  displayRestaurant = () => {
    return (
      <Marker
        position={{
          lat: this.props.restaurants[0].location.latitude,
          lng: this.props.restaurants[0].location.longitude
        }}
        onClick={() => console.log('You clicked me!')}
      />
    ) //replace with some function
  }

  render() {
    const mapStyle = {
      width: '50%',
      height: '50%'
    }

    //const [location, setLocation] = useState(this.state.restaurants[0].location);
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

export default GoogleApiWrapper({
  apiKey: 'AIzaSyAiKw1PKQB59ICN0P4AODiRlLIuFcgUVYc'
})(GoogleMap)
