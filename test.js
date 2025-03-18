function minMeet(intervals){
    if(intervals.length === 0) return null;
    
    let start=[];
    let end=[];
    for(let i=0; i<intervals.length; i++){
        start[i]=intervals[i][0];
        end[i]=intervals[i][1];
        // start.push(intervals[i][0]);
        // end.push(intervals[i][1]);
    }
    console.log(start);
    console.log(end);
    start.sort((a, b) => a - b);
    end.sort((a, b) => a - b);
    console.log(start);
    console.log(end);   
}
minMeet([[7,10],[2,4]]); 