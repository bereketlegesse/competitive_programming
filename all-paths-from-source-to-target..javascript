/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    const store = [];
    const n = graph.length
    const dfs = (path,cur) => {
        if(path.length > 0 && path[path.length - 1] == n-1){
            store.push(path.slice());
        }
        for(neighbor of graph[cur]){
            path.push(neighbor);
            dfs(path,neighbor);
            path.pop();
        }
    }

    const path = [0];
    for(neighbor of graph[0]){
        path.push(neighbor);
        dfs(path, neighbor);
        path.pop();
    }
    return store;
};