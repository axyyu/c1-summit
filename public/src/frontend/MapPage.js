import React from 'react'
import GoogleMap from './components/GoogleMap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

const MapPage = () => (
    <div style={{textAlign:'center', display:'inline-block'}}> 
        <GoogleMap />
    </div>
)

export default MapPage