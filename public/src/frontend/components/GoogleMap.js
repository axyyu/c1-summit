import React from 'react'
import './App.js'
import { Map, GoogleApiWrapper } from 'google-maps-react';

class GoogleApiWrapper extends React.Component {
    state = {}

    render() {
        return (
            <div>
                 <Map
                    google={this.props.google}
                    zoom={8}
                    style={mapStyles}
                    initialCenter={{ lat: 47.444, lng: -122.176 }} //change default center to first suggested location 
                />
            </div>
        );
    }
}

//export default GoogleMap

export default GoogleApiWrapper({
    apiKey: 'TOKEN HERE'
})(MapContainer);