/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function(n, edges) {
    const nodes = new Set();
    for(let i = 0; i<n; i++){
        nodes.add(i);
    }

    for(edge of edges){
        if(nodes.has(edge[1])){
            nodes.delete(edge[1])
        }
    }
    const vertices = Array.from(nodes)
    return vertices
}