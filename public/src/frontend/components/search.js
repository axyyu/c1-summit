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
    const searchBar = {
      marginTop: '50px',
      marginBottom: '30px'
    }

    const input = {
      width: '80%',
      padding: '10px',
      outline: 'none',
      border: '1px solid #CAD3C8',
      fontSize: '1em'
    }

    return (
      <div style={searchBar}>
        <form>
          <input
            style={input}
            type='text'
            name='search'
            placeholder={this.props.placeholder}
          ></input>
        </form>
      </div>
    )
  }
}

export default Search
