function validWordAbbreviation(word: string, abbr: string): boolean {
    let wordIndex = 0;
    let numAcc: string[] = [];

    //ts: checking isDigit
    const isNumber = (s: string) => Number.isNaN(Number(s)) === false;
    const moveForward = () => {
        if (numAcc.length>0) {
            if (numAcc[0] === '0'){ //-
                // no lead-0
                return false;
            }
            const num = parseInt(numAcc.join(''), 10); //12
            wordIndex+=num; // 13
            numAcc = [];
            return true;
        }
        return true;
    };

    for (let i=0; i<abbr.length; i++){ 
        const chAbbr = abbr.charAt(i); //ts: referencing chat in string
        if (isNumber(chAbbr)){
            numAcc.push(chAbbr); //ts: appending element to array
        } else {
            if(!moveForward()){
                return false;
            }
            const ch = word.charAt(wordIndex); // i
            if (ch !== chAbbr){
                return false;
            } else {
                wordIndex++;  //1
                continue;
            } 
        }

        if (i===abbr.length-1){
            if(!moveForward()){
                return false;
            }
        }
    }
    return wordIndex === word.length;
};