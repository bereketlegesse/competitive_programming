/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    const allRooms = new Set();
    for(let i = 0; i< rooms.length; i++){
        allRooms.add(i)
    }
    
    const visit = function(current) {
        if(allRooms.has(current)){
            allRooms.delete(current)
        }
        const avaliable = rooms[current];
        for(key of avaliable){
            if(allRooms.has(key)){
                visit(key)
            }      
        }
    }
    visit(0)
    return allRooms.size == 0 ? true:false; 
};