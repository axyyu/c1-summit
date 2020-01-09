import React from 'react'
import Search from './components/search.js'
import Suggestion from './components/Suggestion'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronRight } from '@fortawesome/free-solid-svg-icons'

const friendSuggestions = ['Christina Lu', 'Emily Lu']

const SearchPage = () => (
  <div style={{ margin: '30px 100px' }}>
    <button className='button'>
      Next <FontAwesomeIcon icon={faChevronRight} style={{ float: 'right' }} />
    </button>
    <h1>Find food with friends</h1>
    <Search placeholder='Who are you going with?' />
    <Suggestion name='Christina Lu' />
    <Search placeholder='What are you feeling?' />
  </div>
)

export default SearchPage
