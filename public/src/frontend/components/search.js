import React from "react";
import "./App.js";

export default class Search extends React.Component {
    state = {

    }
    

    change = e => {
		this.setState({[e.target.name]: e.target.value});
    };
    

    render() {
        return (
            <form>
                <input type="text" name="search" placeholder={this.props.placeholder}></input>
            </form>
        );
    }
}