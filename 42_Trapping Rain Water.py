class Solution:
    def trap(self, height: List[int]) -> int:
        len_A = len(height)
        if 1 == len_A:
            return 0
        max_heights = [0] * len_A
        left_max = 0
        for i in range(0, len_A):
            if height[i] > left_max:
                left_max = height[i]
            max_heights[i] = left_max
        right_max = 0
        for i in range(len_A - 1, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            if right_max < max_heights[i]:
                max_heights[i] = right_max
        result = 0
        for i in range(0, len_A):
            if max_heights[i] > height[i]:
                result += (max_heights[i] - height[i])
        return result
		
		
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if(n<=2) return 0;
        int res = 0;
        stack<int> s;
        
        for(int i=0;i<n;++i) {
            if(s.empty()||height[i]<=height[s.top()])
                s.push(i);//递减则入递减栈
            else {
            	//出现非递减的元素，则为右边界，将栈当中小于此边界的元素弹出计算可储水的量。
                while(!s.empty()&&height[i]>height[s.top()]) {
                //这里一定是while循环 如果左边有多个元素小于当前压栈值 持续出栈计算面积 
                    int t = s.top();
                    s.pop();
                    //特殊情况 就是说没有左边界，此时需要判断栈是否为空如果为空直接跳出
                    if(!s.empty()) {
                    //根据左右边界计算面积
                        int l = s.top();
                        int h = min(height[l],height[i]) - height[t];
                        int w = i - l - 1;
                        res += h*w;
                    }
                }
                s.push(i);
            }
        }
        return res;
    }
};
