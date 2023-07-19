// Problem: https://www.hackerrank.com/challenges/bear-and-steady-gene/

bool isvalid(map<char,int> a, int l){
    if(a['A'] <= l && a['G'] <= l && a['T'] <= l && a['C'] <= l) return true;
    
    return false;
}

int steadyGene(string gene) {
    int n = gene.size(), mini = n;
    map<char,int> am;
    for(char c: gene){
        am[c]++;
    }
    if(isvalid(am, gene.size()/4)){
        return 0;
    }
    
    int i = 0, j = 0;
    while(j < n){
        
        if(isvalid(am, gene.size()/4)){
            am[gene[i]]++;
            i++;
            mini = min(mini, (j - i + 1));
        }
        else{
            am[gene[j]]--;
            j++;
        }
        
    }
    return mini;
}