function solution(A){      // A is the input array
    let res = new Array(2).fill(0);
    let temp = new Array(A.length + 1).fill(0);
    for(let i of A) {
        temp[i] += 1;
    }
    for(let i in temp) {
        if(temp[i] >= 2 && res[0] === 0 && i > 0) {
            res[0] = i;
        }
        if(temp[i] == 0 && res[1] === 0 && i > 0) {
            res[1] = i;
        }
    }
    
    return res;
}