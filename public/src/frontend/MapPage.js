import React from 'react'
import GoogleMap from './components/GoogleMap'
import Sort from './components/Sort'
import Filter from './components/Filter'
import Drop from './components/Drop'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons'

const drop = {
    textAlign: 'center',
    display: 'inline-block',
}

const sort = ['Rating','Distance', 'Category', 'Price']
const filter = ['Rating', 'Distance', 'Category', 'Price', 'Availability']

const MapPage = () => (
    <div style={drop}> 
        <button style={{ float: 'right', width: '100px' }}>
            &nbsp;&nbsp;&nbsp;&nbsp; Back
            <FontAwesomeIcon icon={faChevronLeft} style={{ float: 'left' }} />
        </button>
            <Drop title='Sort By' list={sort}/>
            <Drop title='Filter' list={filter}/>
            <GoogleMap style={{margin:'auto'}}/>
    </div>
)

export default MapPage