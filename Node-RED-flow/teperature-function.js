var paylTemp = msg.payload
if (paylTemp <= 30) {
    msgTemp = {payload: "Y"}
}
else if (paylTemp > 30) {
    msgTemp = {payload: "R"}
}
else {
    msgTemp = {payload: "O"}
}
return msgTemp;