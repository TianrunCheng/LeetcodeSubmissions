// https://leetcode.com/problems/valid-number

class Solution {
public:
    bool isNumber(string s) {
        
        // solution found in discussion
        int i = 0;
        if(s[i] == '-' || s[i] == '+')
            i++;
        
        int digits = 0; 
        int dots = 0;
        while(i < s.length() && (s[i]=='.' || isdigit(s[i]))) // isdigit(): a C++ ctype function
            isdigit(s[i++])?digits++:dots++;
        // i increment done after evaluation
        
        /* prefix(++i) will be done before rest of the expression;
           postfix(i++), increment or decrement will be done after the complete expression is evaluated.*/
        // c = a++; // a is 20: after evaluation c is 20, a becomes 21 after this
        // c = ++a; // after evaluation c is 22, a is 22
        
        if(dots >1 ||digits == 0 )
            return false;
        
        digits = 0;
        dots = 0;
        if(s[i] == 'e' || s[i] == 'E')
        {
            i++;
            if(s[i] == '-' || s[i] == '+')
                i++;
            while(i < s.length() && (s[i]=='.' || isdigit(s[i])))
                isdigit(s[i++])?digits++:dots++;
            
            if(digits == 0 || dots>0)
                return false;
        }
        
        return i == s.length();
        
    }
};