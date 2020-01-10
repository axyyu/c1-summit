import React, {useState} from 'react'
import Tree from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'

const Sort = () => {
    const [selection, setSelection] = useState(null)

    const sort = [
        {label: 'Rating', value:'rating'},
        {label: 'Distance', value:'distance'},
        {label: 'Price', value:'price'}  
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