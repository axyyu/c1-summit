import React from 'react'
import './App.js'

const searchBar = {
  marginTop: '50px',
  marginBottom: '30px',
  width: '500px'
}

class Search extends React.Component {
  state = {}

  change = e => {
    this.setState({ [e.target.name]: e.target.value })
  }

  render() {
    return (
      <form style={searchBar}>
        <input
          type='text'
          name='search'
          placeholder={this.props.placeholder}
        ></input>
      </form>
    )
  }
}

export default Search
