import React from 'react'
import './App.js'
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

class GoogleMap extends React.Component {

    constructor(props) {
        super(props);
    
        this.state = {
          restaurant: [],
          friends: []
        }
    }

    displayFriends = () => {
      return this.state.friends.map((person, index) => {
        return <Marker key={index} id={index} position={{
         lat: person.latitude,
         lng: person.longitude
       }}
       onClick={() => console.log("You clicked me!")} /> //display which friend once clicked
      })
    }

    displayRestaurant = () => {
        return <Marker position={{
           lat: this.state.restaurant.latitude,
           lng: this.state.restaurant.longitude
         }}
         onClick={() => console.log("You clicked me!")} /> //replace with some function
      }

    render() {
        const mapStyle = {
            width: '40%',
            height: '40%'
            
        };

        return (
            <div>
                 <Map
                    google={this.props.google}
                    zoom={8}
                    style={mapStyle}
                    initialCenter={{ lat: 47.444, lng: -122.176 }} //change default center to first suggested location 
                />
                {this.displayFriends()}
                {this.displayRestaurant()}
            </div>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyAiKw1PKQB59ICN0P4AODiRlLIuFcgUVYc'
})(GoogleMap);
