import React from 'react'
import GoogleMap from './components/GoogleMap'
import Sort from './components/Sort'
import Filter from './components/Filter'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

// onClick = e => {
//     let checkList = e.target;

// }
const drop = {
    textAlign: 'center',
    display: 'inline-block'
}

const MapPage = () => (
    <div style={drop}> 
        <div><Sort /></div>
        <div><Filter /></div>
        <div style={{textAlign:'right'}}>
            <GoogleMap />
        </div>
    </div>
)

export default MapPage