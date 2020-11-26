var paylDist = msg.payload
if (paylDist >= 1 && paylDist < 10) {
    msgDist = {payload: "g"}
}
else if (paylDist >= 10 && paylDist < 20) {
    msgDist = {payload: "y"}
}
else if (paylDist >= 20 && paylDist < 30 || paylDist < 1) {
    msgDist = {payload: "r"}
}
else { msgDist = {payload: "o"}
}
return msgDist;