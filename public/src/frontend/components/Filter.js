import React from 'react'

class Filter extends React.Component {
    render() {
        return(
            <div id='filter' class="dropdown-check-list" tabindex="100">
                <span class='anchor'>
                    Filter
                </span>
                <ul class="items">
                    <li><input type="checkbox" />Rating</li>
                    <li><input type="checkbox" />Category</li>
                    <li><input type="checkbox" />Distance</li>
                    <li><input type="checkbox" />Price</li>
                    <li><input type="checkbox" />Availability</li>
                </ul>
            </div>
        );
    }
}

export default Filter