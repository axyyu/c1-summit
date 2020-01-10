import React from 'react'
import Tree from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'
const Filter = () => {
    const rating = [
        {label: '> 1 Star', value:'1'},
        {label: '> 2 Star', value:'2'},
        {label: '> 3 Star', value:'3'},
        {label: '> 4 Star', value:'4'},         
    ]

    const dist = [
        {label: '< 5 miles', value:'5'},
        {label: '< 10 miles', value:'10'},
        {label: '< 15 miles', value:'15'},
        {label: '< 20 miles', value:'20'},
        {label: '50+ miles', value:'50'},
    ]
    
    const price = [
        {label: '< $', value:'one'},
        {label: '< $$', value:'two'},
        {label: '< $$$',value:'three'},
        {label: '< $$$$', value:'four'},
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