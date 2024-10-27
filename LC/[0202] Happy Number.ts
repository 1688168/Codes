function isHappy(n: number): boolean {
    let n1 = n; //slow
    let n2 = n; //fast

    const process = (nn: number) => {
        let ttl: number=0;
        while(nn>0){
            let dd: number = nn%10;
            //console.log(`dd: [${dd}]`);
            ttl = ttl + dd*dd;
            nn = (nn/10) | 0; //ts: cast float to integer (genius)
        }
        return ttl;
    }

    while(1==1){
        n1 = process(n1);
        n2 = process(process(n2));
        //console.log(`n1=[${n1}], n2=[${n2}]`);
        if(n1==1 || n2==1) return true;
        if(n1==n2) break;
     
    }

    return false;
};