// https://leetcode.com/problems/3sum

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_map<int,int> u;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++)
        {
            u[nums[i]]=i+1;
        }
        
        
        vector<vector<int> >ans;

        int c;
        for(int i=0;i<nums.size();)
        {
            for(int j=i+1;j<nums.size();)
            {
                c=-(nums[i]+nums[j]);
                int idx =u[c]-1;
               // cout<<i<<" "<<j<<" "<<idx<<endl;
                if(idx>j)
                {
                    vector<int> t;
                    t.push_back(nums[i]);
                    t.push_back(nums[j]);
                    t.push_back(c);
                    ans.push_back(t);
                }
               
                int temp=nums[j];
                while(j<nums.size()&&nums[j]==temp)
                {
                    j++;
                }
            }
            
             int temp=nums[i];
                while(i<nums.size()&&nums[i]==temp)
                {
                    i++;
                }
        }

        return ans;
    }
};