import React from 'react'
import Tree from 'react-dropdown-tree-select'
import "../../styles/styles.css"

const Sort = () => {
    const sort = [
        {label: 'Rating'},
        {label: 'Distance'},
        {label: 'Category'},
        {label: 'Price'}  
    ]

    const onChange = (currentNode, selectedNodes) => {
        console.log("path::", currentNode.path);
      };
      
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
        <div>
            <Tree 
                data={sort}
                mode='radioSelect'
                onChange={onChange}
                className="bootstrap-demo"
            />
        </div>
    );
}

export default Sort