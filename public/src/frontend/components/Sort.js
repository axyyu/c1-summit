import React from 'react'
import Tree from 'react-dropdown-tree-select'
import './App.js'
import 'react-dropdown-tree-select/dist/styles.css'


class Sort extends React.Component {

    state = {
        value: ''
    } 

	//automatically updates state values as input changes in real time in each field
	change = e => {
		this.setState({value: e.target.value});
	};

    assignObjectPaths = (obj, stack) => {
        Object.keys(obj).forEach(k => {
          const node = obj[k];
          if (typeof node === "object") {
            node.path = stack ? `${stack}.${k}` : k;
            this.assignObjectPaths(node, node.path);
          }
        });
      };


    render () {
        const sort = [
            {label: 'Rating', value:'rating'},
            {label: 'Distance', value:'distance'},
            {label: 'Price', value:'price'}  
        ]

        const onChange = e => {
            this.props.onChange(e.value)
        }

        this.assignObjectPaths(sort);

        return(
            <div style={{marginRight:'50px'}}>
                <Tree 
                    data={sort}
                    mode='simpleSelect'
                    className="bootstrap-demo"
                    onChange={e => onChange(e)}
                />
            </div>
        );
    }   
}

export default Sort