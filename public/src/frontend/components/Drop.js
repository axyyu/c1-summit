import React, { useState } from 'react'


const Drop = ({title, list}) => {
    const [active, setActive] = useState(false)
    
    const onClick = e => {
        e.preventDefault();
        if (active) 
            setActive(false);
        else 
            setActive(true);
    }

    const button = {
        backgroundColor: '#CAD3C8',
        color: '#000000',
        height: '40px',
        display: 'block',
        marginLeft: '20px',
        marginRight: '20px',
    }

    const checkbox = {
        padding: '5px',
        textAlign: 'left',
        marginLeft: '13px'
    }

    return(
        <div className='dropdown-check-list' tabIndex="100">
           <span><button style={button} className='anchor' onClick ={() => setActive(!active)}>{title}</button></span> 
            {active && (
                <div>
                    {list.map(item => {
                    return <div style={checkbox}><input type='checkbox' name={item} />{item}</div>
                    })}
                 </div>
            )}
        </div>
    );
}

export default Drop