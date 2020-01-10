import React from 'react'
import Tree from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'
const Sort = () => {
    const sort = [
        {label: 'Rating'},
        {label: 'Distance'},
        {label: 'Price'}  
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

    assignObjectPaths(sort);
    
    return(
        <div style={{marginRight:'50px'}}>
            <Tree 
                data={sort}
                mode='simpleSelect'
                className="bootstrap-demo"
            />
        </div>
    );
}

export default Sort