import React from 'react'

class Sort extends React.Component {
    
    // onClick = e => {
    //     e.preventDefault();
    //     this.props.onClick();
    // }
    
    render() {
        return (
            <div>
                <div id='sort' class="dropdown-check-list" tabindex="100">
                    <span class='anchor'>
                        Sort
                    </span>
                </div>
         </div>
        );
    }
}

export default Sort