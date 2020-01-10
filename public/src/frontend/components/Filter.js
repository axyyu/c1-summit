import React from 'react'
import Tree from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'
const Filter = () => {
    const rating = [
        {label: '> 1 Star'},
        {label: '> 2 Star'},
        {label: '> 3 Star'},
        {label: '> 4 Star'},         
    ]

    const dist = [
        {label: '< 5 miles'},
        {label: '< 10 miles'},
        {label: '< 15 miles'},
        {label: '< 20 miles'},
        {label: '50+ miles'},
    ]
    
    const price = [
        {label: '< $'},
        {label: '< $$'},
        {label: '< $$$'},
        {label: '< $$$$'},
    ]

      const assignObjectPaths = (obj, stack) => {
        Object.keys(obj).forEach(k => {
          const node = obj[k];
          if (typeof node === "object") {
            node.path = stack ? `${stack}.${k}` : k;
            assignObjectPaths(node, node.path);
          }
        });
      };

    assignObjectPaths(rating);
    assignObjectPaths(dist);
    assignObjectPaths(price);

    return(
        <div>
           <div style={{display:'inline-block'}}>     
            <Tree 
                data={rating}
                mode='multiSelect'
                texts={{placeholder:'Rating'}}
                className="bootstrap-demo"
            /></div>

           <div style={{display:'inline-block'}}>
            <Tree 
                data={dist}
                mode='simpleSelect'
                texts={{placeholder:'Distance'}}
                className="bootstrap-demo"
            />
            </div>

            <div style={{display:'inline-block'}}>
            <Tree 
                data={price}
                mode='simpleSelect'
                className="bootstrap-demo"
                texts={{placeholder:'Price'}}
            />
            </div>
        </div>
    );
}

export default Filter