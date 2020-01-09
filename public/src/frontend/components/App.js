import React from 'react'
import '../../styles/styles.css'
import SearchPage from '../SearchPage'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'

function App() {
  return (
    <Router>
      <Switch>
        <Route path='/test'>hello this is a test!</Route>
        <Route path='/'>
          <SearchPage />
        </Route>
      </Switch>
    </Router>
  )
}

export default App
